# LC_ZBIERZ_DANE 1.0.0 - Windows PowerShell 5.1; odczyt gry, zapis tylko poza nia.
# Limbus Company (Steam 1973530): kopiuje pliki lokalizacji z
# LimbusCompany_Data\Assets\Resources_moved\Localize (kr/en/jp), spis nazw plikow
# LimbusCompany_Data oraz Lang\config.json. Niczego nie zmienia w grze i nie laczy sie z siecia.
[CmdletBinding()]
param(
    [Parameter(Position = 0)] [string] $GameRoot = '',
    [string] $OutputDirectory = '',
    [string] $SteamRoot = '',
    [ValidateSet('pelny', 'aktualizacja')] [string] $Tryb = 'pelny',
    [string] $KatalogStanu = '',
    [long] $LimitCzesciBajtow = 314572800,
    [switch] $BezStanu,
    [switch] $NonInteractive
)

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
$script:Version = 'LC_ZBIERZ_DANE 1.0.0'
$script:AppId = '1973530'
$script:DataDirName = 'LimbusCompany_Data'
$script:LocalizeRelative = 'Assets/Resources_moved/Localize'
$script:AllowedSuffixes = @('.json', '.txt', '.csv', '.tsv', '.xml', '.yaml', '.yml', '.md')
$script:MaxSingleFile = 67108864
$script:MaxInventory = 250000
$script:Problems = New-Object 'System.Collections.Generic.List[object]'
$script:Skipped = New-Object 'System.Collections.Generic.List[object]'
$script:Utf8 = New-Object System.Text.UTF8Encoding($false)

function Add-Problem([string] $Relative, [string] $Reason) {
    [void] $script:Problems.Add([ordered]@{ sciezka = $Relative; powod = $Reason })
}

function Add-Skipped([string] $Relative, [string] $Reason, [long] $Size) {
    [void] $script:Skipped.Add([ordered]@{ sciezka = $Relative; powod = $Reason; rozmiar = $Size })
}

