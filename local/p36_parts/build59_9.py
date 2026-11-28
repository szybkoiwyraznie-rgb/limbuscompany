# -*- coding: utf-8 -*-
# P59 Dary E.G.O cz. 4i
def F(seq, pl): return (seq, pl)
PART = [
F(219, "— nazwa] Mundur - Stowarzyszenie Liu"),
F(220, "— opis] Na początku tury, jeżeli co najmniej 5 Tożsamości ma Umiejętności ataku nakładające Moc [Combustion], Liczniki [Combustion] lub Szczególne Podpalenie, Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; bez jednostek zapasowych)\n\nPodstawowe Umiejętności ataku Tożsamości Stowarzyszenia Liu zyskują Moc Monety Plus +2 (Umiejętności monety Minus zyskują Moc Bazową +(8/liczba monet) (min. 1, zaokrąglając w dół))\n\nUmiejętności inne niż Umiejętność 3 nakładające Moc [Combustion], Liczniki [Combustion] lub Szczególne Podpalenie zadają +20% obrażeń (wliczając Umiejętności E.G.O).\n\nUmiejętności 3 nakładające Moc [Combustion], Liczniki [Combustion] lub Szczególne Podpalenie zyskują Moc Monety Plus +1 (Umiejętności monety Minus zyskują Moc Bazową +(4/liczba monet) (min. 1, zaokrąglając w dół)) i zadają +30% obrażeń.\n- Za każdą Tożsamość tego samego Stowarzyszenia w zespole Umiejętności te zadają +5% obrażeń (maks. 20%, z jednostkami zapasowymi)\n\nNa koniec tury 2 sojuszników o najniższej Poczytalności odzyskuje 8 Poczytalności\n- Jeżeli Poczytalność celu wynosi 0 lub mniej, odzyskuje dodatkowo 5"),
F(221, "— opis skrócony] Umiejętności zyskują Moc i zadają więcej obrażeń"),
F(222, "— nazwa] Czyjeś Urządzenie"),
F(223, "— opis] Na koniec ataku, jeżeli [IndexPrescriptTargetToEnemy] ginie, sojusznik, który pokonał [IndexPrescriptTargetToEnemy], zyskuje 1 [AzureResultUp] na następną turę, a Liczniki [Sinking] 1 losowego przeżyłego wroga rosną o 3 (1 raz na turę)\n- Jeżeli sojusznikiem, który pokonał [IndexPrescriptTargetToEnemy], jest Tożsamość Wskazującego, zamiast [AzureResultUp] zyskuje 1 [Enhancement] na następną turę (1 raz na turę)\n\nNa koniec tury jednostki Wskazującego otrzymują obrażenia równe (posiadana wartość [KarmaOfIndexAlly])% Maks. HP.\n(Z powodu tego efektu nie ulega Oszołomieniu, a HP nie maleje poniżej 20% Maks. HP)\nNastępnie Tożsamość, która otrzymała obrażenia od tego efektu, zyskuje (posiadana wartość [KarmaOfIndexAlly]/5) [ResultEnhancement] na następną turę (maks. 2)"),
F(224, "— opis skrócony] Zyskuje Wzrost Mocy Posępności. Jeżeli Tożsamość jest z Wskazującego, zamiast tego Wzrost Mocy Ataku"),
F(225, "— opis skrócony] Tożsamości Wskazującego otrzymują obrażenia i zyskują Wzrost Mocy na następną turę"),
F(226, "— nazwa] Opatrzność Nakazu"),
F(227, "— opis] Tożsamości, które w poprzedniej turze nałożyły [Sinking], Liczniki [Sinking] lub Szczególne Zatonięcie efektem Umiejętności, na początku tury zyskują 3 Moc [Breath] lub 2 Liczniki [Breath] (1 raz na turę na Tożsamość)\n\nJeżeli w tej walce Tożsamość zyskała dzięki temu efektowi [Breath] łącznie 3 razy lub więcej, począwszy od następnej tury ten Grzesznik zadaje +30% obrażeń Trafieniami Krytycznymi"),
F(230, "— nazwa] Uniwersalne Narzędzie"),
F(231, "— opis] Gdy wroga trafią 12 razy Umiejętności tego samego typu ataku, jego odporność fizyczna na ten typ ataku +0,1 (w przypadku Anomalii — wszystkie Partie; 3 razy na walkę na wroga; dzięki temu efektowi odporność nie może przekroczyć 2.0)"),
F(232, "— opis skrócony] Cel staje się podatniejszy na dany typ ataku"),
F(233, "— nazwa] Uniwersalne Narzędzie+"),
F(234, "— opis] Gdy wroga trafią <style=\"upgradeHighlight\">9 razy</style> Umiejętności tego samego typu ataku, jego odporność fizyczna na ten typ ataku +0,1 (w przypadku Anomalii — wszystkie Partie; 3 razy na walkę na wroga; dzięki temu efektowi odporność nie może przekroczyć 2.0)"),
F(236, "— nazwa] Uniwersalne Narzędzie++"),
F(237, "— opis] Gdy wroga trafią <style=\"upgradeHighlight\">6 razy</style> Umiejętności tego samego typu ataku, jego odporność fizyczna na ten typ ataku +0,1 (w przypadku Anomalii — wszystkie Partie; 3 razy na walkę na wroga; dzięki temu efektowi odporność nie może przekroczyć 2.0)"),
F(239, "— nazwa] Skradzione Czasopismo Fixerów"),
F(240, "— opis] Na początku tury zyskuje 1 [HitResultUp]\n\nPrzy wywołaniu Pełnego Rezonansu Zazdrości, zyskuje na początku walki 1 [HitDamageUp]\n\nJeżeli na polu są co najmniej 4 Tożsamości Środkowego, na początku spotkania nakłada [RetaliationBook] na 1 losowego wroga"),
F(242, "— opis] Przy trafieniu Umiejętnością Grzechu Zazdrości lub Umiejętnością Kontry, zwiększa Liczniki [Laceration] lub Liczniki [Combustion] o 1 (3 razy na turę)\n\nGdy w trakcie walki Liczniki [Laceration] wroga spadną poniżej 1, jeżeli ten wróg ma co najmniej 2 Liczniki [Combustion], zmniejsza zamiast tego Liczniki [Combustion] (3 razy na turę)"),
F(243, "— opis skrócony] Zwiększa Liczniki Krwawienia i Podpalenia"),
F(244, "— opis skrócony] Zmniejsza Liczniki Podpalenia"),
F(245, "— nazwa] Śnieżnobiałe Płótno"),
]
