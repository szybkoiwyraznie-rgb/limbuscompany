# -*- coding: utf-8 -*-
# P59 Dary E.G.O cz. 4e
def F(seq, pl): return (seq, pl)
PART = [
F(110, "— opis skrócony] Nakłada Spadek Poziomu Obrony"),
F(111, "— opis skrócony] Nakłada Wzrost Poziomu Ataku"),
F(116, "— opis skrócony] Nakłada Refluks"),
F(118, "— nazwa] Cięcie Anioła"),
F(119, "— opis] Na koniec tury, jeżeli sojusznik przekroczył 20 Mocy Oddechu, zużywa 1 Moc Oddechu, by zwiększyć Liczniki Oddechu o 1"),
F(120, "— opis skrócony] Zużywa 1 Moc Oddechu, by zwiększyć Liczniki Oddechu o 1"),
F(121, "— nazwa] Trunek z Beczki"),
F(122, "— opis] Na początku tury, jeżeli co najmniej 5 Tożsamości ma Umiejętności ataku nakładające lub zyskujące Moc [Breath] lub Liczniki [Breath], Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; z pominięciem jednostek zapasowych)\n\nNa koniec tury, jeżeli sojusznik przekroczył 20 Mocy [Breath], zużywa 1 Moc [Breath], by zwiększyć Liczniki [Breath] o 1\n\nNa koniec tury nakłada 2 [Agility], 1 [AttackUp] i 1 [AttackDmgUp] na następną turę 1 sojusznikowi z najwyższą Mocą [Breath] i 1 sojusznikowi z najwyższymi Licznikami [Breath] (może się nakładać na tę samą Tożsamość)\n\nZa każde zyskanie Mocy [Breath] efektem Umiejętności ta Tożsamość zyskuje 2 Moc [Breath] i 2 Liczniki [Breath]. Jeżeli suma posiadanej Mocy [Breath] i Liczników [Breath] jest niższa niż 20, zamiast tego zyskuje 3 Moc [Breath] i 3 Liczniki [Breath].\n\nNa koniec walki, jeżeli Moc [Breath] przekracza 40, zużywa 15 Mocy [Breath], by [Discard] 1 Umiejętność o najniższej Randze ze swoich slotów Umiejętności (1 raz na turę na Postać)"),
F(123, "— opis skrócony] Zyskuje Liczniki Oddechu"),
F(124, "— opis skrócony] Nakłada 2 Pośpiech, 1 Wzrost Poziomu Ataku i 1 Wzrost Obrażeń"),
F(125, "— opis skrócony] Za każde zyskanie Mocy Oddechu efektem Umiejętności zyskuje dodatkowo Moc i Liczniki"),
F(126, "— opis skrócony] Odrzuca Umiejętność o najniższej Randze ze slotów Umiejętności"),
F(127, "— nazwa] Miniatura Telepole"),
F(128, "— opis] Na koniec ataku Umiejętnością zużywającą co najmniej 7 własnych Liczników [Charge], jeżeli cel ginie, zwiększa własne Liczniki [Charge] o (zużyte przez tę Umiejętność Liczniki [Charge]/4) (wliczając Szczególne Ładowanie)"),
F(129, "— opis skrócony] Zwiększa własne Liczniki [Charge] proporcjonalnie do zużytych Liczników [Charge]"),
F(130, "— nazwa] Izolator"),
F(131, "— opis] Na początku tury, jeżeli co najmniej 5 Tożsamości ma Umiejętności ataku zyskujące Licznik [Charge] lub Szczególne Ładowanie, Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; z pominięciem jednostek zapasowych)\n\nNa koniec ataku Umiejętnością zużywającą własne Liczniki [Charge], jeżeli cel ginie, zwiększa własne Liczniki [Charge] o (zużyte przez tę Umiejętność Liczniki [Charge]/3)\n\nNa początku tury przy Licznikach [Charge] niższych niż 3, zyskuje +3 Liczniki [Charge]. Na początku tury przy Licznikach Ładowania co najmniej 3, zyskuje 1 [AttackDmgUp]."),
F(133, "— opis skrócony] Zyskuje Liczniki [Charge] lub 1 [AttackDmgUp] zależnie od Liczników [Charge]"),
F(134, "— nazwa] Silnik Wieczny Typu T-5"),
F(135, "— opis] Na początku tury, jeżeli co najmniej 5 Tożsamości ma Umiejętności ataku zyskujące Licznik [Charge] lub Szczególne Ładowanie, Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; z pominięciem jednostek zapasowych)\n\nNa początku tury przy Licznikach [Charge] niższych niż 3, zyskuje +5 Liczniki [Charge]. Na początku tury przy Licznikach Ładowania co najmniej 5, zyskuje minimalną i maksymalną Szybkość +2, 1 [Enhancement] i 2 [AttackDmgUp] (wliczając Szczególne Ładowanie).\n\nWszyscy sojusznicy na polu zyskują [ShareCharge] na początku tury.\n\nNa koniec ataku Umiejętnością 3 zużywającą lub zyskującą Liczniki [Charge], jeżeli cel ginie lub Liczniki [Charge] wynoszą co najmniej 3, dodaje 1 Umiejętność 3 do listy Umiejętności na następną turę (1 wywołanie na turę na sojusznika; wliczając Szczególne Ładowanie)"),
F(137, "— opis skrócony] Zwiększa Liczniki [Charge] proporcjonalnie do zużytych; na następną turę zyskuje [PlusCoinValueUp]"),
F(138, "— opis skrócony] Na koniec ataku Umiejętnością 3 zużywającą [Charge] dodaje 1 Umiejętność 3 do listy Umiejętności"),
]
