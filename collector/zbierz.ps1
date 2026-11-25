# LCB_ZBIERZ_DANE 1.0.0 - Windows PowerShell 5.1; odczyt gry, zapis tylko poza nia.
# Zbiera teksty lokalizacji Limbus Company (Localize/en, kr, jp), stan folderu
# Lang i inwentarz nazw plikow. Nie zmienia gry, nie wysyla niczego przez siec.
[CmdletBinding()]
param(
    [Parameter(Position = 0)] [string] $GameRoot = '',
    [string] $OutputDirectory = '',
    [string] $SteamRoot = '',
    [string[]] $Jezyki = @('en', 'kr', 'jp'),
    [long] $PayloadLimitBytes = 943718400,
    [long] $ArchiveWarnBytes = 99614720,
    [switch] $NonInteractive
)

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
$script:ToolVersion = '1.0.0'
$script:Format = 'lcb-zbieracz-v1'
$script:SteamAppId = '1973530'
$script:MaxInventory = 250000
$script:Utf8 = New-Object System.Text.UTF8Encoding($false)
$script:Problems = New-Object 'System.Collections.Generic.List[object]'
$script:Files = New-Object 'System.Collections.Generic.List[object]'
$script:Skipped = New-Object 'System.Collections.Generic.List[object]'
$script:InventoryCount = 0
$script:InventoryLimited = $false
$script:PayloadBytes = [long] 0

function Add-Problem([string] $Path, [string] $Reason) {
    [void] $script:Problems.Add([ordered]@{ path = $Path; reason = $Reason })
}

