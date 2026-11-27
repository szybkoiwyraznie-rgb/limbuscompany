# -*- coding: utf-8 -*-
# P59 Dary E.G.O cz. 4q
def F(seq, pl): return (seq, pl)
PART = [
F(428, "— opis] Walki Łańcuchowe: gdy pojawi się nowy wróg, nakłada na niego na początku walki 5 [Laceration] i 3 Liczniki [Laceration]."),
F(431, "— opis] Gdy ginie sojusznik, zyskuje po 1 Zasobie E.G.O Grzechu Umiejętności 1, 2 i 3 tego sojusznika oraz 1 losowy Zasób E.G.O\nNa koniec ataku, jeżeli wróg ginie, zyskuje 1 losowy Zasób E.G.O (maks. 1 raz na Umiejętność)"),
F(432, "— opis skrócony] Gdy ginie sojusznik, zyskuje po 1 Zasobie E.G.O Grzechu Umiejętności 1, 2 i 3 tego sojusznika oraz 1 losowy Zasób E.G.O"),
F(433, "— opis skrócony] Na koniec ataku, jeżeli wróg ginie, zyskuje 1 losowy Zasób E.G.O"),
F(434, "— nazwa] Nieustający Głód"),
F(435, "— opis] Na początku 1. tury spotkania Poczytalność Tożsamości na polu maleje o 5, a ta Tożsamość zyskuje 1 [Enhancement] na 3 tury.\nJeżeli Tożsamość jest Krwiożercą, traci 10 Poczytalności; zyskuje 2 [Enhancement] na 3 tury, a przy nakładaniu Mocy [Laceration] i Liczników [Laceration] efektem Umiejętności lub Monety nakłada o 1 więcej"),
F(436, "— opis skrócony] Na początku 1. tury spotkania Poczytalność Tożsamości na polu maleje o 5, a ta Tożsamość zyskuje 1 [Enhancement] na 3 tury."),
F(437, "— opis skrócony] Jeżeli Tożsamość jest Krwiożercą, traci 10 Poczytalności; zyskuje 2 [Enhancement] na 3 tury, a przy nakładaniu Mocy i Liczników [Laceration] efektem Umiejętności lub Monety nakłada o 1 więcej"),
F(438, "— nazwa] Małe Marzenie"),
F(439, "— opis] Przy wygranej Starciu Umiejętnością Grzechu Pychy odzyskuje 5 Poczytalności.\nPrzy trafieniu po wygranej tą Umiejętnością, zwiększa Liczniki [Laceration] i [Burst] celu o 1 (maks. 4 na Umiejętność)"),
F(440, "— opis skrócony] Przy wygranej Starciu Umiejętnością Grzechu Pychy odzyskuje 5 Poczytalności, a przy trafieniu po wygranej Starciu zwiększa Liczniki [Laceration] i Liczniki [Burst] celu o 1"),
F(441, "— nazwa] Puste Marzenie"),
F(442, "— opis] Przy trafieniu celu z [Laceration] lub Szczególnym Krwawieniem, odzyskuje 2-5 HP.\nUmiejętności zużywające [BloodDinner] zyskują Moc Monet +1"),
F(443, "— opis skrócony] Odzyskuje HP przy trafieniu atakiem celu z nałożonym [Laceration] lub Szczególnym Krwawieniem."),
F(444, "— opis skrócony] Umiejętności zużywające [BloodDinner] zyskują Moc Monet +1"),
F(445, "— nazwa] Marzenie na Nowo"),
F(446, "— opis] Wszystkie Umiejętności Don Kichota zyskują Moc Końcową +2\nGdy ginie sojusznik, sojusznicy odzyskują 15 Poczytalności, a na koniec tury zyskują 1 [Enhancement] na następną turę (maks. zdobytych [Enhancement]: 3)"),
F(447, "— opis skrócony] Wszystkie Umiejętności Don Kichota zyskują Moc Końcową +2"),
F(448, "— opis skrócony] Gdy ginie sojusznik, sojusznicy odzyskują 15 Poczytalności i zyskują 1 [Enhancement] na następną turę"),
F(490, "— opis] Na początku tury, jeżeli co najmniej 5 Tożsamości ma Umiejętności ataku nakładające Moc [Vibration], Liczniki [Vibration] lub Szczególny Wstrząs, Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; z pominięciem jednostek zapasowych)\n\nUmiejętności 3 sojuszników nakładających Moc [Vibration], Liczniki [Vibration] lub Szczególny Wstrząs zyskują Moc Monet +2 i zadają +25% obrażeń.\n\nGdy sojusznik nakładający Moc [Vibration], Liczniki [Vibration] lub Szczególny Wstrząs [Switch_Vibration] wroga Umiejętnością ataku (wliczając Umiejętności E.G.O), przekształcana Moc [Vibration] i Liczniki [Vibration] są stosowane 1,5 razy większe (tylko przy przekształceniu w inny typ) i nakłada 5 [DefenseDown] na następną turę (1 raz na turę).\n\nNa początku tury 3 wrogów o najniższej Szybkości zyskuje Moc [Vibration] równą (12-obecna Szybkość) (min. 6; maks. 1 raz na falę)."),
F(491, "— opis skrócony] Umiejętność 3 zyskuje Moc Monet +2 i zadaje +25% obrażeń"),
F(495, "— opis] Na początku tury, jeżeli co najmniej 5 Tożsamości ma Umiejętności ataku nakładające Moc [Vibration], Liczniki [Vibration] lub Szczególny Wstrząs, Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; z pominięciem jednostek zapasowych)\n\nUmiejętności 3 sojuszników nakładających Moc [Vibration], Liczniki [Vibration] lub Szczególny Wstrząs zyskują Moc Monet +2 i zadają +25% obrażeń.\n\nGdy sojusznik nakładający Moc [Vibration], Liczniki [Vibration] lub Szczególny Wstrząs zadaje obrażenia wrogowi o co najmniej 2 Szybkości wolniejszemu od niego, zadaje +(Moc [Vibration] celu, maks. 25)% obrażeń, a przy każdym zadaniu obrażeń nakłada 2 [DefenseDown] (maks. 6).\n\nNa początku tury nakłada 1 wrogowi z najwyższą Szybkością Moc [Vibration] równą (12-obecna Szybkość) (min. 6) i Liczniki [Vibration] równe połowie tej wartości (zaokrąglając w górę; w przypadku Anomalii — 1 Partię; maks. 1 raz na falę)."),
]
