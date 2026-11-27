# -*- coding: utf-8 -*-
# P59 Dary E.G.O cz. 4h
def F(seq, pl): return (seq, pl)
PART = [
F(194, "— opis skrócony] Zyskuje Moc Końcową"),
F(195, "— nazwa] Deszczowa Chmura"),
F(196, "— opis] Na początku tury, jeżeli suma Mocy [Sinking] i Liczników [Sinking] wszystkich wrogów wynosi co najmniej 30, stosuje poniższe efekty\n\n- Umiejętności nakładające Moc [Sinking] lub Liczniki [Sinking] zyskują Moc Końcową +1 (wliczając Szczególne Zatonięcie; poza Umiejętnościami E.G.O)\n\n- Jeżeli co najmniej 6 Tożsamości ma Umiejętności ataku nakładające Moc [Sinking], Liczniki [Sinking] lub Szczególne Zatonięcie, Umiejętności nakładające Moc [Sinking] lub Liczniki [Sinking] zadają dodatkowo +20% obrażeń (wliczając Szczególne Zatonięcie; poza Umiejętnościami E.G.O; wliczając jednostki zapasowe)\n · Jeżeli Poczytalność atakowanego celu wynosi -45, dodatkowe obrażenia +10%\n\n- Jeżeli co najmniej 10 Tożsamości ma Umiejętności ataku nakładające Moc [Sinking], Liczniki [Sinking] lub Szczególne Zatonięcie, Umiejętności monety Plus nakładające Moc [Sinking] lub Liczniki [Sinking] zyskują dodatkowo Moc Monet +1 (wliczając Szczególne Zatonięcie; poza Umiejętnościami E.G.O; wliczając jednostki zapasowe)\n · Umiejętności monety Minus zamiast Mocy Monet zyskują Moc Bazową +(4/liczba monet) (min. 1, zaokrąglając w dół)"),
F(197, "— opis skrócony] Umiejętności Zatonięcia zyskują Moc Końcową"),
F(198, "— opis skrócony] Umiejętności Zatonięcia zadają więcej obrażeń"),
F(199, "— opis skrócony] Umiejętności Zatonięcia zyskują Moc Monet/Bazową"),
F(200, "— nazwa] Koniec wszelkiego Zła"),
F(201, "— opis] Uruchamia się, gdy w zespole są co najmniej 3 Tożsamości załogi Pequod (wliczając jednostki zapasowe)\n\nPrzy trafieniu Umiejętnością ataku wroga z nałożonym [Laceration] lub Szczególnym Krwawieniem, zwiększa Liczniki [Breath] o 2 lub zyskuje 3 [Breath] (3 razy na turę na Tożsamość)\n\nPrzy trafieniu Umiejętnością z Trafieniem Krytycznym, z 80% szansą zyskuje 1 [PenetrateResultUp] na następną turę (2 razy na turę na Tożsamość; wliczając Umiejętności E.G.O i Kontry)\n- Jeżeli Tożsamość należy do załogi Pequod, dodatkowo zyskuje 1 [PlusCoinValueUp] na następną turę (1 raz na turę na Tożsamość)\n\nPrzy trafieniu Awersu z Trafieniem Krytycznym Umiejętnością podstawową, wartość ujemnych efektów nakładanych tą monetą rośnie o 1 (1 raz na turę na Tożsamość; poza Umiejętnościami E.G.O; wliczając Kontry)\n\nGdy ginie wróg lub sojusznik, przez resztę tej walki Tożsamości załogi Pequod zyskują co turę 1 [PenetrateResultUp], 1 [Protection] i 1 [CriticalDamageUp] (maks. 3 razy na walkę)\n\nJeżeli Tożsamość załogi Pequod trafiła wroga atakiem, Tożsamość załogi Pequod przydzielona najwcześniej w kolejności odzyskuje 7 Poczytalności (1 raz na Umiejętność)\n\nGdy sojusznik pokona wroga, jeżeli Poczytalność Tożsamości załogi Pequod przydzielonej najwcześniej w kolejności jest obniżona, odzyskuje ona 15 Poczytalności"),
F(202, "— opis skrócony] Zyskuje Oddech"),
F(203, "— opis skrócony] Przy Trafieniu Krytycznym z pewną szansą zyskuje [PenetrateResultUp] na następną turę; gdy warunek spełniony, zyskuje [PlusCoinValueUp] i zwiększa wartość ujemnych efektów"),
F(204, "— opis skrócony] Zyskuje [PenetrateResultUp], [Protection] i [CriticalDamageUp]"),
F(206, "— nazwa] Miniatura Kolejki Górskiej"),
F(207, "— opis] Podstawowe Umiejętności wszystkich sojuszników Krwiożerców zyskują Moc Monet +1, a Umiejętności zadają obrażenia <noparse>+([BloodDinner_Accumulation] / 10)%</noparse>\n\nNa koniec tury 2 Tożsamości z najmniej HP spośród sojuszników z [Laceration] odzyskują HP równe 5% własnego Maks. HP i zyskują 10 [SwirlingBloodPersonality] na początku następnej tury\n\nPrzy zabiciu wroga generuje [BloodDinner] w wysokości (Maks. HP korpusu wroga/10) (maks. 50)\n\nNa koniec tury, jeżeli w tej turze zginął sojusznik, wszyscy sojusznicy zyskują 2 [Enhancement] na następną turę\n\nW potyczkach, w których wrogowie mają posiłki: gdy pojawi się nowy wróg, nakłada na niego na początku walki 5 [Laceration] i 3 Licznika [Laceration].\nJeżeli wśród sojuszników jest <Krwiożerca>: gdy pojawia się nowy wróg, wywołuje [Laceration] na wszystkich wrogach 2 razy i zmniejsza Liczniki [Laceration] wszystkich wrogów o 2"),
F(208, "— opis skrócony] Zyskuje Moc Monet podstawowych Umiejętności"),
F(209, "— opis skrócony] Odzyskuje HP i zyskuje [SwirlingBloodPersonality]"),
F(211, "— opis skrócony] Nakłada Moc Krwawienia i Liczniki Krwawienia"),
F(212, "— nazwa] Żarzący się Młot"),
F(213, "— opis] Jeżeli wróg ma [VibrationIgnition], stosuje efekty:\n- Przy trafieniu Umiejętnością podstawową nakłada 1 Moc [Combustion] (maks. 3 razy na Umiejętność)\n- Przy trafieniu Umiejętnością podstawową, jeżeli wróg ma [VibrationIgnition] co najmniej 15, zwiększa Liczniki [Combustion] o 1 (maks. 2 razy na Umiejętność)\n- Za każde 3 [Combustion] Oszołomienie wywołane przez [VibrationExplosion] podnosi Próg +1% (maks. 15%)"),
F(214, "— opis skrócony] Nakłada Podpalenie"),
F(215, "— opis skrócony] Wybuch Wstrząsu dodatkowo podnosi Próg Oszołomienia"),
F(216, "— nazwa] Czerwony Krawat"),
F(217, "— opis] Umiejętności 3 nakładające Moc [Combustion], Liczniki [Combustion] lub Szczególne Podpalenie zyskują Moc Starcia +2 i +30% obrażeń"),
]
