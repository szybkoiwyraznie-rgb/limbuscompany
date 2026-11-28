# -*- coding: utf-8 -*-
# P59 Dary E.G.O cz. 4f
def F(seq, pl): return (seq, pl)
PART = [
F(139, "— nazwa] Pewna Filozofia"),
F(140, "— opis] Prognoza prawdopodobieństwa syntezy Darów zawsze wynosi 100%"),
F(141, "— nazwa] Bogactwo"),
F(142, "— opis] Koszt zakupu i ulepszania wszystkich Darów E.G.O jest ustalony na 1.\n\nWszyscy sojusznicy zyskują 1 [AttackUp] za każde 500 Kosztu (maks. 20)"),
F(144, "— nazwa] Bolus Wytrwałości"),
F(145, "— opis] Na początku tury 1 sojusznik z najwyższym Maks. HP zyskuje [DefenseUp] w liczbie równej liczbie otrzymanych obrażeń od Umiejętności ataku wrogów w tej walce (maks. 6)."),
F(147, "— nazwa] Topór Piorunowy"),
F(148, "— opis] Przy trafieniu Umiejętnością zużywającą Liczniki [Charge], nakłada 1 [Burst] (3 wywołania na Umiejętność; wliczając Szczególne Ładowanie)\n\nEfekty tego Daru są wzmocnione w zależności od liczby Tożsamości w zespole z Umiejętnościami ataku nakładającymi [Burst] lub zyskującymi [Charge] (poza Umiejętnościami E.G.O; wlicza wszystkie jednostki zespołu).\n\n- Przy co najmniej 6 Tożsamościach\nPrzy zadaniu obrażeń [Burst] wrogowi, zwiększa Liczniki [Charge] o 1 (3 razy na Umiejętność)\n\n- Przy co najmniej 8 Tożsamościach\nPrzy trafieniu Umiejętnością zużywającą Liczniki [Charge], zwiększa Liczniki [Burst] o 1 (3 razy na Umiejętność; wliczając Szczególne Ładowanie)"),
F(149, "— opis skrócony] Nakłada 1 Rozdarcie"),
F(150, "— opis skrócony] Zwiększa Liczniki Ładowania o 1"),
F(151, "— opis skrócony] Zwiększa Liczniki Rozdarcia o 1"),
F(152, "— nazwa] Kwiat w Lustrze"),
F(153, "— opis] Przy każdym początku tury nakłada 3 Moc [Burst] na wszystkich wrogach i zwiększa Liczniki [Burst] o 1 (walki Skupione — wszystkie Partie).\n\nEfekty Daru są wzmocnione w zależności od liczby Tożsamości w zespole z Umiejętnościami ataku nakładającymi lub zyskującymi [Burst] lub [Breath] (poza Umiejętnościami E.G.O; wlicza cały zespół).\n\n- Przy co najmniej 6 Tożsamościach\nPrzy trafieniu z obrażeniami [Burst], zyskuje 1 Licznik [Breath] (3 razy na Umiejętność)\n\n- Przy co najmniej 10 Tożsamościach\nPrzy Trafieniu Krytycznym Umiejętnością, zwiększa Liczniki [Burst] o 1 (3 razy na Umiejętność)"),
F(154, "— opis skrócony] Nakłada 3 Moc Rozdarcia i zwiększa Liczniki Rozdarcia o 1"),
F(155, "— opis skrócony] Zyskuje 1 Licznik Oddechu"),
F(157, "— nazwa] Księżyc na Wodzie"),
F(158, "— opis] Przy trafieniu atakiem wroga z nałożoną Mocą [Burst] co najmniej 5, zyskuje 1 Moc [Breath] i zwiększa własne Liczniki [Breath] o 1 (maks. 3 razy na Umiejętność).\n\nEfekty tego Daru są wzmocnione w zależności od liczby Tożsamości w zespole z Umiejętnościami ataku nakładającymi lub zyskującymi [Burst] lub [Breath] (poza Umiejętnościami E.G.O; wlicza wszystkie jednostki zespołu).\n\nPrzy trafieniu Umiejętnością, jeżeli [Burst] celu wynosi co najmniej 20, Obrażenia Krytyczne +10% (Obrażenia Krytyczne dodatkowo +3% na każdą Tożsamość w zespole)\n\n- Przy co najmniej 12 Tożsamościach\nPrzy trafieniu Umiejętnością, jeżeli wystąpiło Trafienie Krytyczne, usuwa 1 losowy ujemny efekt z odwracalnych nałożonych na siebie (1 raz na turę na Tożsamość)"),
F(159, "— opis skrócony] Zyskuje Moc Oddechu i Liczniki Oddechu"),
F(161, "— opis skrócony] Usuwa 1 losowy ujemny efekt"),
F(162, "— nazwa] Kropla"),
F(163, "— opis] Na początku tury, jeżeli co najmniej 3 Tożsamości ma Umiejętności zużywające [BloodDinner], Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; z pominięciem jednostek zapasowych)\n\nNa początku walki, jeżeli [Laceration] celu atakowanego przez Tożsamość zużywającą [BloodDinner] wynosi co najmniej 30, zmniejsza Moc [Laceration] celu do 15 i generuje [BloodDinner] równy zredukowanej Mocy [Laceration] (1 wywołanie na turę na wszystkich wrogów; w przypadku Umiejętności obszarowych stosowane tylko do głównego celu).\n\nZa każde 10 [BloodDinner] wygenerowanych tym efektem nakłada na Tożsamości z Umiejętnościami zużywającymi [BloodDinner] 1 Wzrost Mocy i 1 Wzrost Obrażeń na następną turę (maks. 4)"),
F(164, "— opis skrócony] Zmniejsza Moc Krwawienia i zwiększa Krwawą Ucztę"),
]