function ConvertTo-JsonString([string] $Value) {
    $builder = New-Object System.Text.StringBuilder
    [void] $builder.Append('"')
    foreach ($ch in $Value.ToCharArray()) {
        $code = [int] $ch
        if ($ch -eq '"') { [void] $builder.Append('\"') }
        elseif ($ch -eq '\') { [void] $builder.Append('\\') }
        elseif ($code -lt 32) { [void] $builder.Append(('\u{0:x4}' -f $code)) }
        else { [void] $builder.Append($ch) }
    }
    [void] $builder.Append('"')
    return $builder.ToString()
}

function Get-Sha256Hex([byte[]] $Bytes) {
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try {
        return ([System.BitConverter]::ToString($sha.ComputeHash($Bytes))).Replace('-', '').ToLowerInvariant()
    } finally { $sha.Dispose() }
}

function Test-Reparse($Item) {
    return (($Item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0)
}

function Get-RelativePath([string] $Base, [string] $Full) {
    $relative = $Full.Substring($Base.Length).TrimStart('\', '/')
    return ($relative -replace '\\', '/')
}

function Resolve-GameRootCandidate([string] $Path) {
    if ([string]::IsNullOrWhiteSpace($Path)) { return $null }
    try {
        $item = Get-Item -LiteralPath $Path.Trim('"') -Force -ErrorAction Stop
    } catch { return $null }
    if (-not $item.PSIsContainer) { return $null }
    if ($item.Name -ieq $script:DataDirName) { $item = $item.Parent }
    $data = Join-Path $item.FullName $script:DataDirName
    if (Test-Path -LiteralPath $data -PathType Container) {
        return $item.FullName.TrimEnd('\', '/')
    }
    return $null
}

function Get-AcfValue([string] $Path, [string] $Key) {
    try {
        if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) { return '' }
        $text = [IO.File]::ReadAllText($Path)
        $pattern = '(?im)^\s*"' + [regex]::Escape($Key) + '"\s*"([^"\r\n]*)"'
        $match = [regex]::Match($text, $pattern)
        if ($match.Success) { return $match.Groups[1].Value }
    } catch { }
    return ''
}

function Find-SteamGameRoots([string] $Override) {
    $steamDirs = New-Object 'System.Collections.Generic.List[string]'
    if (-not [string]::IsNullOrWhiteSpace($Override)) {
        [void] $steamDirs.Add($Override)
    } else {
        foreach ($registry in @('HKCU:\Software\Valve\Steam', 'HKLM:\SOFTWARE\WOW6432Node\Valve\Steam')) {
            try {
                $props = Get-ItemProperty -LiteralPath $registry -ErrorAction Stop
                foreach ($value in @($props.SteamPath, $props.InstallPath)) {
                    if (-not [string]::IsNullOrWhiteSpace($value)) { [void] $steamDirs.Add(($value -replace '/', '\')) }
                }
            } catch { }
        }
    }
    $libraries = New-Object 'System.Collections.Generic.List[string]'
    foreach ($steam in $steamDirs) {
        [void] $libraries.Add($steam)
        $vdf = Join-Path $steam 'steamapps\libraryfolders.vdf'
        try {
            if (Test-Path -LiteralPath $vdf -PathType Leaf) {
                $text = [IO.File]::ReadAllText($vdf)
                foreach ($m in [regex]::Matches($text, '(?im)^\s*"path"\s*"([^"\r\n]+)"')) {
                    [void] $libraries.Add(($m.Groups[1].Value -replace '\\\\', '\'))
                }
            }
        } catch { }
    }
    $found = New-Object 'System.Collections.Generic.List[string]'
    foreach ($library in ($libraries | Select-Object -Unique)) {
        $acf = Join-Path $library ('steamapps\appmanifest_' + $script:AppId + '.acf')
        $installDir = Get-AcfValue $acf 'installdir'
        if ([string]::IsNullOrWhiteSpace($installDir)) { $installDir = 'Limbus Company' }
        $candidate = Resolve-GameRootCandidate (Join-Path $library ('steamapps\common\' + $installDir))
        if ($null -ne $candidate -and -not $found.Contains($candidate)) { [void] $found.Add($candidate) }
    }
    return ,$found
}

function Select-GameRoot {
    $direct = Resolve-GameRootCandidate $GameRoot
    if (-not [string]::IsNullOrWhiteSpace($GameRoot)) {
        if ($null -eq $direct) { throw 'Wskazany folder nie zawiera LimbusCompany_Data. Wskaz glowny folder gry.' }
        return $direct
    }
    $roots = Find-SteamGameRoots $SteamRoot
    if ($roots.Count -eq 1) { return $roots[0] }
    if ($roots.Count -gt 1) {
        if ($NonInteractive) { throw 'Znaleziono kilka instalacji gry; podaj folder jako parametr.' }
        Write-Host 'Znaleziono kilka instalacji Limbus Company:'
        for ($i = 0; $i -lt $roots.Count; $i++) { Write-Host ('  [{0}] {1}' -f ($i + 1), $roots[$i]) }
        $answer = Read-Host 'Podaj numer'
        $index = 0
        if ([int]::TryParse($answer, [ref] $index) -and $index -ge 1 -and $index -le $roots.Count) { return $roots[$index - 1] }
        throw 'Nie wybrano instalacji.'
    }
    if ($NonInteractive) { throw 'Nie znaleziono gry w bibliotekach Steam; podaj folder jako parametr.' }
    Write-Host 'Nie znaleziono gry w bibliotekach Steam. Wskaz glowny folder gry (ten z LimbusCompany_Data).'
    Add-Type -AssemblyName System.Windows.Forms
    $dialog = New-Object System.Windows.Forms.FolderBrowserDialog
    $dialog.Description = 'Wskaz glowny folder Limbus Company (z folderem LimbusCompany_Data)'
    if ($dialog.ShowDialog() -ne [System.Windows.Forms.DialogResult]::OK) { throw 'Nie wybrano folderu gry.' }
    $chosen = Resolve-GameRootCandidate $dialog.SelectedPath
    if ($null -eq $chosen) { throw 'Wybrany folder nie zawiera LimbusCompany_Data.' }
    return $chosen
}

function Get-OutputDirectory {
    $dir = $OutputDirectory
    if ([string]::IsNullOrWhiteSpace($dir)) { $dir = [Environment]::GetFolderPath('Desktop') }
    if ([string]::IsNullOrWhiteSpace($dir)) { $dir = $env:USERPROFILE }
    if (-not (Test-Path -LiteralPath $dir -PathType Container)) { [void] (New-Item -ItemType Directory -Path $dir) }
    return (Get-Item -LiteralPath $dir).FullName.TrimEnd('\', '/')
}

function Get-StateFile {
    $dir = $KatalogStanu
    if ([string]::IsNullOrWhiteSpace($dir)) { $dir = Join-Path $env:LOCALAPPDATA 'LC_ZBIERACZ_STAN' }
    return (Join-Path $dir 'stan_wyslanych.json')
}

function Read-State([string] $Path) {
    $state = @{}
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) { return $state }
    $data = [IO.File]::ReadAllText($Path, $script:Utf8) | ConvertFrom-Json
    if ($data.format -ne 'lc-zbieracz-stan-v1') { throw 'Plik stanu ma nieznany format. Usun go albo uruchom z -BezStanu.' }
    foreach ($prop in $data.pliki.PSObject.Properties) { $state[$prop.Name] = [string] $prop.Value }
    return $state
}

function Write-State([string] $Path, [hashtable] $Hashes, [string] $BuildId) {
    $dir = Split-Path -Parent $Path
    if (-not (Test-Path -LiteralPath $dir -PathType Container)) { [void] (New-Item -ItemType Directory -Path $dir) }
    $lines = New-Object 'System.Collections.Generic.List[string]'
    foreach ($key in ($Hashes.Keys | Sort-Object)) {
        [void] $lines.Add('    ' + (ConvertTo-JsonString $key) + ': ' + (ConvertTo-JsonString $Hashes[$key]))
    }
    $text = "{`n  ""format"": ""lc-zbieracz-stan-v1"",`n  ""buildid"": " + (ConvertTo-JsonString $BuildId) +
        ",`n  ""zapisano_utc"": " + (ConvertTo-JsonString ([DateTime]::UtcNow.ToString('o'))) +
        ",`n  ""pliki"": {`n" + ($lines -join ",`n") + "`n  }`n}`n"
    $tmp = $Path + '.tmp'
    [IO.File]::WriteAllText($tmp, $text, $script:Utf8)
    Move-Item -LiteralPath $tmp -Destination $Path -Force
}

function Add-ZipEntry($Zip, [string] $Name, [byte[]] $Bytes) {
    $entry = $Zip.CreateEntry($Name, [System.IO.Compression.CompressionLevel]::Optimal)
    $stream = $entry.Open()
    try { $stream.Write($Bytes, 0, $Bytes.Length) } finally { $stream.Dispose() }
}

function Main {
    Add-Type -AssemblyName System.IO.Compression
    Add-Type -AssemblyName System.IO.Compression.FileSystem

    $running = Get-Process -Name 'LimbusCompany' -ErrorAction SilentlyContinue
    if ($null -ne $running) { throw 'Limbus Company jest uruchomione. Zamknij gre i uruchom ponownie.' }

    $root = Select-GameRoot
    $data = (Get-Item -LiteralPath (Join-Path $root $script:DataDirName)).FullName.TrimEnd('\', '/')
    if (Test-Reparse (Get-Item -LiteralPath $data -Force)) { throw 'LimbusCompany_Data jest linkiem; wskaz rzeczywisty folder.' }
    Write-Host ('Gra: ' + $root)

    $steamapps = Split-Path -Parent (Split-Path -Parent $root)
    $buildId = Get-AcfValue (Join-Path $steamapps ('appmanifest_' + $script:AppId + '.acf')) 'buildid'

    # 1. Spis nazw plikow LimbusCompany_Data (bez tresci).
    $inventory = New-Object System.Text.StringBuilder
    $inventoryRows = 0
    $inventoryLimited = $false
    foreach ($file in (Get-ChildItem -LiteralPath $data -Recurse -File -Force -ErrorAction SilentlyContinue)) {
        if ($inventoryRows -ge $script:MaxInventory) { $inventoryLimited = $true; break }
        $rel = Get-RelativePath $data $file.FullName
        [void] $inventory.Append('{"p": ' + (ConvertTo-JsonString $rel) + ', "s": ' + $file.Length +
            ', "m": "' + $file.LastWriteTimeUtc.ToString('yyyy-MM-ddTHH:mm:ssZ') + '"}' + "`n")
        $inventoryRows++
    }

    # 2. Kandydaci: wszystko pod Localize oraz Lang\config.json.
    $localize = Join-Path $data ($script:LocalizeRelative -replace '/', '\')
    $localizeExists = Test-Path -LiteralPath $localize -PathType Container
    if (-not $localizeExists) { Add-Problem $script:LocalizeRelative 'brak_folderu_localize' }
    $candidates = New-Object 'System.Collections.Generic.List[object]'
    $languages = New-Object 'System.Collections.Generic.List[string]'
    if ($localizeExists) {
        foreach ($dir in (Get-ChildItem -LiteralPath $localize -Directory -Force)) { [void] $languages.Add($dir.Name) }
        foreach ($file in (Get-ChildItem -LiteralPath $localize -Recurse -File -Force)) {
            $rel = Get-RelativePath $data $file.FullName
            if (Test-Reparse $file) { Add-Skipped $rel 'link' $file.Length; continue }
            if ($script:AllowedSuffixes -notcontains $file.Extension.ToLowerInvariant()) { Add-Skipped $rel 'typ' $file.Length; continue }
            if ($file.Length -gt $script:MaxSingleFile) { Add-Skipped $rel 'limit' $file.Length; continue }
            [void] $candidates.Add($file)
        }
    }
    $langDir = Join-Path $data 'Lang'
    $langFolders = @()
    $langConfig = $false
    if (Test-Path -LiteralPath $langDir -PathType Container) {
        $langFolders = @(Get-ChildItem -LiteralPath $langDir -Directory -Force | ForEach-Object { $_.Name })
        $configFile = Get-Item -LiteralPath (Join-Path $langDir 'config.json') -Force -ErrorAction SilentlyContinue
        if ($null -ne $configFile -and $configFile.Length -le 65536) { [void] $candidates.Add($configFile); $langConfig = $true }
    }

    # 3. Sumy i wybor (tryb aktualizacji wysyla tylko nowe i zmienione pliki).
    $stateFile = Get-StateFile
    $useState = (-not $BezStanu) -and ($Tryb -eq 'aktualizacja')
    $previous = @{}
    if ($useState) { $previous = Read-State $stateFile }
    $current = @{}
    $selected = New-Object 'System.Collections.Generic.List[object]'
    $unchanged = 0
    foreach ($file in $candidates) {
        $rel = Get-RelativePath $data $file.FullName
        try { $bytes = [IO.File]::ReadAllBytes($file.FullName) } catch { Add-Problem $rel 'blad_odczytu'; continue }
        $hash = Get-Sha256Hex $bytes
        $current[$rel] = $hash
        if ($useState -and $previous.ContainsKey($rel) -and $previous[$rel] -eq $hash) { $unchanged++; continue }
        [void] $selected.Add([ordered]@{ plik = $file; sciezka = $rel; rozmiar = [long] $bytes.Length; sha256 = $hash })
    }
    $removed = @()
    if ($useState) { $removed = @($previous.Keys | Where-Object { -not $current.ContainsKey($_) } | Sort-Object) }

    if ($useState -and $selected.Count -eq 0 -and $removed.Count -eq 0 -and $script:Problems.Count -eq 0) {
        Write-Host 'Od ostatniego wyslania nic sie nie zmienilo. Nie tworze ZIP-a.'
        return 0
    }

    # 4. Podzial na czesci wedlug rozmiaru przed kompresja.
    $parts = New-Object 'System.Collections.Generic.List[object]'
    $currentPart = New-Object 'System.Collections.Generic.List[object]'
    $currentBytes = [long] 0
    foreach ($item in $selected) {
        if ($currentPart.Count -gt 0 -and ($currentBytes + $item.rozmiar) -gt $LimitCzesciBajtow) {
            [void] $parts.Add($currentPart)
            $currentPart = New-Object 'System.Collections.Generic.List[object]'
            $currentBytes = 0
        }
        [void] $currentPart.Add($item)
        $currentBytes += $item.rozmiar
    }
    [void] $parts.Add($currentPart)

    $outDir = Get-OutputDirectory
    $stamp = [DateTime]::Now.ToString('yyyyMMdd-HHmmss')
    $id = -join ((1..8) | ForEach-Object { '{0:x}' -f (Get-Random -Maximum 16) })
    $summary = @()
    for ($p = 0; $p -lt $parts.Count; $p++) {
        $bytesInPart = [long] 0
        foreach ($item in $parts[$p]) { $bytesInPart += $item.rozmiar }
        $summary += ,([ordered]@{ czesc = $p + 1; plikow = $parts[$p].Count; bajtow = $bytesInPart })
    }

    $written = New-Object 'System.Collections.Generic.List[string]'
    for ($p = 0; $p -lt $parts.Count; $p++) {
        $suffix = ''
        if ($parts.Count -gt 1) { $suffix = '_czesc' + ($p + 1) }
        $name = 'LC_DANE_' + $stamp + '_' + $id + $suffix + '.zip'
        $target = Join-Path $outDir $name
        $temp = $target + '.partial'
        $records = New-Object 'System.Collections.Generic.List[object]'
        $fs = [IO.File]::Open($temp, [IO.FileMode]::CreateNew)
        try {
            $zip = New-Object System.IO.Compression.ZipArchive($fs, [System.IO.Compression.ZipArchiveMode]::Create, $false)
            try {
                foreach ($item in $parts[$p]) {
                    $bytes = [IO.File]::ReadAllBytes($item.plik.FullName)
                    $hash = Get-Sha256Hex $bytes
                    if ($hash -ne $item.sha256) {
                        Add-Problem $item.sciezka 'zmieniony_w_trakcie'
                        $current[$item.sciezka] = $hash
                    }
                    $member = 'pliki/' + $item.sciezka
                    Add-ZipEntry $zip $member $bytes
                    [void] $records.Add([ordered]@{ sciezka = $item.sciezka; czlon = $member; rozmiar = [long] $bytes.Length; sha256 = $hash })
                }
                if ($p -eq 0) { Add-ZipEntry $zip 'INWENTARZ.jsonl' ($script:Utf8.GetBytes($inventory.ToString())) }
                $complete = ($script:Problems.Count -eq 0)
                $state = 'niepelny'
                if ($complete) { $state = 'kompletny' }
                $report = [ordered]@{
                    format = 'lc-zbior-v1'
                    zbieracz = $script:Version
                    tryb = $Tryb
                    zbior_id = $id
                    utworzono_utc = [DateTime]::UtcNow.ToString('o')
                    czesc = $p + 1
                    czesci = $parts.Count
                    gra = [ordered]@{ appid = $script:AppId; buildid = $buildId; folder_gry = (Split-Path -Leaf $root) }
                    localize = [ordered]@{ istnieje = $localizeExists; jezyki = @($languages | Sort-Object) }
                    lang = [ordered]@{ istnieje = (Test-Path -LiteralPath $langDir -PathType Container); podfoldery = @($langFolders); config_json = $langConfig }
                    stan = [ordered]@{ uzyty = $useState; plikow_w_stanie = $previous.Count; niezmienione = $unchanged; usuniete = @($removed) }
                    inwentarz = [ordered]@{ w_tej_czesci = ($p -eq 0); wierszy = $inventoryRows; ograniczony = $inventoryLimited }
                    wszystkie_czesci = @($summary)
                    pliki = @($records)
                    pominiete = @($script:Skipped)
                    problemy = @($script:Problems)
                    stan_zbioru = $state
                }
                $json = ConvertTo-Json -InputObject $report -Depth 8
                Add-ZipEntry $zip 'RAPORT.json' ($script:Utf8.GetBytes($json + "`n"))
                $txt = @(
                    ('Zbieracz: ' + $script:Version),
                    ('Tryb: ' + $Tryb + ', czesc ' + ($p + 1) + ' z ' + $parts.Count + ', zbior ' + $id),
                    ('Steam buildid: ' + $buildId),
                    ('Jezyki w Localize: ' + (($languages | Sort-Object) -join ', ')),
                    ('Plikow w tej czesci: ' + $records.Count),
                    ('Niezmienione (pominiete dzieki stanowi): ' + $unchanged),
                    ('Usuniete od ostatniego razu: ' + $removed.Count),
                    ('Pominiete (typ/limit/link): ' + $script:Skipped.Count),
                    ('Problemy: ' + $script:Problems.Count),
                    ('Stan: ' + $state)
                ) -join "`r`n"
                Add-ZipEntry $zip 'RAPORT.txt' ($script:Utf8.GetBytes($txt + "`r`n"))
            } finally { $zip.Dispose() }
        } finally { $fs.Dispose() }
        Move-Item -LiteralPath $temp -Destination $target
        [void] $written.Add($target)
    }

    if (-not $BezStanu) { Write-State $stateFile $current $buildId }

    Write-Host ''
    foreach ($path in $written) {
        $info = Get-Item -LiteralPath $path
        $hash = Get-Sha256Hex ([IO.File]::ReadAllBytes($path))
        Write-Host ('ZIP: ' + $info.FullName)
        Write-Host ('     rozmiar: ' + $info.Length + ' B, SHA-256: ' + $hash)
        if ($info.Length -gt 99614720) { Write-Host '     UWAGA: ponad 95 MiB - napisz o tym przed wyslaniem.' }
    }
    if ($script:Problems.Count -gt 0) {
        Write-Host ('UWAGA: zbieranie niepelne, problemow: ' + $script:Problems.Count + ' (szczegoly w RAPORT.json).')
        return 2
    }
    return 0
}

try {
    # Ostatnia wartosc to kod wyjscia; ewentualne inne wyjscie potoku jest ignorowane.
    $result = @(Main)
    exit ([int] $result[-1])
} catch {
    Write-Host ('BLAD: ' + $_.Exception.Message)
    exit 1
}