function Json-Escape([string] $Text) {
    $sb = New-Object System.Text.StringBuilder
    foreach ($ch in $Text.ToCharArray()) {
        $code = [int] $ch
        if ($ch -eq '"') { [void] $sb.Append('\"') }
        elseif ($ch -eq '\') { [void] $sb.Append('\\') }
        elseif ($code -lt 32) { [void] $sb.Append(('\u{0:x4}' -f $code)) }
        else { [void] $sb.Append($ch) }
    }
    return $sb.ToString()
}

function Is-Reparse($Item) {
    return (($Item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0)
}

function Assert-NoReparseAncestors([string] $Path) {
    $item = Get-Item -LiteralPath $Path -Force -ErrorAction Stop
    while ($null -ne $item) {
        if (Is-Reparse $item) {
            throw 'Folder gry lub jego folder nadrzedny jest linkiem (reparse point). Wskaz rzeczywisty folder.'
        }
        $item = $item.Parent
    }
}

function Normalize-GameRoot([string] $Path) {
    # Akceptuje glowny folder gry, LimbusCompany_Data albo dowolny folder wewnatrz niego.
    if ([string]::IsNullOrWhiteSpace($Path)) { return '' }
    $Path = $Path.Trim().Trim('"')
    try { $item = Get-Item -LiteralPath $Path -Force -ErrorAction Stop } catch { return '' }
    if (-not $item.PSIsContainer) { $item = $item.Directory }
    while ($null -ne $item) {
        if ($item.Name -ieq 'LimbusCompany_Data') { return $item.Parent.FullName }
        if (Test-Path -LiteralPath (Join-Path $item.FullName 'LimbusCompany_Data') -PathType Container) {
            return $item.FullName
        }
        $item = $item.Parent
    }
    return ''
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

function Find-SteamCandidates([string] $Override) {
    $steamDirs = New-Object 'System.Collections.Generic.List[string]'
    if (-not [string]::IsNullOrWhiteSpace($Override)) {
        [void] $steamDirs.Add($Override)
    } else {
        foreach ($registry in @('HKCU:\Software\Valve\Steam', 'HKLM:\SOFTWARE\WOW6432Node\Valve\Steam')) {
            try {
                $props = Get-ItemProperty -LiteralPath $registry -ErrorAction Stop
                foreach ($value in @($props.SteamPath, $props.InstallPath)) {
                    if ($value -and -not $steamDirs.Contains([string] $value)) { [void] $steamDirs.Add([string] $value) }
                }
            } catch { }
        }
        foreach ($base in @(${env:ProgramFiles(x86)}, $env:ProgramFiles)) {
            if ($base) {
                $value = Join-Path $base 'Steam'
                if (-not $steamDirs.Contains($value)) { [void] $steamDirs.Add($value) }
            }
        }
    }
    $libraries = New-Object 'System.Collections.Generic.List[string]'
    foreach ($dir in $steamDirs) {
        if (-not $libraries.Contains($dir)) { [void] $libraries.Add($dir) }
        $vdf = Join-Path $dir 'steamapps\libraryfolders.vdf'
        try {
            if (Test-Path -LiteralPath $vdf -PathType Leaf) {
                $text = [IO.File]::ReadAllText($vdf)
                $found = [regex]::Matches($text, '(?im)^\s*"(?:path|[0-9]+)"\s*"([^"\r\n]+)"\s*$')
                foreach ($m in $found) {
                    $library = $m.Groups[1].Value.Replace('\\', '\')
                    if ([IO.Path]::IsPathRooted($library) -and -not $libraries.Contains($library)) {
                        [void] $libraries.Add($library)
                    }
                }
            }
        } catch { }
    }
    $result = New-Object 'System.Collections.Generic.List[string]'
    foreach ($library in $libraries) {
        $apps = Join-Path $library 'steamapps'
        $acf = Join-Path $apps ('appmanifest_' + $script:SteamAppId + '.acf')
        $names = New-Object 'System.Collections.Generic.List[string]'
        $installDir = Get-AcfValue $acf 'installdir'
        if ($installDir -and $installDir -notmatch '[:/\\]' -and $installDir -notin @('.', '..')) { [void] $names.Add($installDir) }
        if (-not $names.Contains('Limbus Company')) { [void] $names.Add('Limbus Company') }
        foreach ($name in $names) {
            $path = Join-Path (Join-Path $apps 'common') $name
            $root = Normalize-GameRoot $path
            if ($root -and -not $result.Contains($root)) { [void] $result.Add($root) }
        }
    }
    return $result.ToArray()
}

function Choose-GameRoot {
    if (-not [string]::IsNullOrWhiteSpace($GameRoot)) {
        $root = Normalize-GameRoot $GameRoot
        if (-not $root) { throw 'Wskazany folder nie zawiera LimbusCompany_Data. Wskaz glowny folder gry.' }
        return $root
    }
    $found = @(Find-SteamCandidates $SteamRoot)
    if ($found.Count -eq 1) { return $found[0] }
    if ($found.Count -gt 1) {
        if ($NonInteractive) { throw 'Znaleziono kilka instalacji. Wskaz folder gry parametrem.' }
        Write-Host 'Znaleziono kilka instalacji. Wybierz numer:'
        for ($i = 0; $i -lt $found.Count; $i++) { Write-Host ('{0}. {1}' -f ($i + 1), $found[$i]) }
        $choice = Read-Host 'Numer'
        $number = 0
        if ([int]::TryParse($choice, [ref] $number) -and $number -ge 1 -and $number -le $found.Count) {
            return $found[$number - 1]
        }
        throw 'Nie wybrano instalacji.'
    }
    if ($NonInteractive) { throw 'Nie znaleziono gry w bibliotekach Steam.' }
    Write-Host 'Nie znaleziono gry automatycznie. Wybierz glowny folder Limbus Company (z folderem LimbusCompany_Data).'
    $picked = ''
    try {
        Add-Type -AssemblyName System.Windows.Forms
        $dialog = New-Object System.Windows.Forms.FolderBrowserDialog
        $dialog.Description = 'Wybierz glowny folder Limbus Company'
        $dialog.ShowNewFolderButton = $false
        if ($dialog.ShowDialog() -eq [System.Windows.Forms.DialogResult]::OK) { $picked = $dialog.SelectedPath }
    } catch { Write-Host 'Nie mozna otworzyc okna wyboru folderu.' }
    if (-not $picked) { $picked = Read-Host 'Wpisz pelna sciezke do folderu gry albo nacisnij Enter, aby przerwac' }
    $root = Normalize-GameRoot $picked
    if (-not $root) { throw 'Wskazany folder nie zawiera LimbusCompany_Data.' }
    return $root
}

function Read-SteamInfo([string] $Root) {
    $info = [ordered]@{ app_id = $script:SteamAppId; buildid = ''; last_updated = ''; manifest_found = $false }
    try {
        $common = (Get-Item -LiteralPath $Root -Force).Parent
        if ($null -ne $common -and $common.Name -ieq 'common' -and $null -ne $common.Parent -and $common.Parent.Name -ieq 'steamapps') {
            $acf = Join-Path $common.Parent.FullName ('appmanifest_' + $script:SteamAppId + '.acf')
            if (Test-Path -LiteralPath $acf -PathType Leaf) {
                $info.manifest_found = $true
                $build = Get-AcfValue $acf 'buildid'
                if ($build -match '^\d+$') { $info.buildid = $build }
                $updated = Get-AcfValue $acf 'LastUpdated'
                if ($updated -match '^\d+$') {
                    $info.last_updated = [DateTimeOffset]::FromUnixTimeSeconds([long] $updated).UtcDateTime.ToString('yyyy-MM-ddTHH:mm:ssZ')
                }
            }
        }
    } catch { Add-Problem 'steamapps' 'steam_manifest_unreadable' }
    return $info
}

function Relative-To([string] $Base, [string] $Path) {
    $prefix = $Base.TrimEnd('\') + '\'
    if (-not $Path.StartsWith($prefix, [StringComparison]::OrdinalIgnoreCase)) { throw 'Sciezka poza oczekiwanym folderem.' }
    return $Path.Substring($prefix.Length).Replace('\', '/')
}

function Get-Sha256([string] $Path) {
    return (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash.ToLowerInvariant()
}

function Copy-Verified([string] $Source, [string] $ArchiveName, [string] $Kind) {
    # Kopia z kontrola: SHA-256 zrodla przed i kopii po skopiowaniu musza byc rowne.
    $item = Get-Item -LiteralPath $Source -Force
    $size = [long] $item.Length
    if ($script:PayloadBytes + $size -gt $PayloadLimitBytes) {
        [void] $script:Skipped.Add([ordered]@{ path = $ArchiveName; reason = 'skipped_limit'; size = $size })
        return
    }
    $before = Get-Sha256 $Source
    $target = Join-Path $script:Work ($ArchiveName.Replace('/', '\'))
    $parent = [IO.Path]::GetDirectoryName($target)
    [void] [IO.Directory]::CreateDirectory($parent)
    [IO.File]::Copy($Source, $target, $false)
    $after = Get-Sha256 $target
    if ($before -ne $after) {
        Remove-Item -LiteralPath $target -Force
        Add-Problem $ArchiveName 'changed_during_copy'
        return
    }
    $script:PayloadBytes += $size
    [void] $script:Files.Add([ordered]@{
        path = $ArchiveName; kind = $Kind; size = $size; sha256 = $after
        mtime_utc = $item.LastWriteTimeUtc.ToString('yyyy-MM-ddTHH:mm:ssZ')
    })
}

function Walk-Files([string] $Top) {
    # Rekurencyjna lista plikow bez wchodzenia w linki/reparse points.
    $out = New-Object 'System.Collections.Generic.List[object]'
    $pending = New-Object System.Collections.Stack
    $pending.Push((Get-Item -LiteralPath $Top -Force))
    while ($pending.Count -gt 0) {
        $dir = $pending.Pop()
        try { $children = @($dir.EnumerateFileSystemInfos()) }
        catch { Add-Problem (Relative-To $script:Root $dir.FullName) 'directory_unreadable'; continue }
        foreach ($child in ($children | Sort-Object Name)) {
            if (Is-Reparse $child) { Add-Problem (Relative-To $script:Root $child.FullName) 'reparse_skipped'; continue }
            if ($child -is [IO.DirectoryInfo]) { $pending.Push($child) } else { [void] $out.Add($child) }
        }
    }
    return $out
}

function Collect-Localize {
    $localize = Join-Path $script:Root 'LimbusCompany_Data\Assets\Resources_moved\Localize'
    $report = [ordered]@{ found = $false; directories = @(); languages = @() }
    if (-not (Test-Path -LiteralPath $localize -PathType Container)) {
        Add-Problem 'LimbusCompany_Data/Assets/Resources_moved/Localize' 'localize_not_found'
        return $report
    }
    $report.found = $true
    $dirs = New-Object 'System.Collections.Generic.List[object]'
    foreach ($d in @(Get-ChildItem -LiteralPath $localize -Force -Directory | Sort-Object Name)) {
        if (Is-Reparse $d) { Add-Problem ('Localize/' + $d.Name) 'reparse_skipped'; continue }
        $files = @(Walk-Files $d.FullName)
        $bytes = [long] 0
        foreach ($f in $files) { $bytes += [long] $f.Length }
        [void] $dirs.Add([ordered]@{ name = $d.Name; files = $files.Count; bytes = $bytes })
    }
    $report.directories = @($dirs.ToArray())
    $languages = New-Object 'System.Collections.Generic.List[object]'
    foreach ($lang in $Jezyki) {
        $entry = [ordered]@{ lang = $lang; found = $false; files = 0; copied = 0; not_copied = 0; bytes = [long] 0 }
        $match = @(Get-ChildItem -LiteralPath $localize -Force -Directory | Where-Object { $_.Name -ieq $lang })
        if ($match.Count -ne 1 -or (Is-Reparse $match[0])) {
            Add-Problem ('Localize/' + $lang) 'language_not_found'
            [void] $languages.Add($entry)
            continue
        }
        $entry.found = $true
        foreach ($file in (Walk-Files $match[0].FullName)) {
            $entry.files += 1
            $entry.bytes += [long] $file.Length
            $relative = 'Localize/' + (Relative-To $localize $file.FullName)
            if ($file.Extension -ine '.json') {
                [void] $script:Skipped.Add([ordered]@{ path = $relative; reason = 'not_json'; size = [long] $file.Length })
                $entry.not_copied += 1
                continue
            }
            $countBefore = $script:Files.Count
            Copy-Verified $file.FullName $relative 'localize'
            if ($script:Files.Count -gt $countBefore) { $entry.copied += 1 } else { $entry.not_copied += 1 }
        }
        [void] $languages.Add($entry)
    }
    $report.languages = @($languages.ToArray())
    return $report
}

function Collect-Lang {
    $lang = Join-Path $script:Root 'LimbusCompany_Data\Lang'
    $report = [ordered]@{ found = $false; config_copied = $false; folders = @(); other_files = @() }
    if (-not (Test-Path -LiteralPath $lang -PathType Container)) { return $report }
    $report.found = $true
    $folders = New-Object 'System.Collections.Generic.List[object]'
    $others = New-Object 'System.Collections.Generic.List[object]'
    foreach ($child in @(Get-ChildItem -LiteralPath $lang -Force | Sort-Object Name)) {
        if (Is-Reparse $child) { Add-Problem ('Lang/' + $child.Name) 'reparse_skipped'; continue }
        if ($child.PSIsContainer) {
            $files = @(Walk-Files $child.FullName)
            $bytes = [long] 0
            foreach ($f in $files) { $bytes += [long] $f.Length }
            [void] $folders.Add([ordered]@{ name = $child.Name; files = $files.Count; bytes = $bytes })
        } elseif ($child.Name -ieq 'config.json' -and $child.Length -le 65536) {
            Copy-Verified $child.FullName 'Lang/config.json' 'lang_config'
            $report.config_copied = $true
        } else {
            [void] $others.Add([ordered]@{ name = $child.Name; bytes = [long] $child.Length })
        }
    }
    $report.folders = @($folders.ToArray())
    $report.other_files = @($others.ToArray())
    return $report
}

function Write-Inventory([string] $Path) {
    # Nazwy, rozmiary i daty wszystkich plikow pod LimbusCompany_Data (bez tresci i hashy).
    $data = Join-Path $script:Root 'LimbusCompany_Data'
    $writer = New-Object System.IO.StreamWriter($Path, $false, $script:Utf8)
    try {
        $pending = New-Object System.Collections.Stack
        $pending.Push((Get-Item -LiteralPath $data -Force))
        while ($pending.Count -gt 0) {
            $dir = $pending.Pop()
            try { $children = @($dir.EnumerateFileSystemInfos()) }
            catch { Add-Problem (Relative-To $script:Root $dir.FullName) 'directory_unreadable'; continue }
            foreach ($child in ($children | Sort-Object Name)) {
                if (Is-Reparse $child) { continue }
                if ($child -is [IO.DirectoryInfo]) { $pending.Push($child); continue }
                if ($script:InventoryCount -ge $script:MaxInventory) {
                    if (-not $script:InventoryLimited) { Add-Problem 'LimbusCompany_Data' 'inventory_limit_reached' }
                    $script:InventoryLimited = $true
                    $pending.Clear()
                    break
                }
                $rel = Relative-To $script:Root $child.FullName
                $line = '{"p":"' + (Json-Escape $rel) + '","s":' + ([long] $child.Length) + ',"t":"' + $child.LastWriteTimeUtc.ToString('yyyy-MM-ddTHH:mm:ssZ') + '"}'
                $writer.WriteLine($line)
                $script:InventoryCount += 1
            }
        }
    } finally { $writer.Dispose() }
}

function Write-Zip([string] $Source, [string] $Target, [string[]] $Names) {
    Add-Type -AssemblyName System.IO.Compression
    Add-Type -AssemblyName System.IO.Compression.FileSystem
    $stream = [IO.File]::Open($Target, [IO.FileMode]::CreateNew)
    try {
        $zip = New-Object System.IO.Compression.ZipArchive($stream, [IO.Compression.ZipArchiveMode]::Create, $false)
        try {
            foreach ($name in $Names) {
                # Nazwy wpisow zawsze z ukosnikiem '/', niezaleznie od wersji .NET.
                $entry = $zip.CreateEntry($name, [IO.Compression.CompressionLevel]::Optimal)
                $in = [IO.File]::OpenRead((Join-Path $Source ($name.Replace('/', '\'))))
                try {
                    $out = $entry.Open()
                    try { $in.CopyTo($out) } finally { $out.Dispose() }
                } finally { $in.Dispose() }
            }
        } finally { $zip.Dispose() }
    } finally { $stream.Dispose() }
}

$exitCode = 1
$script:Work = ''
# -File przekazuje liste jezykow jako jeden napis; akceptuj tez "en,kr,jp".
$Jezyki = @($Jezyki | ForEach-Object { $_ -split ',' } | ForEach-Object { $_.Trim() } | Where-Object { $_ })
try {
    Write-Host ('LCB_ZBIERZ_DANE {0}' -f $script:ToolVersion)
    $running = @(Get-Process -Name 'LimbusCompany' -ErrorAction SilentlyContinue)
    if ($running.Count -gt 0) { throw 'Gra jest uruchomiona. Zamknij Limbus Company i uruchom zbieracz ponownie.' }

    $script:Root = Choose-GameRoot
    Assert-NoReparseAncestors $script:Root
    Write-Host ('Folder gry: {0}' -f $script:Root)

    if ([string]::IsNullOrWhiteSpace($OutputDirectory)) {
        $OutputDirectory = [Environment]::GetFolderPath('Desktop')
        if ([string]::IsNullOrWhiteSpace($OutputDirectory)) { $OutputDirectory = $env:USERPROFILE }
    }
    if (-not (Test-Path -LiteralPath $OutputDirectory -PathType Container)) { throw 'Folder wynikowy nie istnieje.' }
    $outFull = (Get-Item -LiteralPath $OutputDirectory -Force).FullName.TrimEnd('\')
    $rootFull = $script:Root.TrimEnd('\')
    if ($outFull -ieq $rootFull -or $outFull.StartsWith($rootFull + '\', [StringComparison]::OrdinalIgnoreCase)) {
        throw 'Folder wynikowy jest wewnatrz folderu gry. Wybierz inny (np. Pulpit).'
    }

    $stamp = (Get-Date).ToString('yyyyMMdd_HHmmss')
    $random = ([guid]::NewGuid().ToString('N')).Substring(0, 6)
    $baseName = 'LCB_DANE_' + $stamp + '_' + $random
    $script:Work = Join-Path $outFull ('.LCB_ZBIERANIE_' + $stamp + '_' + $random)
    [void] [IO.Directory]::CreateDirectory($script:Work)

    Write-Host 'Kopiowanie tekstow lokalizacji (Localize)...'
    $localizeReport = Collect-Localize
    Write-Host 'Sprawdzanie folderu Lang...'
    $langReport = Collect-Lang
    $appInfo = Join-Path $script:Root 'LimbusCompany_Data\app.info'
    if ((Test-Path -LiteralPath $appInfo -PathType Leaf) -and (Get-Item -LiteralPath $appInfo -Force).Length -le 4096) {
        Copy-Verified $appInfo 'app.info' 'app_info'
    }
    Write-Host 'Spisywanie nazw plikow (inwentarz)...'
    Write-Inventory (Join-Path $script:Work 'INWENTARZ.jsonl')
    $steam = Read-SteamInfo $script:Root

    $status = 'complete'
    $limitSkips = @($script:Skipped | Where-Object { $_.reason -eq 'skipped_limit' })
    if ($script:Problems.Count -gt 0 -or $limitSkips.Count -gt 0) { $status = 'partial' }
    $report = [ordered]@{
        format = $script:Format
        tool_version = $script:ToolVersion
        created_utc = (Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ')
        status = $status
        game = [ordered]@{ root_name = [IO.Path]::GetFileName($rootFull); steam = $steam }
        languages_requested = @($Jezyki)
        localize = $localizeReport
        lang = $langReport
        inventory = [ordered]@{ file = 'INWENTARZ.jsonl'; entries = $script:InventoryCount; limited = $script:InventoryLimited }
        limits = [ordered]@{ payload_bytes = $PayloadLimitBytes; payload_used = $script:PayloadBytes; inventory_entries = $script:MaxInventory }
        files = @($script:Files.ToArray())
        skipped = @($script:Skipped.ToArray())
        problems = @($script:Problems.ToArray())
    }
    [IO.File]::WriteAllText((Join-Path $script:Work 'RAPORT.json'), ($report | ConvertTo-Json -Depth 8), $script:Utf8)

    $lines = New-Object 'System.Collections.Generic.List[string]'
    [void] $lines.Add('LIMBUS COMPANY - RAPORT ZBIERACZA ' + $script:ToolVersion)
    [void] $lines.Add('Stan: ' + $status)
    [void] $lines.Add('Steam build: ' + $(if ($steam.buildid) { $steam.buildid } else { 'nieznany' }))
    foreach ($l in $localizeReport.languages) {
        [void] $lines.Add(('Jezyk {0}: znaleziono={1}, plikow={2}, skopiowano={3}' -f $l.lang, $l.found, $l.files, $l.copied))
    }
    [void] $lines.Add(('Folder Lang: {0}; podfoldery: {1}' -f $langReport.found, @($langReport.folders).Count))
    [void] $lines.Add(('Inwentarz: {0} plikow' -f $script:InventoryCount))
    [void] $lines.Add(('Problemy: {0}; pominiete: {1}' -f $script:Problems.Count, $script:Skipped.Count))
    foreach ($p in $script:Problems) { [void] $lines.Add(' - ' + $p.reason + ': ' + $p.path) }
    $bomUtf8 = New-Object System.Text.UTF8Encoding($true)
    [IO.File]::WriteAllLines((Join-Path $script:Work 'RAPORT.txt'), $lines.ToArray(), $bomUtf8)

    $names = New-Object 'System.Collections.Generic.List[string]'
    foreach ($n in @('RAPORT.json', 'RAPORT.txt', 'INWENTARZ.jsonl')) { [void] $names.Add($n) }
    foreach ($f in $script:Files) { [void] $names.Add($f.path) }
    $zipPath = Join-Path $outFull ($baseName + '.zip')
    Write-Host 'Tworzenie archiwum ZIP...'
    Write-Zip $script:Work $zipPath $names.ToArray()
    $zipSize = (Get-Item -LiteralPath $zipPath).Length
    $zipSha = Get-Sha256 $zipPath

    Write-Host ''
    Write-Host ('ZIP: {0}' -f $zipPath)
    Write-Host ('Rozmiar: {0} B ({1:N1} MiB)' -f $zipSize, ($zipSize / 1MB))
    Write-Host ('SHA-256: {0}' -f $zipSha)
    Write-Host ('Stan: {0}; plikow w ZIP: {1}' -f $status, $script:Files.Count)
    if ($zipSize -gt $ArchiveWarnBytes) {
        Write-Host 'UWAGA: ZIP ma ponad 95 MiB. Napisz o tym przed wgraniem na Dysk (limit pobierania 100 MiB).'
    }
    if ($status -eq 'complete') { $exitCode = 0 } else { $exitCode = 2 }
} catch {
    Write-Host ('BLAD: {0}' -f $_.Exception.Message)
    $exitCode = 1
} finally {
    if ($script:Work -and (Test-Path -LiteralPath $script:Work)) {
        try { Remove-Item -LiteralPath $script:Work -Recurse -Force } catch { Write-Host 'Nie udalo sie usunac folderu tymczasowego.' }
    }
}
exit $exitCode
