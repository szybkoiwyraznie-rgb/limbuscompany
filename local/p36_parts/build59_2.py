# -*- coding: utf-8 -*-
# P59 Dary E.G.O cz. 4b
def F(seq, pl): return (seq, pl)
PART = [
F(35, "— nazwa] Wymiarowy Modyfikator Percepcji"),
F(36, "— opis] Umiejętności 1 i 2 typu Uderzenia: Poziom Ataku +(liczba monet-1) (maks. 2)\n- Umiejętności z efektem Odrzucenia: zamiast tego Poziom Ataku +(liczba monet) (maks. 4)\n\nGdy jednostka odrzuci własną Umiejętność Umiejętnością Odrzucenia, na początku następnej tury zyskuje 1 Wzrost Obrażeń i Wzrost Poziomu Ataku równy Rangi odrzuconej Umiejętności (1 raz na turę na Tożsamość; liczone wg najwyższej rangi; maks. 3).\n- Jeżeli odrzucono Umiejętność typu Uderzenia, dodatkowo zyskuje 1 Wzrost Obrażeń Uderzenia"),
F(38, "— opis skrócony] Wzrost Obrażeń i Poziomu Ataku. Jeżeli odrzucono Umiejętność Uderzenia, dodatkowo Wzrost Obrażeń Uderzenia"),
F(40, "— opis] Umiejętności podstawowe ataku Uderzenia zyskują Moc Starcia +2. Na początku walki zyskuje [AttackUp] w liczbie równej liczbie Tożsamości używających Umiejętności podstawowych ataku Uderzenia w tej turze (maks. 3).\n\nSojusznicy, których wszystkie Umiejętności podstawowe ataku są typu Uderzenia, zyskują na początku tury 2 [HitDamageUp] (z pominięciem Umiejętności wzmocnionych lub wymagających specjalnych warunków).\n\nPrzy użyciu Umiejętności Kontry (z pominięciem Wzmocnionej Kontry) zyskuje Tarczę równą 7.5% Maks. HP i zadaje +20% obrażeń. Przy otrzymaniu obrażeń podczas używania Umiejętności Kontry nie ulega Oszołomieniu (1 raz na walkę na Tożsamość).\n\nTożsamości frakcji Środkowego zyskują na początku tury 1 [HitResultUp] i 2 [Endurance]. Przy użyciu Umiejętności Kontry przez Tożsamości frakcji Środkowego powyższy efekt wzmocnienia Kontry uruchamia się 2 razy na walkę, a obrażenia Kontry są wzmocnione do +40%."),
F(41, "— opis skrócony] Wzrost Mocy Starcia i Poziomu Ataku"),
F(43, "— opis skrócony] Nie ulega Oszołomieniu od obrażeń przy użyciu Umiejętności Kontry"),
F(44, "— opis skrócony] Wzrost Mocy Uderzenia, Wzrost Mocy Obrony, Wzrost Obrażeń Kontry"),
F(45, "— nazwa] Ognisko 10 000 Lat"),
F(46, "— opis] Na koniec tury wrogowie z co najmniej 3 Licznikami [Combustion] wywołują [Combustion] 1 dodatkowy raz (Liczniki [Combustion] maleją o 1)"),
F(47, "— nazwa] Ukradziony Płomień"),
F(48, "— opis] Na początku tury, jeżeli co najmniej 5 Tożsamości ma Umiejętności ataku nakładające [Combustion] lub Szczególne Podpalenie, Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; z pominięciem jednostek zapasowych)\n\nPrzy trafieniu Umiejętnością (z wliczeniem Umiejętności E.G.O), jeżeli cel ma co najmniej 3 Liczniki [Combustion], wywołuje [Combustion] na celu 1 raz (Liczniki [Combustion] maleją o 1; wywoływane 1 raz na Umiejętność)\n\nNa koniec tury wrogowie z co najmniej 3 Licznikami [Combustion] wywołują [Combustion] 1 dodatkowy raz (Liczniki [Combustion] maleją o 1)\n\nGdy ginie wróg w stanie [Combustion] (w przypadku Anomalii — śmierć korpusu), na początku następnej tury nakłada Moc [Combustion] równą pozostałej Mocy [Combustion] na 1 wroga z najniższą Mocą [Combustion]\n\nNa początku tury nakłada 4 [AttackDown] na wrogów w stanie [Combustion] na czas tej tury\n\nGdy ginie wróg z [Combustion], na początku następnej tury (liczba pozostałej Mocy [Combustion] pokonanego wroga/15) sojuszników z Umiejętnościami nakładającymi [Combustion] zyskuje 2 [AttackDmgUp] (1 wywołanie na turę)"),
F(49, "— opis skrócony] Wywołuje [Combustion] 1 raz"),
F(50, "— opis skrócony] Wywołuje [Combustion] 1 dodatkowy raz"),
F(51, "— opis skrócony] Nakłada Moc [Combustion] równą pozostałej Mocy Podpalenia pokonanego wroga"),
F(52, "— opis skrócony] Nakłada 4 [AttackDown]"),
F(54, "— nazwa] Rozdarty Worek Krwi"),
F(55, "— opis] Przy wygranej Starciu sojusznika wywołuje [Laceration] wroga 1 raz, a Liczniki [Laceration] maleją o 1 (3 razy na turę)"),
F(56, "— opis skrócony] Wywołuje Krwawienie 1 raz (Liczniki Krwawienia maleją o 1)"),
F(57, "— nazwa] Wstrząs Krwotoczny"),
F(58, "— opis] Na początku tury, jeżeli co najmniej 5 Tożsamości ma Umiejętności ataku nakładające [Laceration] lub Szczególne Krwawienie, Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; z pominięciem jednostek zapasowych)\n\nPrzy wygranej Starciu sojusznika wywołuje [Laceration] wroga 1 raz, a Liczniki [Laceration] maleją o 1 (1 raz na turę na sojusznika)\n\nWrogowie mogą ulegać Oszołomieniu od obrażeń [Laceration]; jeżeli wróg ulega Oszołomieniu od obrażeń [Laceration] w trakcie Starcia, wywołuje [Laceration] tyle razy, ile wynosi liczba pozostałych monet wroga, a Liczniki [Laceration] maleją o liczbę wywołań\n\nJeżeli wszyscy wrogowie mają nałożone [Laceration], ich Poziom Obrony maleje o 2. Na koniec tury zyskują (liczba wywołanych [Laceration] x 2) [DefenseDown] na następną turę (maks. 20)\n\nZa każde nałożenie Mocy [Laceration] lub Szczególnego Krwawienia efektem Umiejętności nakłada na cel 3 Moc [Laceration] i 1 Licznik [Laceration]"),
F(59, "— opis skrócony] Przy wygranej Starciu wywołuje Krwawienie wroga 1 raz (Liczniki Krwawienia maleją o 1)"),
F(60, "— opis skrócony] Po zakończeniu Starcia wywołuje Krwawienie wroga tyle razy, ile wynosi liczba pozostałych monet (Liczniki Krwawienia maleją o liczbę wywołań)"),
]
