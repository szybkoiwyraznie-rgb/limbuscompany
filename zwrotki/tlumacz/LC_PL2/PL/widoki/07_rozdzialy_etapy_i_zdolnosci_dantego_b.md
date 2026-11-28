# Rozdziały, węzły etapów, lochy fabularne, zdolności Dantego i efekty tekstowe (część b) — Limbus Company

Tytuły części i rozdziałów, nazwy i opisy wszystkich węzłów na mapie etapów, lochów fabularnych, zdolności Złotej Gałęzi (Durante) oraz napisy specjalne w walkach fabularnych.

Polski tekst wpisujesz w **jednej linii** po `PL:`. Znacznik `\n` oznacza łamanie linii w oknie gry — zachowaj go tam, gdzie napis ma mieć kilka wierszy. Nie zmieniaj linii `źródło:`, `limit:`, `tokeny:` ani `EN:`.

## Rozdziały, etapy i zdolności Dantego: StageContinueText
- plik gry: `StageContinueText.json`

1. [Rozdziały, etapy i zdolności Dantego [StageInfoUI_ContinueText] — tekst] 컨티뉴 가능
   źródło: StageContinueText.json :: dataList[id=StageInfoUI_ContinueText].content
   limit: do 120 znaków
   EN: Continuable
   PL:
2. [Rozdziały, etapy i zdolności Dantego [ContinueMainTitle] — tekst] 컨티뉴
   źródło: StageContinueText.json :: dataList[id=ContinueMainTitle].content
   limit: do 120 znaków
   EN: Continue
   PL:
3. [Rozdziały, etapy i zdolności Dantego [ContinueMainDesc_HellChainInsufficient] — tekst] 전투에서 패배했습니다.\n<color=#e94d37>광기 40</color>을 사용하여 계속 플레이 하시겠습니까?\n\n<color=#ebcaa2><컨티뉴 시 적용되는 효과></color>\n<color=#F8C200>- 인격, E.G.O가 보유한 효과의 전투당 횟수 제한 초기화\n- 모든 속성 E.G.O 자원 +10\n- 모든 아군 체력 · 정신력 최대로 회복\n(빼기 코인 인격은 정신력 -30으로 적용)</color>
   źródło: StageContinueText.json :: dataList[id=ContinueMainDesc_HellChainInsufficient].content
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: <color=#e94d37>, </color>, <color=#ebcaa2>, <color=#F8C200>, \n
   EN: You have been defeated.\nUse <color=#e94d37>40 Lunacy</color> and continue the battle?\n\n<color=#ebcaa2><Effects Applied Upon Continuing></color>\n<color=#F8C200>- Reset Identities & E.G.O Per-Encounter Effect Activation Limits\n- Gain 10 E.G.O Resources for all Affinities\n- Fully restore HP and SP of all allies\n(SP of Minus Coin Identities set to -30)</color>
   PL:
4. [Rozdziały, etapy i zdolności Dantego [ContinueMainRemainContinueCount] — tekst] 남은 횟수
   źródło: StageContinueText.json :: dataList[id=ContinueMainRemainContinueCount].content
   limit: do 120 znaków
   EN: Remaining Continues
   PL:
5. [Rozdziały, etapy i zdolności Dantego [ContinueMainHaveLunacy] — tekst] 보유 광기
   źródło: StageContinueText.json :: dataList[id=ContinueMainHaveLunacy].content
   limit: do 120 znaków
   EN: Remaining Lunacy
   PL:
6. [Rozdziały, etapy i zdolności Dantego [ContinueMainFreeLunacy] — tekst] 무료
   źródło: StageContinueText.json :: dataList[id=ContinueMainFreeLunacy].content
   limit: do 120 znaków
   EN: Free
   PL:
7. [Rozdziały, etapy i zdolności Dantego [ContinueMainPaidLunacy] — tekst] 유료
   źródło: StageContinueText.json :: dataList[id=ContinueMainPaidLunacy].content
   limit: do 120 znaków
   EN: Paid
   PL:
8. [Rozdziały, etapy i zdolności Dantego [ContinueMainCancel] — tekst] 스테이지 포기
   źródło: StageContinueText.json :: dataList[id=ContinueMainCancel].content
   limit: do 120 znaków
   EN: Forfeit Battle
   PL:
9. [Rozdziały, etapy i zdolności Dantego [ContinueMainUseContinue] — tekst] 컨티뉴 진행
   źródło: StageContinueText.json :: dataList[id=ContinueMainUseContinue].content
   limit: do 120 znaków
   EN: Continue Battle
   PL:
10. [Rozdziały, etapy i zdolności Dantego [ContinueMainBuyHellChain] — tekst] 컨티뉴 진행
   źródło: StageContinueText.json :: dataList[id=ContinueMainBuyHellChain].content
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
11. [Rozdziały, etapy i zdolności Dantego [ContinueConfirm_Title_HellChain] — tekst] 안내
   źródło: StageContinueText.json :: dataList[id=ContinueConfirm_Title_HellChain].content
   limit: do 120 znaków
   EN: Notice
   PL:
12. [Rozdziały, etapy i zdolności Dantego [ContinueConfirm_Desc] — tekst] 스테이지 컨티뉴 기능을 사용해 스테이지를 클리어한 경우,\nEX 클리어로 기록되지 않습니다.\n또한 컨티뉴에 사용된 재화가 반환되지 않으며,\n사용된 광기는 청약철회가 불가능합니다.\n\n단, 스테이지를 포기하거나 비상적으로 게임이 종료된 경우,\n이번 전투에서 컨티뉴에 사용된 재화가 모두 반환됩니다.
   źródło: StageContinueText.json :: dataList[id=ContinueConfirm_Desc].content
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Clearing this Stage by using a Stage Continue function will prevent its Extra Conditions from being fulfilled.\nAlso, upon clearing the Stage, resources spent to continue this battle will not be restored, and spent Lunacy cannot be refunded.\n\nHowever, if, after using the Continue function, the player forfeits this Stage or if the game closes due to unusual circumstances, any Lunacy spent to continue this battle will be restored.
   PL:
13. [Rozdziały, etapy i zdolności Dantego [ContinueConfirm_Skip] — tekst] 다음 접속까지 안내 팝업 띄우지 않기
   źródło: StageContinueText.json :: dataList[id=ContinueConfirm_Skip].content
   limit: do 120 znaków
   EN: Don't show this message again until next login
   PL:
14. [Rozdziały, etapy i zdolności Dantego [ContinuePurchase_LunacyTitle] — tekst] 광기
   źródło: StageContinueText.json :: dataList[id=ContinuePurchase_LunacyTitle].content
   limit: do 120 znaków
   EN: Lunacy
   PL:
15. [Rozdziały, etapy i zdolności Dantego [ContinuePurchase_Notice] — tekst] ※ 무료 광기부터 사용됩니다.
   źródło: StageContinueText.json :: dataList[id=ContinuePurchase_Notice].content
   limit: do 120 znaków
   EN: ※ Free Lunacy is used first.
   PL:
16. [Rozdziały, etapy i zdolności Dantego [ContinueConfirmCancel] — tekst] 취소
   źródło: StageContinueText.json :: dataList[id=ContinueConfirmCancel].content
   limit: do 120 znaków
   EN: Cancel
   PL:
17. [Rozdziały, etapy i zdolności Dantego [ContinueMainConfirm] — tekst] 컨티뉴 진행
   źródło: StageContinueText.json :: dataList[id=ContinueMainConfirm].content
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
18. [Rozdziały, etapy i zdolności Dantego [ContinueConfirm_Title_Lunacy] — tekst] 안내
   źródło: StageContinueText.json :: dataList[id=ContinueConfirm_Title_Lunacy].content
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
19. [Rozdziały, etapy i zdolności Dantego [ContinueResult_Win_Desc] — tekst] 스테이지를 클리어하여\n컨티뉴에 사용한 재화가 소모되었습니다.
   źródło: StageContinueText.json :: dataList[id=ContinueResult_Win_Desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Clearing the Stage has consumed all resources\nspent to Continue the battle.
   PL:
20. [Rozdziały, etapy i zdolności Dantego [ContinueResult_Defeat_Desc] — tekst] 스테이지를 포기하여\n컨티뉴에 사용한 재화가 반환되었습니다.
   źródło: StageContinueText.json :: dataList[id=ContinueResult_Defeat_Desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Forfeiting the Stage has returned all resources\nspent to Continue the battle.
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c10p1
- plik gry: `StageNode-a1c10p1.json`

21. [Rozdziały, etapy i zdolności Dantego [11001] — tytuł] 재판
   źródło: StageNode-a1c10p1.json :: dataList[id=11001].title
   limit: do 40 znaków
   EN: The Trial
   PL:
22. [Rozdziały, etapy i zdolności Dantego [11002] — tytuł] 법정
   źródło: StageNode-a1c10p1.json :: dataList[id=11002].title
   limit: do 40 znaków
   EN: The Courthouse
   PL:
23. [Rozdziały, etapy i zdolności Dantego [11003] — tytuł] 계획
   źródło: StageNode-a1c10p1.json :: dataList[id=11003].title
   limit: do 40 znaków
   EN: The Plan
   PL:
24. [Rozdziały, etapy i zdolności Dantego [11004] — tytuł] 시지프 백화점
   źródło: StageNode-a1c10p1.json :: dataList[id=11004].title
   limit: do 40 znaków
   EN: Grand Magasin Sisyphe
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c10p3
- plik gry: `StageNode-a1c10p3.json`

25. [Rozdziały, etapy i zdolności Dantego [11007] — tytuł] 연기
   źródło: StageNode-a1c10p3.json :: dataList[id=11007].title
   limit: do 40 znaków
   EN: The Smoke
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c5p1
- plik gry: `StageNode-a1c5p1.json`

26. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 항해
   źródło: StageNode-a1c5p1.json :: dataList[id=10501].title
   limit: do 40 znaków
   EN: Setting Sail
   PL:
27. [Rozdziały, etapy i zdolności Dantego [10501] — miejsce] 메피스토펠레스 버스배
   źródło: StageNode-a1c5p1.json :: dataList[id=10501].place
   limit: do 40 znaków
   EN: Mephistopheles the Busboat
   PL:
28. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 한바탕 초록색 불빛의 소동이 일단락된 뒤, 버스배는 계속 항해 중이다. 파우스트가 무언갈 발견한 듯이 키가 있는 곳을 향해 걸어간다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10501].desc
   limit: do 160 znaków
   EN: We sail on, the incident with the green lights finally behind us. Faust approaches the helm as though she noticed something.
   PL:
29. [Rozdziały, etapy i zdolności Dantego [10502] — tytuł] 규칙
   źródło: StageNode-a1c5p1.json :: dataList[id=10502].title
   limit: do 40 znaków
   EN: The Laws
   PL:
30. [Rozdziały, etapy i zdolności Dantego [10502] — miejsce] 메피스토펠레스 버스배
   źródło: StageNode-a1c5p1.json :: dataList[id=10502].place
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
31. [Rozdziały, etapy i zdolności Dantego [10502] — opis] 항해에 대한 오티스의 강의가 무르익을 무렵, 엔진이 멈춰버렸다. 앞으로 갈 길은 한참 남았는데…
   źródło: StageNode-a1c5p1.json :: dataList[id=10502].desc
   limit: do 160 znaków
   EN: The engine came to a sputtering halt as Outis's seafaring lecture reached its climax. But we still have so much to go...
   PL:
32. [Rozdziały, etapy i zdolności Dantego [10503] — tytuł] 공명 굽쇠
   źródło: StageNode-a1c5p1.json :: dataList[id=10503].title
   limit: do 40 znaków
   EN: Resonance Tuning Fork
   PL:
33. [Rozdziały, etapy i zdolności Dantego [10503] — miejsce] 메피스토펠레스 버스배
   źródło: StageNode-a1c5p1.json :: dataList[id=10503].place
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
34. [Rozdziały, etapy i zdolności Dantego [10503] — opis] 오티스의 구령에 맞춰 일심동체…는 아니지만 수감자들의 단합으로 엔진이 멈춘 버스배는 움직이고 있었다. 그러던 중 이 호수에 살아남기 위해서 반드시 알아야만 하는 사실이 있었다. 가령 규칙을 어기면 과자 부스러기 꼴이 된다거나… 그리고 우리의 버스배는 항해 노선과는 무관하게 끌려가고 있었다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10503].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Our busboat with a dead engine was still sailing, with every Sinner's hearts and bodies... well, not exactly every Sinner, but most Sinner's hearts and bodies working as one. Oh, and we learned a very valuable lesson about surviving in the Great Lake: that breaking its laws can have catastrophic results.\n... And that's when we noticed that our busboat was getting dragged by something off course.
   PL:
35. [Rozdziały, etapy i zdolności Dantego [10504] — tytuł] 납치범
   źródło: StageNode-a1c5p1.json :: dataList[id=10504].title
   limit: do 40 znaków
   EN: Kidnappers
   PL:
36. [Rozdziały, etapy i zdolności Dantego [10504] — miejsce] U사 청새치 항구선
   źródło: StageNode-a1c5p1.json :: dataList[id=10504].place
   limit: do 40 znaków
   EN: U Corp.'s Marlin Portship
   PL:
37. [Rozdziały, etapy i zdolności Dantego [10504] — opis] 몇 번의 위험과 호수를 건너 목적지에 도착했다. 이번 목적지는 U사의 청새치 항구선 이라는 곳인듯하다. 그곳은 수없이 많은 컨테이너로 이루어진 거대한 배였다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10504].desc
   limit: do 280 znaków
   EN: After numerous trials and tribulations, we finally arrived at our destination. Looks like this place is called Marlin Portship of U Corp., a giant seafaring vessel made by merging together countless shipping containers.
   PL:
38. [Rozdziały, etapy i zdolności Dantego [10505] — tytuł] 명령 불복종
   źródło: StageNode-a1c5p1.json :: dataList[id=10505].title
   limit: do 40 znaków
   EN: Insubordination
   PL:
39. [Rozdziały, etapy i zdolności Dantego [10505] — miejsce] U사 청새치 항구선
   źródło: StageNode-a1c5p1.json :: dataList[id=10505].place
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
40. [Rozdziały, etapy i zdolności Dantego [10505] — opis] 접선하기로 했었던 LCCB 대원 대신 악질적인 납치범이 우릴 반겨주었다. 몸값을 요구하는 그들에게 어떻게 대응해야 할지 논의하고 있었던 와중… 이스마엘은 아랑곳없이 돌발 행동을 한다. 이스마엘의 눈은 여러 감정으로 가득 차 갈피를 못 잡고 있는 것만 같았다. 우리는 납치된 LCCB 대원의 생사도 확인 못 한 채로 납치범들을 물리쳐야 한다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10505].desc
   limit: do 490 znaków
   EN: In place of the LCCB Agent we were supposed to meet was a posse of kidnappers who demanded ransom from us. As we were discussing our plan of action, Ishmael suddenly decided to act. I could see from her eyes... that there was a mix of numerous, complex feelings. Now, we have no choice but to take these kidnappers out, even if we are yet to learn if the LCCB Agent is alive or not.
   PL:
41. [Rozdziały, etapy i zdolności Dantego [10506] — tytuł] 클럽
   źródło: StageNode-a1c5p1.json :: dataList[id=10506].title
   limit: do 40 znaków
   EN: The Club
   PL:
42. [Rozdziały, etapy i zdolności Dantego [10506] — miejsce] U사 청새치 항구선
   źródło: StageNode-a1c5p1.json :: dataList[id=10506].place
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
43. [Rozdziały, etapy i zdolności Dantego [10506] — opis] 모두가 함께 결속된 상태로 작전을 수행하는 건 아닌 것 같다.  우리는 이스마엘의 협박으로 인해 겨우 얻어낸 보스의 위치를 향해 이동했다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10506].desc
   limit: do 210 znaków
   EN: Maybe not everyone felt a sense of unity, a sense of belonging from this group. We headed to the boss's location that Ishmael threatened out of the kidnappers.
   PL:
44. [Rozdziały, etapy i zdolności Dantego [10507] — tytuł] 클럽 2
   źródło: StageNode-a1c5p1.json :: dataList[id=10507].title
   limit: do 40 znaków
   EN: The Club 2
   PL:
45. [Rozdziały, etapy i zdolności Dantego [10507] — miejsce] U사 청새치 항구선
   źródło: StageNode-a1c5p1.json :: dataList[id=10507].place
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
46. [Rozdziały, etapy i zdolności Dantego [10507] — opis] 납치범들의 보스가 있는 곳은 시끄러운 음악들이 새어 나오고 있는 클럽이었다. 조용히 들어가고자 했지만… 우리는 클럽 입구에서부터 싸움에 휩싸이게 되었고 겨우 문지기들을 물러나게 만들었다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10507].desc
   limit: do 360 znaków
   EN: Following the kidnapper's directions, we found ourselves at the entrance of a club blaring with music. I wanted to do this quietly... But we broke into a fight pretty much immediately as we tried to talk to the bouncers. We had to find different ways to convince them to let us in.
   PL:
47. [Rozdziały, etapy i zdolności Dantego [10508] — tytuł] 클럽 3
   źródło: StageNode-a1c5p1.json :: dataList[id=10508].title
   limit: do 40 znaków
   EN: The Club 3
   PL:
48. [Rozdziały, etapy i zdolności Dantego [10508] — miejsce] U사 청새치 항구선
   źródło: StageNode-a1c5p1.json :: dataList[id=10508].place
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
49. [Rozdziały, etapy i zdolności Dantego [10508] — opis] 납치범들의 보스가 있는 곳은 시끄러운 음악들이 새어 나오고 있는 클럽이었다. 조용히 들어가고자 했지만… 우리는 클럽 입구에서부터 싸움에 휩싸이게 되었고 겨우 문지기들을 물러나게 만들었다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10508].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
50. [Rozdziały, etapy i zdolności Dantego [10509] — tytuł] 부선장
   źródło: StageNode-a1c5p1.json :: dataList[id=10509].title
   limit: do 40 znaków
   EN: The First Mate
   PL:
51. [Rozdziały, etapy i zdolności Dantego [10509] — miejsce] U사 청새치 항구선
   źródło: StageNode-a1c5p1.json :: dataList[id=10509].place
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
52. [Rozdziały, etapy i zdolności Dantego [10509] — opis] 클럽을 돌아다니며 납치범들이 소속되어 있는 조직원들을 물리쳤다. 이제 슬슬 그들의 보스가 있는 방도 알아내야 할 텐데…
   źródło: StageNode-a1c5p1.json :: dataList[id=10509].desc
   limit: do 190 znaków
   EN: We trashed the club and defeated members of the Syndicate that the kidnappers were part of. Hopefully we can learn their boss's location soon...
   PL:
53. [Rozdziały, etapy i zdolności Dantego [10510] — tytuł] 부선장 2
   źródło: StageNode-a1c5p1.json :: dataList[id=10510].title
   limit: do 40 znaków
   EN: The First Mate 2
   PL:
54. [Rozdziały, etapy i zdolności Dantego [10510] — miejsce] U사 청새치 항구선
   źródło: StageNode-a1c5p1.json :: dataList[id=10510].place
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
55. [Rozdziały, etapy i zdolności Dantego [10510] — opis] 싱클레어의 활약으로 그들의 보스가 있는 방을 알아냈다. 자신을 쌍갈고리 해적단의 부선장이라고 소개하는데…
   źródło: StageNode-a1c5p1.json :: dataList[id=10510].desc
   limit: do 170 znaków
   EN: We learned where the boss's room was, all thanks to Sinclair. She introduced herself as the first mate of the Twinhook Pirates...
   PL:
56. [Rozdziały, etapy i zdolności Dantego [10511] — tytuł] 컨테이너
   źródło: StageNode-a1c5p1.json :: dataList[id=10511].title
   limit: do 40 znaków
   EN: Shipping Containers
   PL:
57. [Rozdziały, etapy i zdolności Dantego [10511] — miejsce] U사 청새치 항구선
   źródło: StageNode-a1c5p1.json :: dataList[id=10511].place
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
58. [Rozdziały, etapy i zdolności Dantego [10511] — opis] 쌍갈고리 해적단의 부선장, 스미로부터 납치된 LCCB 부서의 팀장이라는 자가 잡혀있는 위치를 전달받았다. 이스마엘은 확실한 몰살을 원하는 것 같았지만… 나는 몸을 던지면서까지 막았다. 논리적으로 설명할 수도, 납득시킬 수도 없었지만, 후회는 없다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10511].desc
   limit: do 420 znaków
   EN: Smee, first mate of the Twinhook Pirates, told us where they were keeping the captured LCCB Team Leader. Ishmael wanted to leave no loose threads behind... But I stopped her, even if it meant putting myself in danger. I have no logical explanation for what I did, nor could I convince Ishmael... But I don't regret what I did.
   PL:
59. [Rozdziały, etapy i zdolności Dantego [10512] — tytuł] 컨테이너 2
   źródło: StageNode-a1c5p1.json :: dataList[id=10512].title
   limit: do 40 znaków
   EN: Shipping Containers 2
   PL:
60. [Rozdziały, etapy i zdolności Dantego [10512] — miejsce] U사 청새치 항구선
   źródło: StageNode-a1c5p1.json :: dataList[id=10512].place
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
61. [Rozdziały, etapy i zdolności Dantego [10512] — opis] 부선장, 스미로부터 납치된 LCCB 부서의 팀장이라는 자가 잡혀있는 위치를 전달받았다. 그곳엔 산처럼 쌓여있는 컨테이너들이 보인다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10512].desc
   limit: do 230 znaków
   EN: Smee, first mate of the Twinhook Pirates, told us where they were keeping the captured LCCB Team Leader. When we got there, we found a whole mountain of shipping containers.
   PL:
62. [Rozdziały, etapy i zdolności Dantego [10513] — tytuł] 파일럿
   źródło: StageNode-a1c5p1.json :: dataList[id=10513].title
   limit: do 40 znaków
   EN: Mr. Pilot
   PL:
63. [Rozdziały, etapy i zdolności Dantego [10513] — miejsce] U사 청새치 항구선
   źródło: StageNode-a1c5p1.json :: dataList[id=10513].place
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
64. [Rozdziały, etapy i zdolności Dantego [10513] — opis] 스미라는 자가 말한 컨테이너를 열자 얼굴엔 눈물범벅이 되어있는 앳된 LCCB 대원이 보인다. 크게 다친 것 같진 않아 보여 다행이다만, 이 자가 팀장이라고…?
   źródło: StageNode-a1c5p1.json :: dataList[id=10513].desc
   limit: do 260 znaków
   EN: When we opened the shipping container Smee singled out, an unexpectedly tearful and youthful face of an LCCB Agent greeted us. I'm glad that he looks mostly unharmed, but... Is he really the Team Leader?
   PL:
65. [Rozdziały, etapy i zdolności Dantego [10514] — tytuł] 파일럿 2
   źródło: StageNode-a1c5p1.json :: dataList[id=10514].title
   limit: do 40 znaków
   EN: Mr. Pilot 2
   PL:
66. [Rozdziały, etapy i zdolności Dantego [10514] — miejsce] U사 청새치 항구선
   źródło: StageNode-a1c5p1.json :: dataList[id=10514].place
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
67. [Rozdziały, etapy i zdolności Dantego [10514] — opis] 파일럿이라는 LCCB 생존자 대원을 만났다. 또한 소드가 살아있다는 반가운 사실도 전해주었다. 이제 파일럿이 겪은 이야기를 들어봐야 할 때이다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10514].desc
   limit: do 200 znaków
   EN: We met an LCCB survivor who called himself Pilot. He shared a very good news with us—that Saude was alive! It's time to listen to what he's got to say.
   PL:
68. [Rozdziały, etapy i zdolności Dantego [10515] — tytuł] 아이스크림
   źródło: StageNode-a1c5p1.json :: dataList[id=10515].title
   limit: do 40 znaków
   EN: Ice Cream
   PL:
69. [Rozdziały, etapy i zdolności Dantego [10515] — miejsce] U사 청새치 항구선
   źródło: StageNode-a1c5p1.json :: dataList[id=10515].place
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
70. [Rozdziały, etapy i zdolności Dantego [10515] — opis] 파일럿으로부터 황금가지가 마지막으로 목격되었다고 하는 로보토미 지부의 변동 좌표를 전달받았다. 아무렇지 않게 말을 이어가던 파일럿은 결국 눈물을 보인다. 부디 앞으로 향할 로보토미 지부에 생존자가 남아있기를 간절히 믿고 싶었다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10515].desc
   limit: do 350 znaków
   EN: Pilot handed us the variable coordinates to the Lobotomy Corp. Branch where the Golden Bough was last seen. Pilot, who so far has been trying to appear nonchalant, broke into tears. I really wanted to believe that there are survivors at the upcoming Lobotomy Corp. Branch.
   PL:
71. [Rozdziały, etapy i zdolności Dantego [10516] — tytuł] 해적들
   źródło: StageNode-a1c5p1.json :: dataList[id=10516].title
   limit: do 40 znaków
   EN: Pirates
   PL:
72. [Rozdziały, etapy i zdolności Dantego [10516] — miejsce] 메피스토펠레스 버스배
   źródło: StageNode-a1c5p1.json :: dataList[id=10516].place
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
73. [Rozdziały, etapy i zdolności Dantego [10516] — opis] 파일럿이 전달해 준 변동 좌표를 토대로 호수 어딘가에 있을 로보토미 지부를 향해 가야 한다.  이스마엘은 초조한 표정으로 계속 망원경을 연신 확인하고 있다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10516].desc
   limit: do 220 znaków
   EN: We have to make our way to the Lobotomy Corp. Branch based on the variable coordinates that Pilot gave us. Meanwhile, Ishmael keeps nervously checking the telescope.
   PL:
74. [Rozdziały, etapy i zdolności Dantego [10517] — tytuł] 해적들 2
   źródło: StageNode-a1c5p1.json :: dataList[id=10517].title
   limit: do 40 znaków
   EN: Pirates 2
   PL:
75. [Rozdziały, etapy i zdolności Dantego [10517] — miejsce] 메피스토펠레스 버스배
   źródło: StageNode-a1c5p1.json :: dataList[id=10517].place
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
76. [Rozdziały, etapy i zdolności Dantego [10517] — opis] 쌍갈고리 해적단들이 우리를 뒤쫓고 있었다. 이스마엘의 제안에 따라 우리가 먼저 그들의 배로 넘어가기로 했다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10517].desc
   limit: do 160 znaków
   EN: The Twinhook Pirates were tailing us. I decided to follow Ishmael's advice and board their ship first before they did ours.
   PL:
77. [Rozdziały, etapy i zdolności Dantego [10518] — tytuł] 파도
   źródło: StageNode-a1c5p1.json :: dataList[id=10518].title
   limit: do 40 znaków
   EN: The Waves
   PL:
78. [Rozdziały, etapy i zdolności Dantego [10518] — miejsce] 메피스토펠레스 버스배
   źródło: StageNode-a1c5p1.json :: dataList[id=10518].place
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
79. [Rozdziały, etapy i zdolności Dantego [10518] — opis] 해적들을 물리쳤지만 찝찝함이 가시지 않는다. 호수의 규칙을 유념하며 계속 항해를 하는 수밖에…
   źródło: StageNode-a1c5p1.json :: dataList[id=10518].desc
   limit: do 200 znaków
   EN: We defeated the Pirates, but... I can't shake this uneasy feeling. Well, no choice but to continue our voyage while minding the laws of the Great Lake.
   PL:
80. [Rozdziały, etapy i zdolności Dantego [10519] — tytuł] 파도 2
   źródło: StageNode-a1c5p1.json :: dataList[id=10519].title
   limit: do 40 znaków
   EN: The Waves 2
   PL:
81. [Rozdziały, etapy i zdolności Dantego [10519] — miejsce] 메피스토펠레스 버스배
   źródło: StageNode-a1c5p1.json :: dataList[id=10519].place
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
82. [Rozdziały, etapy i zdolności Dantego [10519] — opis] 오티스는 시간을 단축하기 위해 규칙을 어기고 파도를 이겨내자고 했다. 곧바로 날씨는 험악해지고 무엇일지 모르는 파도가 밀려온다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10519].desc
   limit: do 220 znaków
   EN: Outis suggested that we break the laws of the Great Lake and sail headfirst into the Waves. The sky immediately darkens, and the unknown Waves begin crashing into us.
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c5p2
- plik gry: `StageNode-a1c5p2.json`

83. [Rozdziały, etapy i zdolności Dantego [10520] — tytuł] 크루즈 파티
   źródło: StageNode-a1c5p2.json :: dataList[id=10520].title
   limit: do 40 znaków
   EN: Cruise Party
   PL:
84. [Rozdziały, etapy i zdolności Dantego [10520] — miejsce] 메피스토펠레스 버스배
   źródło: StageNode-a1c5p2.json :: dataList[id=10520].place
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
85. [Rozdziały, etapy i zdolności Dantego [10520] — opis] 파도를 헤치고 나와, 조금은 잔잔한 항해를 시작했다.\n이제 좌표를 향해 순항할 수 있을까, 그런 생각도 잠시.\n호수 가운데 덩그러니 놓여져 있는 크루즈 선박이 눈에 띈다.
   źródło: StageNode-a1c5p2.json :: dataList[id=10520].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We finally made it out of the Waves and into calmer seas.\nI briefly wondered if we can finally start smooth-sailing toward the coordinates...\n... and that's when I noticed a stationary cruise ship floating in the middle of a Lake.
   PL:
86. [Rozdziały, etapy i zdolności Dantego [10521] — tytuł] 크루즈 파티 2
   źródło: StageNode-a1c5p2.json :: dataList[id=10521].title
   limit: do 40 znaków
   EN: Cruise Party 2
   PL:
87. [Rozdziały, etapy i zdolności Dantego [10521] — miejsce] 크루즈 선박
   źródło: StageNode-a1c5p2.json :: dataList[id=10521].place
   limit: do 40 znaków
   EN: Cruise Ship
   PL:
88. [Rozdziały, etapy i zdolności Dantego [10521] — opis] 정보를 얻기 위해 크루즈 위로 올랐다. 화려한 음식과 치장과는 다르게 사람 한 명 보이지 않는 것이, 어쩐지 서늘한 기운을 느끼게한다.
   źródło: StageNode-a1c5p2.json :: dataList[id=10521].desc
   limit: do 230 znaków
   EN: We boarded the cruise ship to gather some intel. Though it's littered with gaudy decorations, I don't see anyone on board... Something about this whole affair is creeping me out.
   PL:
89. [Rozdziały, etapy i zdolności Dantego [10522] — tytuł] 크루즈 파티 3
   źródło: StageNode-a1c5p2.json :: dataList[id=10522].title
   limit: do 40 znaków
   EN: Cruise Party 3
   PL:
90. [Rozdziały, etapy i zdolności Dantego [10522] — miejsce] 크루즈 선박
   źródło: StageNode-a1c5p2.json :: dataList[id=10522].place
   (powtórzenie elementu 87 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
91. [Rozdziały, etapy i zdolności Dantego [10522] — opis] 무서운 이야기를 피해 도망간 싱클레어를 찾아 선실 내부로 들어갔다. 싱클레어는 어렵지 않게 발견할 수 있었다.\n그런데…
   źródło: StageNode-a1c5p2.json :: dataList[id=10522].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I ran into the cabins of the ship in search of Sinclair, who fled from Hong Lu's scary tales. Thankfully, I was able to find him without much trouble.\nBut...
   PL:
92. [Rozdziały, etapy i zdolności Dantego [10523] — tytuł] 크루즈 파티 4
   źródło: StageNode-a1c5p2.json :: dataList[id=10523].title
   limit: do 40 znaków
   EN: Cruise Party 4
   PL:
93. [Rozdziały, etapy i zdolności Dantego [10523] — miejsce] 크루즈 선박
   źródło: StageNode-a1c5p2.json :: dataList[id=10523].place
   (powtórzenie elementu 87 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
94. [Rozdziały, etapy i zdolności Dantego [10523] — opis] 크루즈는 희생의 결과물이었다. 호수 위에서 규칙을 소홀히 한 죄는 이토록 무거웠다.\n…다음 번에는 좀 더 현명한 판단을 해야할 것 같다.
   źródło: StageNode-a1c5p2.json :: dataList[id=10523].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Cruise was an aftermath of a devastation. The consequences of breaking the laws of the Great Lake were severe.\n... I'll have to be more careful from now on.
   PL:
95. [Rozdziały, etapy i zdolności Dantego [10524] — tytuł] 재앙
   źródło: StageNode-a1c5p2.json :: dataList[id=10524].title
   limit: do 40 znaków
   EN: The Calamity
   PL:
96. [Rozdziały, etapy i zdolności Dantego [10524] — miejsce] 로보토미 지부 시추선 어딘가
   źródło: StageNode-a1c5p2.json :: dataList[id=10524].place
   limit: do 60 znaków
   EN: Abandoned Lobotomy Corp. Drilling Ship
   PL:
97. [Rozdziały, etapy i zdolności Dantego [10524] — opis] 안개 너머로 보이는 것은 그토록 찾던 U사의 로보토미 지부였다. 정말 저것이 지부인지 되물을 정도로 기괴한 흰 점막이 지부의 전체를 뒤덮고 있다는 것 만 빼면… 우린 나쁘지 않은 과정 속에 있는 것만 같았다.
   źródło: StageNode-a1c5p2.json :: dataList[id=10524].desc
   limit: do 280 znaków
   EN: The elusive Lobotomy Corp. Branch of U Corp. finally appeared from beyond the veil of mist. But... it was completely covered under a layer of bizarre, white membrane. I think we're on the correct path, at least...
   PL:
98. [Rozdziały, etapy i zdolności Dantego [10525] — tytuł] 고래잡이
   źródło: StageNode-a1c5p2.json :: dataList[id=10525].title
   limit: do 40 znaków
   EN: The Whaler
   PL:
99. [Rozdziały, etapy i zdolności Dantego [10525] — miejsce] 로보토미 지부 시추선 어딘가
   źródło: StageNode-a1c5p2.json :: dataList[id=10525].place
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
100. [Rozdziały, etapy i zdolności Dantego [10525] — opis] 기괴함을 간직한 것은 단순히 외부 만의 일이 아니었다. 희고도 창백한 점막은 그 내부를 모조리 뒤덮고 있었다.\n그리고… 그런 점막을 뒤집어 쓴 채 걸어다니는 이도 있었다.
   źródło: StageNode-a1c5p2.json :: dataList[id=10525].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The bizarreness continued deep into the Lobotomy Corp. Branch. That white, pallid membrane was covering every inch of its interiors.\nAnd... we found those that were shambling around, wrapped under that very same membrane.
   PL:
101. [Rozdziały, etapy i zdolności Dantego [10526] — tytuł] 호수와 나비
   źródło: StageNode-a1c5p2.json :: dataList[id=10526].title
   limit: do 40 znaków
   EN: The Lake and the Butterfly
   PL:
102. [Rozdziały, etapy i zdolności Dantego [10526] — miejsce] 로보토미 지부 시추선 어딘가
   źródło: StageNode-a1c5p2.json :: dataList[id=10526].place
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
103. [Rozdziały, etapy i zdolności Dantego [10526] — opis] 신비로운 분위기를 자아내는 나비를 따라, 우리는 지부의 안으로 더욱 걸어들어갔다. 그 안에는, 찰랑거리는 머리를 가진 자가 있었다.
   źródło: StageNode-a1c5p2.json :: dataList[id=10526].desc
   limit: do 170 znaków
   EN: We followed the mysterious butterfly deeper into the Lobotomy Corp. Branch. A man with a flowing head was waiting for us in there.
   PL:
104. [Rozdziały, etapy i zdolności Dantego [10527] — tytuł] 호수와 나비 2
   źródło: StageNode-a1c5p2.json :: dataList[id=10527].title
   limit: do 40 znaków
   EN: The Lake and the Butterfly 2
   PL:
105. [Rozdziały, etapy i zdolności Dantego [10527] — miejsce] 로보토미 지부 시추선 어딘가
   źródło: StageNode-a1c5p2.json :: dataList[id=10527].place
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
106. [Rozdziały, etapy i zdolności Dantego [10527] — opis] 마치 나비가 수면 위에 잠시 앉았다 날아가듯, 림이라는 자는 꿈결같이 사라졌다. 그리고 우리는, 언젠가 보았던 익숙한 붉은 문양을 떠올린다. …다시 인어들이 몰려든다.
   źródło: StageNode-a1c5p2.json :: dataList[id=10527].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Rim disappeared from our sights like a butterfly leaving its brief respite upon the water surface. It was as though we had all awakened from a dream. From him we saw that familiar red mark. \n... The Mermaids are coming back.
   PL:
107. [Rozdziały, etapy i zdolności Dantego [10529] — tytuł] 호수와 나비 3
   źródło: StageNode-a1c5p2.json :: dataList[id=10529].title
   limit: do 40 znaków
   EN: The Lake and the Butterfly 3
   PL:
108. [Rozdziały, etapy i zdolności Dantego [10529] — miejsce] 로보토미 지부 시추선 어딘가
   źródło: StageNode-a1c5p2.json :: dataList[id=10529].place
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
109. [Rozdziały, etapy i zdolności Dantego [10529] — opis] 림이라는 자의 말대로, 지부 안에서는 황금가지의 흔적을 찾을 수 없었다.\n…그의 말대로 고래라는 걸 찾아야만 하겠지.
   źródło: StageNode-a1c5p2.json :: dataList[id=10529].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Rim was right. We could not find even a hint of the Golden Bough from within the Lobotomy Corp. Branch.\n... We'll have to search for the Whale like he said, then.
   PL:
110. [Rozdziały, etapy i zdolności Dantego [10530] — tytuł] 작살
   źródło: StageNode-a1c5p2.json :: dataList[id=10530].title
   limit: do 40 znaków
   EN: Harpoons
   PL:
111. [Rozdziały, etapy i zdolności Dantego [10530] — miejsce] 로보토미 지부 시추선 입구
   źródło: StageNode-a1c5p2.json :: dataList[id=10530].place
   limit: do 60 znaków
   EN: Lobotomy Corp. Drilling Ship Entrance
   PL:
112. [Rozdziały, etapy i zdolności Dantego [10530] — opis] 베르길리우스와 합류를 대기하려는데, 갑작스러운 충격이 지부를 덮쳤다. 황급히 외부로 나가 안개 속을 쳐다보았더니… 그 안개로부터 험상궂은 선박이 고개를 내밀기 시작했다.
   źródło: StageNode-a1c5p2.json :: dataList[id=10530].desc
   limit: do 230 znaków
   EN: We were waiting by the entrance when a sudden shock shook the Lobotomy Corp. Branch. We hurried out and gazed into the mists... and saw several intimidating-looking vessels emerge.
   PL:
113. [Rozdziały, etapy i zdolności Dantego [10532] — tytuł] 작은 형님
   źródło: StageNode-a1c5p2.json :: dataList[id=10532].title
   limit: do 40 znaków
   EN: The Big Brother
   PL:
114. [Rozdziały, etapy i zdolności Dantego [10532] — miejsce] 로보토미 지부 시추선 입구
   źródło: StageNode-a1c5p2.json :: dataList[id=10532].place
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
115. [Rozdziały, etapy i zdolności Dantego [10532] — opis] 습격한 해적들을 처리하고 있었지만, 이들은 그저 전초전에 불과하다는 생각이 불현듯 스쳤다. 그러고보면, 아직 저들의 선박 중 가장 화려하고 커다란 것은 우리에게 갈고리를 걸지 않았었는데…
   źródło: StageNode-a1c5p2.json :: dataList[id=10532].desc
   limit: do 290 znaków
   EN: We were making relatively short work of the ambushing pirates, but I had a feeling that they were just gauging our capabilities... Now that I mention it, the largest and gaudiest vessel from their fleet has yet to hook us.
   PL:
116. [Rozdziały, etapy i zdolności Dantego [10533] — tytuł] 작은 형님 2
   źródło: StageNode-a1c5p2.json :: dataList[id=10533].title
   limit: do 40 znaków
   EN: The Big Brother 2
   PL:
117. [Rozdziały, etapy i zdolności Dantego [10533] — miejsce] 로보토미 지부 시추선 입구
   źródło: StageNode-a1c5p2.json :: dataList[id=10533].place
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
118. [Rozdziały, etapy i zdolności Dantego [10533] — opis] 이건 일종의 유린이나 기만에 가깝다. 이스마엘은 계속해서 죽고, 나는 그 죽음의 고통을 공유하며 끊임없이 되살린다.\n…승리는 요원하다. 정말 파우스트가 말한 대로… 여기서 끝이 나는 걸까.
   źródło: StageNode-a1c5p2.json :: dataList[id=10533].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This is nothing short of a massacre. A humiliation. He kills Ishmael again and again. I keep bringing her back, feeling that very same pain that killed her.\n... This battle is lost. Maybe Faust is right... Maybe this is where our journey ends.
   PL:
119. [Rozdziały, etapy i zdolności Dantego [10534] — tytuł] 쪽빛노인
   źródło: StageNode-a1c5p2.json :: dataList[id=10534].title
   limit: do 40 znaków
   EN: The Indigo Elder
   PL:
120. [Rozdziały, etapy i zdolności Dantego [10534] — miejsce] 메피스토펠레스 버스배
   źródło: StageNode-a1c5p2.json :: dataList[id=10534].place
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
121. [Rozdziały, etapy i zdolności Dantego [10534] — opis] 푸른 불꽃이 올라오는 담배를 물고 있는 노인은, 설명을 들을 필요도 없이 강력했다. 파우스트는 이미 이 자가 누구인지 아는 듯이, 가벼운 인사와 함께 그를 베르길리우스에게로 데려갔다.
   źródło: StageNode-a1c5p2.json :: dataList[id=10534].desc
   limit: do 320 znaków
   EN: Blue embers flickered from the old man's cigar. We didn't need anyone to tell us that he was overwhelmingly powerful; we knew instinctively. Faust, who seemed to recognize the old man, led him to Vergilius after a quick exchange of pleasantries.
   PL:
122. [Rozdziały, etapy i zdolności Dantego [10535] — tytuł] 암초
   źródło: StageNode-a1c5p2.json :: dataList[id=10535].title
   limit: do 40 znaków
   EN: Rocks
   PL:
123. [Rozdziały, etapy i zdolności Dantego [10535] — miejsce] 메피스토펠레스 보트
   źródło: StageNode-a1c5p2.json :: dataList[id=10535].place
   limit: do 40 znaków
   EN: Mephistopheles' Skiff
   PL:
124. [Rozdziały, etapy i zdolności Dantego [10535] — opis] 쪽빛노인과 의논한 대로, 우리는 회색빛 호수를 향해 노를 저어갔다. 탁하고 흐린 호수의 물결 위로, 희끄무레한 암초 같은 것들이 멀찍하게 보인다. 저것들을 피하면서 지나가야 하는 건가.
   źródło: StageNode-a1c5p2.json :: dataList[id=10535].desc
   limit: do 270 znaków
   EN: We rowed toward the gray Lake as we previously discussed with the Indigo Elder. We can see some rocks poking out of the pale, opaque waters of the Lake. Looks like we'll have to maneuver our way between them.
   PL:
125. [Rozdziały, etapy i zdolności Dantego [10537] — tytuł] 창백한 고래
   źródło: StageNode-a1c5p2.json :: dataList[id=10537].title
   limit: do 40 znaków
   EN: The Pallid Whale
   PL:
126. [Rozdziały, etapy i zdolności Dantego [10537] — miejsce] 메피스토펠레스 보트
   źródło: StageNode-a1c5p2.json :: dataList[id=10537].place
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
127. [Rozdziały, etapy i zdolności Dantego [10537] — opis] 암초라고 생각했던 구멍 고래 위로 흘러나오는 인어들을 해치워냈다. 하지만… 우리가 찾는 고래는 이게 아닐텐데, 이스마엘이 이렇게 한 이유가 뭘까?\n히스클리프의 안색을 보아하니… 나만 궁금한 건 아닌 것 같다.
   źródło: StageNode-a1c5p2.json :: dataList[id=10537].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: What we thought to be a rock was a Porous Whale. When its Mermaids crawled out of the holes, we defeated them. But... This isn't the Whale we're looking for, is it? What is Ishmael thinking?\nI could tell from the look on Heathcliff's face that I wasn't the only one wondering about this.
   PL:
128. [Rozdziały, etapy i zdolności Dantego [10538] — tytuł] 창백한 고래 2
   źródło: StageNode-a1c5p2.json :: dataList[id=10538].title
   limit: do 40 znaków
   EN: The Pallid Whale 2
   PL:
129. [Rozdziały, etapy i zdolności Dantego [10538] — miejsce] 메피스토펠레스 보트
   źródło: StageNode-a1c5p2.json :: dataList[id=10538].place
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
130. [Rozdziały, etapy i zdolności Dantego [10538] — opis] 걷혀진 해무를 비집고, 우리는 새카만 호수의 안으로 들어왔다.\n이스마엘이 말하는, 전설 속의 호수. 그리고 그 안에는…\n시릴 정도로 창백한 고래가 있었다.
   źródło: StageNode-a1c5p2.json :: dataList[id=10538].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We waded past the ocean mist and entered the obsidian Lake.\nThe Lake of legends, as told by Ishmael. Within it...\n... Was the Pallid Whale, pale as the midnight moon.
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c5p3
- plik gry: `StageNode-a1c5p3.json`

131. [Rozdziały, etapy i zdolności Dantego [10539] — tytuł] 칠흑 속으로
   źródło: StageNode-a1c5p3.json :: dataList[id=10539].title
   limit: do 40 znaków
   EN: Into the Dark
   PL:
132. [Rozdziały, etapy i zdolności Dantego [10539] — miejsce] 창백한 고래
   źródło: StageNode-a1c5p3.json :: dataList[id=10539].place
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
133. [Rozdziały, etapy i zdolności Dantego [10539] — opis] 걷혀진 해무를 비집고, 우리는 새카만 호수의 안으로 들어왔다.\n이스마엘이 말하는, 전설 속의 호수. 그리고 그 안에는…\n시릴 정도로 창백한 고래가 있었다.
   źródło: StageNode-a1c5p3.json :: dataList[id=10539].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c6p1
- plik gry: `StageNode-a1c6p1.json`

134. [Rozdziały, etapy i zdolności Dantego [10601] — tytuł] 워더링하이츠
   źródło: StageNode-a1c6p1.json :: dataList[id=10601].title
   limit: do 40 znaków
   EN: Wuthering Heights
   PL:
135. [Rozdziały, etapy i zdolności Dantego [10602] — tytuł] 시간이 없어
   źródło: StageNode-a1c6p1.json :: dataList[id=10602].title
   limit: do 40 znaków
   EN: There's no TIME
   PL:
136. [Rozdziały, etapy i zdolności Dantego [10603] — tytuł] 시간이 없어 2
   źródło: StageNode-a1c6p1.json :: dataList[id=10603].title
   limit: do 40 znaków
   EN: There's no TIME 2
   PL:
137. [Rozdziały, etapy i zdolności Dantego [10604] — tytuł] 편지
   źródło: StageNode-a1c6p1.json :: dataList[id=10604].title
   limit: do 40 znaków
   EN: The Letter
   PL:
138. [Rozdziały, etapy i zdolności Dantego [10605] — tytuł] 색깔
   źródło: StageNode-a1c6p1.json :: dataList[id=10605].title
   limit: do 40 znaków
   EN: Colours
   PL:
139. [Rozdziały, etapy i zdolności Dantego [10606] — tytuł] 단장
   źródło: StageNode-a1c6p1.json :: dataList[id=10606].title
   limit: do 40 znaków
   EN: The Makeover
   PL:
140. [Rozdziały, etapy i zdolności Dantego [10607] — tytuł] 대문
   źródło: StageNode-a1c6p1.json :: dataList[id=10607].title
   limit: do 40 znaków
   EN: The Front Gate
   PL:
141. [Rozdziały, etapy i zdolności Dantego [10608] — tytuł] 넬리
   źródło: StageNode-a1c6p1.json :: dataList[id=10608].title
   limit: do 40 znaków
   EN: Nelly
   PL:
142. [Rozdziały, etapy i zdolności Dantego [10609] — tytuł] 환영 인사
   źródło: StageNode-a1c6p1.json :: dataList[id=10609].title
   limit: do 40 znaków
   EN: A Warm Reception
   PL:
143. [Rozdziały, etapy i zdolności Dantego [10610] — tytuł] 캐서린
   źródło: StageNode-a1c6p1.json :: dataList[id=10610].title
   limit: do 40 znaków
   EN: Catherine
   PL:
144. [Rozdziały, etapy i zdolności Dantego [10611] — tytuł] 버틀러
   źródło: StageNode-a1c6p1.json :: dataList[id=10611].title
   limit: do 40 znaków
   EN: Butlers
   PL:
145. [Rozdziały, etapy i zdolności Dantego [10612] — tytuł] 유령
   źródło: StageNode-a1c6p1.json :: dataList[id=10612].title
   limit: do 40 znaków
   EN: The Ghost
   PL:
146. [Rozdziały, etapy i zdolności Dantego [10613] — tytuł] 수수께끼
   źródło: StageNode-a1c6p1.json :: dataList[id=10613].title
   limit: do 40 znaków
   EN: Riddles
   PL:
147. [Rozdziały, etapy i zdolności Dantego [10614] — tytuł] 복도
   źródło: StageNode-a1c6p1.json :: dataList[id=10614].title
   limit: do 40 znaków
   EN: The Corridor
   PL:
148. [Rozdziały, etapy i zdolności Dantego [10615] — tytuł] 복도 2
   źródło: StageNode-a1c6p1.json :: dataList[id=10615].title
   limit: do 40 znaków
   EN: The Corridor 2
   PL:
149. [Rozdziały, etapy i zdolności Dantego [10616] — tytuł] 복도 3
   źródło: StageNode-a1c6p1.json :: dataList[id=10616].title
   limit: do 40 znaków
   EN: The Corridor 3
   PL:
150. [Rozdziały, etapy i zdolności Dantego [10617] — tytuł] 데드레빗츠
   źródło: StageNode-a1c6p1.json :: dataList[id=10617].title
   limit: do 40 znaków
   EN: The Dead Rabbits
   PL:
151. [Rozdziały, etapy i zdolności Dantego [10618] — tytuł] 데드레빗츠 2
   źródło: StageNode-a1c6p1.json :: dataList[id=10618].title
   limit: do 40 znaków
   EN: The Dead Rabbits 2
   PL:
152. [Rozdziały, etapy i zdolności Dantego [10619] — tytuł] 일기장
   źródło: StageNode-a1c6p1.json :: dataList[id=10619].title
   limit: do 40 znaków
   EN: The Diary
   PL:
153. [Rozdziały, etapy i zdolności Dantego [10620] — tytuł] 일기장 2
   źródło: StageNode-a1c6p1.json :: dataList[id=10620].title
   limit: do 40 znaków
   EN: The Diary 2
   PL:
154. [Rozdziały, etapy i zdolności Dantego [10621] — tytuł] 벽난로
   źródło: StageNode-a1c6p1.json :: dataList[id=10621].title
   limit: do 40 znaków
   EN: The Fireplace
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c6p2
- plik gry: `StageNode-a1c6p2.json`

155. [Rozdziały, etapy i zdolności Dantego [10622] — tytuł] 깊고 깊은 지하실
   źródło: StageNode-a1c6p2.json :: dataList[id=10622].title
   limit: do 40 znaków
   EN: Abyssal Basement
   PL:
156. [Rozdziały, etapy i zdolności Dantego [10623] — tytuł] 깊고 깊은 지하실 2
   źródło: StageNode-a1c6p2.json :: dataList[id=10623].title
   limit: do 40 znaków
   EN: Abyssal Basement 2
   PL:
157. [Rozdziały, etapy i zdolności Dantego [10624] — tytuł] 유리관
   źródło: StageNode-a1c6p2.json :: dataList[id=10624].title
   limit: do 40 znaków
   EN: Glass Pods
   PL:
158. [Rozdziały, etapy i zdolności Dantego [10625] — tytuł] 모조품
   źródło: StageNode-a1c6p2.json :: dataList[id=10625].title
   limit: do 40 znaków
   EN: Imitations
   PL:
159. [Rozdziały, etapy i zdolności Dantego [10626] — tytuł] 모조품 2
   źródło: StageNode-a1c6p2.json :: dataList[id=10626].title
   limit: do 40 znaków
   EN: Imitations 2
   PL:
160. [Rozdziały, etapy i zdolności Dantego [10627] — tytuł] 모조품 3
   źródło: StageNode-a1c6p2.json :: dataList[id=10627].title
   limit: do 40 znaków
   EN: Imitations 3
   PL:
161. [Rozdziały, etapy i zdolności Dantego [10628] — tytuł] 그리웠던 얼굴
   źródło: StageNode-a1c6p2.json :: dataList[id=10628].title
   limit: do 40 znaków
   EN: Nostalgic Face
   PL:
162. [Rozdziały, etapy i zdolności Dantego [10629] — tytuł] 모조품 4
   źródło: StageNode-a1c6p2.json :: dataList[id=10629].title
   limit: do 40 znaków
   EN: Imitations 4
   PL:
163. [Rozdziały, etapy i zdolności Dantego [10630] — tytuł] 잘못 끼워진 단추
   źródło: StageNode-a1c6p2.json :: dataList[id=10630].title
   limit: do 40 znaków
   EN: Where It All Went Wrong
   PL:
164. [Rozdziały, etapy i zdolności Dantego [10631] — tytuł] 검은색의 풀
   źródło: StageNode-a1c6p2.json :: dataList[id=10631].title
   limit: do 40 znaków
   EN: Obsidian Grass
   PL:
165. [Rozdziały, etapy i zdolności Dantego [10632] — tytuł] 바이올린
   źródło: StageNode-a1c6p2.json :: dataList[id=10632].title
   limit: do 40 znaków
   EN: Violin
   PL:
166. [Rozdziały, etapy i zdolności Dantego [10633] — tytuł] 매트
   źródło: StageNode-a1c6p2.json :: dataList[id=10633].title
   limit: do 40 znaków
   EN: Matt
   PL:
167. [Rozdziały, etapy i zdolności Dantego [10634] — tytuł] 짐승
   źródło: StageNode-a1c6p2.json :: dataList[id=10634].title
   limit: do 40 znaków
   EN: The Beast
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c6p3
- plik gry: `StageNode-a1c6p3.json`

168. [Rozdziały, etapy i zdolności Dantego [10635] — tytuł] 시계 소리
   źródło: StageNode-a1c6p3.json :: dataList[id=10635].title
   limit: do 40 znaków
   EN: Ticking Sounds
   PL:
169. [Rozdziały, etapy i zdolności Dantego [10636] — tytuł] 이사벨라
   źródło: StageNode-a1c6p3.json :: dataList[id=10636].title
   limit: do 40 znaków
   EN: Isabella
   PL:
170. [Rozdziały, etapy i zdolności Dantego [10637] — tytuł] 피뢰침
   źródło: StageNode-a1c6p3.json :: dataList[id=10637].title
   limit: do 40 znaków
   EN: Lightning Rod
   PL:
171. [Rozdziały, etapy i zdolności Dantego [10638] — tytuł] 와일드헌트
   źródło: StageNode-a1c6p3.json :: dataList[id=10638].title
   limit: do 40 znaków
   EN: The Wild Hunt
   PL:
172. [Rozdziały, etapy i zdolności Dantego [10639] — tytuł] 와일드헌트 2
   źródło: StageNode-a1c6p3.json :: dataList[id=10639].title
   limit: do 40 znaków
   EN: The Wild Hunt 2
   PL:
173. [Rozdziały, etapy i zdolności Dantego [10640] — tytuł] 와일드헌트 3
   źródło: StageNode-a1c6p3.json :: dataList[id=10640].title
   limit: do 40 znaków
   EN: The Wild Hunt 3
   PL:
174. [Rozdziały, etapy i zdolności Dantego [10641] — tytuł] 끝도 없이 막힌 길
   źródło: StageNode-a1c6p3.json :: dataList[id=10641].title
   limit: do 40 znaków
   EN: Impenetrable Path
   PL:
175. [Rozdziały, etapy i zdolności Dantego [10642] — tytuł] 옥상으로
   źródło: StageNode-a1c6p3.json :: dataList[id=10642].title
   limit: do 40 znaków
   EN: To The Rooftop
   PL:
176. [Rozdziały, etapy i zdolności Dantego [10643] — tytuł] 황금가지
   źródło: StageNode-a1c6p3.json :: dataList[id=10643].title
   limit: do 40 znaków
   EN: The Golden Bough
   PL:
177. [Rozdziały, etapy i zdolności Dantego [10644] — tytuł] 마왕
   źródło: StageNode-a1c6p3.json :: dataList[id=10644].title
   limit: do 40 znaków
   EN: Erlking
   PL:
178. [Rozdziały, etapy i zdolności Dantego [10645] — tytuł] 도둑맞은 삶
   źródło: StageNode-a1c6p3.json :: dataList[id=10645].title
   limit: do 40 znaków
   EN: Life, Stolen
   PL:
179. [Rozdziały, etapy i zdolności Dantego [10646] — tytuł] 사랑한다는 말
   źródło: StageNode-a1c6p3.json :: dataList[id=10646].title
   limit: do 40 znaków
   EN: Expression of Love
   PL:
180. [Rozdziały, etapy i zdolności Dantego [10647] — tytuł] 같은 마음
   źródło: StageNode-a1c6p3.json :: dataList[id=10647].title
   limit: do 40 znaków
   EN: Hearts Unbroken
   PL:
181. [Rozdziały, etapy i zdolności Dantego [10648] — tytuł] 모든 세계
   źródło: StageNode-a1c6p3.json :: dataList[id=10648].title
   limit: do 40 znaków
   EN: Every World
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c7p1
- plik gry: `StageNode-a1c7p1.json`

182. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 유명하진 않지만 용감한 돈키호테의 일상과 의뢰에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10701].title
   limit: do 110 znaków
   EN: WHICH TREATS THE LIFE AND THE CONTRACTS OF THE NOT-SO-FAMOUS-BUT-VALIANT DON QUIXOTE
   PL:
183. [Rozdziały, etapy i zdolności Dantego [10702] — tytuł] 림버스컴퍼니가 처음은 아니지만 날개와 협력하는 것에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10702].title
   limit: do 100 znaków
   EN: IN WHICH IS EXPLORED LIMBUS COMPANY'S NOT-EXACTLY-FIRST ALLIANCE WITH A WING
   PL:
184. [Rozdziały, etapy i zdolności Dantego [10703] — tytuł] 수감자들이 도시의 방법으로 해결사에게 인정받는 것에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10703].title
   limit: do 100 znaków
   EN: WHEREIN THE SINNERS ARE ACCEPTED AND RESPECTED BY FIXERS IN WAYS OF THE CITY
   PL:
185. [Rozdziały, etapy i zdolności Dantego [10704] — tytuł] 붉은시선 품에서 벗어난 우리에게 일어난 일들에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10704].title
   limit: do 100 znaków
   EN: OF WHAT BEFELL OUR COMPANY UPON OUR DEPARTURE FROM THE RED GAZE'S HANDS
   PL:
186. [Rozdziały, etapy i zdolności Dantego [10705] — tytuł] 여기에서는 우리의 도련님이 겪어온 이야기가 밝혀진다
   źródło: StageNode-a1c7p1.json :: dataList[id=10705].title
   limit: do 70 znaków
   EN: IN WHICH THE TALE OF OUR YOUNG MASTER IS REVEALED
   PL:
187. [Rozdziały, etapy i zdolności Dantego [10706] — tytuł] 섕크가 우리의 해결사에게 행한 어마어마한 결투에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10706].title
   limit: do 100 znaków
   EN: OF THE IMMENSELY DEVASTATING DUEL IN WHICH OUR FIXER AND THE CINQ BATTLED
   PL:
188. [Rozdziały, etapy i zdolności Dantego [10707] — tytuł] 우리의 훌륭한 정보원 LCD 부서의 두번째 연락에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10707].title
   limit: do 170 znaków
   EN: OF THE EXCELLENT DIALOGUE IN WHICH OUR EXCEPTIONAL INFORMANT LCD DEPARTMENT HAS PASSED INTEL TO US IN OUR SECOND COMMUNICATION
   PL:
189. [Rozdziały, etapy i zdolności Dantego [10708] — tytuł] 버스 기사의 놀이공원과 관리자의 유쾌한 약속에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10708].title
   limit: do 130 znaków
   EN: IN WHICH IS DISCUSSED THE MERRY OATH OF THE BUS DRIVER AND THE MANAGER CONCERNING AMUSEMENT PARKS
   PL:
190. [Rozdziały, etapy i zdolności Dantego [10709] — tytuł] 여기에서는 용감무쌍한 해결사들의 토벌에 결말이 난다
   źródło: StageNode-a1c7p1.json :: dataList[id=10709].title
   limit: do 150 znaków
   EN: WHEREIN IS CONCLUDED THE METHOD BY WHICH ERADICATION QUEST OF FIXERS, THE BRAVE AND THE BOLD, ARE TO BE CONDUCTED
   PL:
191. [Rozdziały, etapy i zdolności Dantego [10710] — tytuł] 라만차랜드의 사건과 혈귀와의 만남에서 생긴 위험에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10710].title
   limit: do 120 znaków
   EN: OF WHAT PERIL BEFELL US IN THE CASE OF LA MANCHALAND AND OUR ENCOUNTER WITH THE BLOODFIENDS
   PL:
192. [Rozdziały, etapy i zdolności Dantego [10711] — tytuł] 림버스컴퍼니와 돈키호테에게 일어난 전투에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10711].title
   limit: do 100 znaków
   EN: WHEREIN IS DISCUSSED THE BATTLE THAT FOUND LIMBUS COMPANY AND DON QUIXOTE
   PL:
193. [Rozdziały, etapy i zdolności Dantego [10712] — tytuł] 쓰러진 혈귀들이 들려주려다 실패한 이야기에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10712].title
   limit: do 120 znaków
   EN: OF THE TALE WHICH THE FALLEN BLOODFIENDS HAVE FAILED TO TELL, DESPITE THEIR BEST ENDEAVORS
   PL:
194. [Rozdziały, etapy i zdolności Dantego [10713] — tytuł] 여기에서는 어트랙션의 내레이션과 퀴즈가 이어진다
   źródło: StageNode-a1c7p1.json :: dataList[id=10713].title
   limit: do 80 znaków
   EN: IN WHICH THE ATTRACTION'S NARRATION AND ITS RIDDLES CONTINUE
   PL:
195. [Rozdziały, etapy i zdolności Dantego [10714] — tytuł] 여기에서는 혈귀와 관련된 뜻밖의 사실들을 이야기한다
   źródło: StageNode-a1c7p1.json :: dataList[id=10714].title
   limit: do 90 znaków
   EN: WHEREIN IS LEARNED THE UNEXPECTED TRUTHS REGARDING BLOODFIENDS
   PL:
196. [Rozdziały, etapy i zdolności Dantego [10715] — tytuł] 여기에서는 라만차랜드에 대한 수감자의 감상을 이야기한다
   źródło: StageNode-a1c7p1.json :: dataList[id=10715].title
   limit: do 90 znaków
   EN: WHEREIN THE SINNERS EACH SHARE THEIR IMPRESSIONS OF LA MANCHALAND
   PL:
197. [Rozdziały, etapy i zdolności Dantego [10716] — tytuł] 해결사 돈키호테가 동료라고 믿은 사람이 벌인 일에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10716].title
   limit: do 120 znaków
   EN: IN WHICH ARE DISCUSSED THE DEEDS OF THE FIXER WHOM DON QUIXOTE HAD BELIEVED TO BE A FRIEND
   PL:
198. [Rozdziały, etapy i zdolności Dantego [10717] — tytuł] 여기에서는 돈키호테가 과거에 겪은 수많은 모험담이 계속된다
   źródło: StageNode-a1c7p1.json :: dataList[id=10717].title
   limit: do 90 znaków
   EN: WHEREIN THE NUMEROUS TALES OF DON QUIXOTE'S ADVENTURES ARE RECOUNTED
   PL:
199. [Rozdziały, etapy i zdolności Dantego [10718] — tytuł] 맘브리노 투구를 탈취한 모험과 주어진 배역들에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10718].title
   limit: do 110 znaków
   EN: OF THE ADVENTURE TO LAY CLAIM UPON THE HELM OF MAMBRINO AND THE ROLES THAT ARE GIVEN
   PL:
200. [Rozdziały, etapy i zdolności Dantego [10719] — tytuł] 관리자와 나눈 분별 있는 이야기와 마술사에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10719].title
   limit: do 110 znaków
   EN: OF THE VERY NICE DISCUSSION THAT WAS HAD BETWEEN THE MANAGER AND THE MAGICIAN
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c7p2
- plik gry: `StageNode-a1c7p2.json`

201. [Rozdziały, etapy i zdolności Dantego [10720] — tytuł] 여기에서는 유령의 집에 대한 수감자들의 감상이 이어진다
   źródło: StageNode-a1c7p2.json :: dataList[id=10720].title
   limit: do 100 znaków
   EN: WHEREIN THE SINNERS EACH SHARE THEIR IMPRESSIONS OF THE HAUNTED MANSION
   PL:
202. [Rozdziały, etapy i zdolności Dantego [10721] — tytuł] '헌티드 블러디 메리' 유령의 집인지 혈귀의 집인지와 맞닥뜨린 수감자들의 모험에 대하여
   źródło: StageNode-a1c7p2.json :: dataList[id=10721].title
   limit: do 230 znaków
   EN: IN WHICH IS RECOUNTED THE SINNERS' ADVENTURE IN THE ENCOUNTER WITH 'HAUNTED: BLOODY MARY', THE NATURE OF WHICH IS UNCLEAR WHETHER IT IS A HAUNTED MANSION OR A BLOODFIENDS' DEN
   PL:
203. [Rozdziały, etapy i zdolności Dantego [10722] — tytuł] 숨어있던 혈귀들과 앞서 지나간 해결사들에 대하여
   źródło: StageNode-a1c7p2.json :: dataList[id=10722].title
   limit: do 110 znaków
   EN: WHEREIN IS DISCUSSED THE BLOODFIENDS IN HIDING AND THE FIXERS WHO ARRIVED FIRST
   PL:
204. [Rozdziały, etapy i zdolności Dantego [10723] — tytuł] 여기에서는 <쓸쓸했던 왕과 행복했던 가족>을 들려준다
   źródło: StageNode-a1c7p2.json :: dataList[id=10723].title
   limit: do 120 znaków
   EN: HERE IT IS RECOUNTED THE TALE OF <THE FORLORN KING AND THE FAMILY THAT WAS ONCE HAPPY>
   PL:
205. [Rozdziały, etapy i zdolności Dantego [10724] — tytuł] 회개하는 혈귀들과 기이한 설문조사에 대하여
   źródło: StageNode-a1c7p2.json :: dataList[id=10724].title
   limit: do 70 znaków
   EN: OF THE PENITENT BLOODFIENDS AND THE BIZARRE SURVEY
   PL:
206. [Rozdziały, etapy i zdolności Dantego [10725] — tytuł] 만일 주의 깊게 본다면 알게 될 사실을 산손이 미리 말하는 일에 대하여
   źródło: StageNode-a1c7p2.json :: dataList[id=10725].title
   limit: do 140 znaków
   EN: IN WHICH A TRUTH THAT MAY BE REVEALED BY CLOSE INSPECTION IS SPOILED BY NONE OTHER THAN SANSÓN HIMSELF
   PL:
207. [Rozdziały, etapy i zdolności Dantego [10726] — tytuł] 하얀 달의 기사와 용감한 돈키호테의 치열한 전투에 대하여
   źródło: StageNode-a1c7p2.json :: dataList[id=10726].title
   limit: do 140 znaków
   EN: WHICH RECOUNTS THE CLOSE AND DRAMATIC DUEL BETWEEN THE KNIGHT OF THE WHITE MOON AND THE VALIANT DON QUIXOTE
   PL:
208. [Rozdziały, etapy i zdolności Dantego [10727] — tytuł] 산손의 연극에 다가온 뻔한 결말에 대하여
   źródło: StageNode-a1c7p2.json :: dataList[id=10727].title
   limit: do 70 znaków
   EN: OF THE PREDICTABLE ENDING TO SANSÓN'S STAGEPLAY
   PL:
209. [Rozdziały, etapy i zdolności Dantego [10728] — tytuł] 가시춘의 의문과 질문에 대한 수감자들의 그냥저냥한 대답에 대하여
   źródło: StageNode-a1c7p2.json :: dataList[id=10728].title
   limit: do 80 znaków
   EN: OF JIA XICHUN'S QUERY AND THE SINNER'S LUKEWARM ANSWERS
   PL:
210. [Rozdziały, etapy i zdolności Dantego [10729] — tytuł] 에밀 싱클레어의 걱정과 돈키호테의 착각에 대하여
   źródło: StageNode-a1c7p2.json :: dataList[id=10729].title
   limit: do 100 znaków
   EN: IN WHICH IS DISCUSSED EMIL SINCLAIR'S CONCERNS AND DON QUIXOTE'S DELUSIONS
   PL:
211. [Rozdziały, etapy i zdolności Dantego [10730] — tytuł] 여기에서는 춤추는 혈귀들과 화려한 퍼레이드에 대해 이야기한다
   źródło: StageNode-a1c7p2.json :: dataList[id=10730].title
   limit: do 100 znaków
   EN: WHEREIN IS TOLD THE STORY OF DANCING BLOODFIENDS AND THE EXTRAVAGANT PARADE
   PL:
212. [Rozdziały, etapy i zdolności Dantego [10731] — tytuł] 행렬의 앞으로 가는 길에 수감자들이 벌인 전투에 대하여
   źródło: StageNode-a1c7p2.json :: dataList[id=10731].title
   limit: do 110 znaków
   EN: OF THE BATTLES THE SINNERS FOUGHT IN THEIR JOURNEY TO THE FRONT OF THE PARADE
   PL:
213. [Rozdziały, etapy i zdolności Dantego [10732] — tytuł] 여기에서는 카세티의 패륜과 비참한 노랫말에 대해 이야기한다
   źródło: StageNode-a1c7p2.json :: dataList[id=10732].title
   limit: do 120 znaków
   EN: WHEREIN IS TOLD THE TALE OF CASSETTI'S FILIAL IMPIETY AND THE TRAGIC NATURE OF THE LYRICS
   PL:
214. [Rozdziały, etapy i zdolności Dantego [10733] — tytuł] 여기에서는 절망에 잠긴 행렬이 계속된다
   źródło: StageNode-a1c7p2.json :: dataList[id=10733].title
   limit: do 60 znaków
   EN: IN WHICH IS CONTINUED THE PARADE OF DESPAIR
   PL:
215. [Rozdziały, etapy i zdolności Dantego [10734] — tytuł] 아름다운 돌시네아와 돈키호테에게 일어난 일에 대하여
   źródło: StageNode-a1c7p2.json :: dataList[id=10734].title
   limit: do 80 znaków
   EN: OF WHAT BEFELL DULCINEA THE BEAUTIFUL AND DON QUIXOTE
   PL:
216. [Rozdziały, etapy i zdolności Dantego [10735] — tytuł] 이어서, 이 모험담을 분명히 하기 위해 꼭 필요한 기억에 대하여
   źródło: StageNode-a1c7p2.json :: dataList[id=10735].title
   limit: do 150 znaków
   EN: TO CONTINUE, IN WHICH IS DISCUSSED THE MEMORY NECESSARY TO BRING TO LIGHT THE CLARITY OF THIS TALE OF ADVENTURE
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c7p3
- plik gry: `StageNode-a1c7p3.json`

217. [Rozdziały, etapy i zdolności Dantego [10736] — tytuł] 꿈에 닿으려 했던 위대한 해결사에 대한 이야기
   źródło: StageNode-a1c7p3.json :: dataList[id=10736].title
   limit: do 80 znaków
   EN: The Tale of a Great Fixer Who Once Reached for The Dream
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c8p1
- plik gry: `StageNode-a1c8p1.json`

218. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 귀향
   źródło: StageNode-a1c8p1.json :: dataList[id=10801].title
   limit: do 40 znaków
   EN: Homeward Bound
   PL:
219. [Rozdziały, etapy i zdolności Dantego [10802] — tytuł] 타종
   źródło: StageNode-a1c8p1.json :: dataList[id=10802].title
   limit: do 40 znaków
   EN: The Bell Tolls
   PL:
220. [Rozdziały, etapy i zdolności Dantego [10803] — tytuł] 방해
   źródło: StageNode-a1c8p1.json :: dataList[id=10803].title
   limit: do 40 znaków
   EN: Disruption
   PL:
221. [Rozdziały, etapy i zdolności Dantego [10804] — tytuł] 방해2
   źródło: StageNode-a1c8p1.json :: dataList[id=10804].title
   limit: do 40 znaków
   EN: Disruption 2
   PL:
222. [Rozdziały, etapy i zdolności Dantego [10805] — tytuł] 꽃잎
   źródło: StageNode-a1c8p1.json :: dataList[id=10805].title
   limit: do 40 znaków
   EN: Petals
   PL:
223. [Rozdziały, etapy i zdolności Dantego [10806] — tytuł] 가보옥
   źródło: StageNode-a1c8p1.json :: dataList[id=10806].title
   limit: do 40 znaków
   EN: Jia Baoyu
   PL:
224. [Rozdziały, etapy i zdolności Dantego [10807] — tytuł] 설보차
   źródło: StageNode-a1c8p1.json :: dataList[id=10807].title
   limit: do 40 znaków
   EN: Xue Baochai
   PL:
225. [Rozdziały, etapy i zdolności Dantego [10808] — tytuł] 이홍원
   źródło: StageNode-a1c8p1.json :: dataList[id=10808].title
   limit: do 40 znaków
   EN: Yihongyuan
   PL:
226. [Rozdziały, etapy i zdolności Dantego [10809] — tytuł] 연무장
   źródło: StageNode-a1c8p1.json :: dataList[id=10809].title
   limit: do 40 znaków
   EN: Training Yard
   PL:
227. [Rozdziały, etapy i zdolności Dantego [10810] — tytuł] 불로불사
   źródło: StageNode-a1c8p1.json :: dataList[id=10810].title
   limit: do 50 znaków
   EN: To be Free from Aging and Death
   PL:
228. [Rozdziały, etapy i zdolności Dantego [10811] — tytuł] N사
   źródło: StageNode-a1c8p1.json :: dataList[id=10811].title
   limit: do 40 znaków
   EN: N Corp.
   PL:
229. [Rozdziały, etapy i zdolności Dantego [10812] — tytuł] 엄지
   źródło: StageNode-a1c8p1.json :: dataList[id=10812].title
   limit: do 40 znaków
   EN: The Thumb
   PL:
230. [Rozdziały, etapy i zdolności Dantego [10813] — tytuł] 참가 선언
   źródło: StageNode-a1c8p1.json :: dataList[id=10813].title
   limit: do 40 znaków
   EN: Declaration of Participation
   PL:
231. [Rozdziały, etapy i zdolności Dantego [10814] — tytuł] 가시춘
   źródło: StageNode-a1c8p1.json :: dataList[id=10814].title
   limit: do 40 znaków
   EN: Jia Xichun
   PL:
232. [Rozdziały, etapy i zdolności Dantego [10815] — tytuł] 침입자
   źródło: StageNode-a1c8p1.json :: dataList[id=10815].title
   limit: do 40 znaków
   EN: Intruders
   PL:
233. [Rozdziały, etapy i zdolności Dantego [10816] — tytuł] 야습
   źródło: StageNode-a1c8p1.json :: dataList[id=10816].title
   limit: do 40 znaków
   EN: Night Ambush
   PL:
234. [Rozdziały, etapy i zdolności Dantego [10817] — tytuł] 야습2
   źródło: StageNode-a1c8p1.json :: dataList[id=10817].title
   limit: do 40 znaków
   EN: Night Ambush 2
   PL:
235. [Rozdziały, etapy i zdolności Dantego [10818] — tytuł] 습인
   źródło: StageNode-a1c8p1.json :: dataList[id=10818].title
   limit: do 40 znaków
   EN: Xiren
   PL:
236. [Rozdziały, etapy i zdolności Dantego [10819] — tytuł] 임대옥
   źródło: StageNode-a1c8p1.json :: dataList[id=10819].title
   limit: do 40 znaków
   EN: Lin Daiyu
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c8p2
- plik gry: `StageNode-a1c8p2.json`

237. [Rozdziały, etapy i zdolności Dantego [10820] — tytuł] 가주 심사 2차전
   źródło: StageNode-a1c8p2.json :: dataList[id=10820].title
   limit: do 70 znaków
   EN: Second Round of the Family Hierarch Evaluation
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c8p3
- plik gry: `StageNode-a1c8p3.json`

238. [Rozdziały, etapy i zdolności Dantego [10821] — tytuł] 홍원의 가주
   źródło: StageNode-a1c8p3.json :: dataList[id=10821].title
   limit: do 40 znaków
   EN: The Hierarch of Hongyuan
   PL:
239. [Rozdziały, etapy i zdolności Dantego [10822] — tytuł] 찰나의 공석
   źródło: StageNode-a1c8p3.json :: dataList[id=10822].title
   limit: do 40 znaków
   EN: Momentary Power Vacuum
   PL:
240. [Rozdziały, etapy i zdolności Dantego [10823] — tytuł] 타인의 정의
   źródło: StageNode-a1c8p3.json :: dataList[id=10823].title
   limit: do 40 znaków
   EN: Justice of Others
   PL:
241. [Rozdziały, etapy i zdolności Dantego [10824] — tytuł] 도둑의 행동
   źródło: StageNode-a1c8p3.json :: dataList[id=10824].title
   limit: do 40 znaków
   EN: Actions of a Thief
   PL:
242. [Rozdziały, etapy i zdolności Dantego [10825] — tytuł] 바꿔보려는 의지
   źródło: StageNode-a1c8p3.json :: dataList[id=10825].title
   limit: do 40 znaków
   EN: The Will to Change
   PL:
243. [Rozdziały, etapy i zdolności Dantego [10826] — tytuł] 가당찮은 발상
   źródło: StageNode-a1c8p3.json :: dataList[id=10826].title
   limit: do 40 znaków
   EN: A Ridiculous Idea
   PL:
244. [Rozdziały, etapy i zdolności Dantego [10827] — tytuł] 두번째 전장
   źródło: StageNode-a1c8p3.json :: dataList[id=10827].title
   limit: do 40 znaków
   EN: The Second Battlefield
   PL:
245. [Rozdziały, etapy i zdolności Dantego [10828] — tytuł] 판단하지 않는 자들
   źródło: StageNode-a1c8p3.json :: dataList[id=10828].title
   limit: do 40 znaków
   EN: Those Who Do Not Decide
   PL:
246. [Rozdziały, etapy i zdolności Dantego [10829] — tytuł] 판단하지 않는 자들2
   źródło: StageNode-a1c8p3.json :: dataList[id=10829].title
   limit: do 40 znaków
   EN: Those Who Do Not Decide 2
   PL:
247. [Rozdziały, etapy i zdolności Dantego [10830] — tytuł] 마음
   źródło: StageNode-a1c8p3.json :: dataList[id=10830].title
   limit: do 40 znaków
   EN: The Heart
   PL:
248. [Rozdziały, etapy i zdolności Dantego [10831] — tytuł] 일시적 휴전
   źródło: StageNode-a1c8p3.json :: dataList[id=10831].title
   limit: do 40 znaków
   EN: Temporary Truce
   PL:
249. [Rozdziały, etapy i zdolności Dantego [10832] — tytuł] 불로불사
   źródło: StageNode-a1c8p3.json :: dataList[id=10832].title
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
250. [Rozdziały, etapy i zdolności Dantego [10833] — tytuł] 희로애락
   źródło: StageNode-a1c8p3.json :: dataList[id=10833].title
   limit: do 50 znaków
   EN: Happiness, Wrath, Sorrow, and Joy
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c9p1
- plik gry: `StageNode-a1c9p1.json`

251. [Rozdziały, etapy i zdolności Dantego [10901] — tytuł] 암중 습격
   źródło: StageNode-a1c9p1.json :: dataList[id=10901].title
   limit: do 40 znaków
   EN: Ambush in the Dark
   PL:
252. [Rozdziały, etapy i zdolności Dantego [10902] — tytuł] 거미줄
   źródło: StageNode-a1c9p1.json :: dataList[id=10902].title
   limit: do 40 znaków
   EN: The Spiders' Thread
   PL:
253. [Rozdziały, etapy i zdolności Dantego [10903] — tytuł] 교본
   źródło: StageNode-a1c9p1.json :: dataList[id=10903].title
   limit: do 40 znaków
   EN: Textbook
   PL:
254. [Rozdziały, etapy i zdolności Dantego [10904] — tytuł] 난도질 당한 기억
   źródło: StageNode-a1c9p1.json :: dataList[id=10904].title
   limit: do 40 znaków
   EN: Mutilated Memory
   PL:
255. [Rozdziały, etapy i zdolności Dantego [10905] — tytuł] 아비규환
   źródło: StageNode-a1c9p1.json :: dataList[id=10905].title
   limit: do 40 znaków
   EN: Abikyōkan
   PL:
256. [Rozdziały, etapy i zdolności Dantego [10906] — tytuł] 아비규환2
   źródło: StageNode-a1c9p1.json :: dataList[id=10906].title
   limit: do 40 znaków
   EN: Abikyōkan 2
   PL:
257. [Rozdziały, etapy i zdolności Dantego [10907] — tytuł] 나선의 역설
   źródło: StageNode-a1c9p1.json :: dataList[id=10907].title
   limit: do 40 znaków
   EN: Paradox of the Spiral
   PL:
258. [Rozdziały, etapy i zdolności Dantego [10908] — tytuł] 현혹
   źródło: StageNode-a1c9p1.json :: dataList[id=10908].title
   limit: do 40 znaków
   EN: Charm
   PL:
259. [Rozdziały, etapy i zdolności Dantego [10909] — tytuł] 방황
   źródło: StageNode-a1c9p1.json :: dataList[id=10909].title
   limit: do 40 znaków
   EN: Wayward
   PL:
260. [Rozdziały, etapy i zdolności Dantego [10910] — tytuł] 불신
   źródło: StageNode-a1c9p1.json :: dataList[id=10910].title
   limit: do 40 znaków
   EN: Doubt
   PL:
261. [Rozdziały, etapy i zdolności Dantego [10911] — tytuł] 인연 얽힘
   źródło: StageNode-a1c9p1.json :: dataList[id=10911].title
   limit: do 40 znaków
   EN: Entangled Fate
   PL:
262. [Rozdziały, etapy i zdolności Dantego [10912] — tytuł] 목적 추론
   źródło: StageNode-a1c9p1.json :: dataList[id=10912].title
   limit: do 40 znaków
   EN: A Distinct Objective
   PL:
263. [Rozdziały, etapy i zdolności Dantego [10913] — tytuł] 아수라장
   źródło: StageNode-a1c9p1.json :: dataList[id=10913].title
   limit: do 40 znaków
   EN: Shurajō
   PL:
264. [Rozdziały, etapy i zdolności Dantego [10914] — tytuł] 분홍빛 욕망
   źródło: StageNode-a1c9p1.json :: dataList[id=10914].title
   limit: do 40 znaków
   EN: Roseate Desire
   PL:
265. [Rozdziały, etapy i zdolności Dantego [10915] — tytuł] 선홍빛 예술
   źródło: StageNode-a1c9p1.json :: dataList[id=10915].title
   limit: do 40 znaków
   EN: Sanguine Artistry
   PL:
266. [Rozdziały, etapy i zdolności Dantego [10916] — tytuł] 손가락
   źródło: StageNode-a1c9p1.json :: dataList[id=10916].title
   limit: do 40 znaków
   EN: The Fingers
   PL:
267. [Rozdziały, etapy i zdolności Dantego [10917] — tytuł] 아비
   źródło: StageNode-a1c9p1.json :: dataList[id=10917].title
   limit: do 40 znaków
   EN: Nursefathers
   PL:
268. [Rozdziały, etapy i zdolności Dantego [10918] — tytuł] 담배와 아비
   źródło: StageNode-a1c9p1.json :: dataList[id=10918].title
   limit: do 40 znaków
   EN: Cigarettes & The Nursefather
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c9p2
- plik gry: `StageNode-a1c9p2.json`

269. [Rozdziały, etapy i zdolności Dantego [10919] — tytuł] 자식
   źródło: StageNode-a1c9p2.json :: dataList[id=10919].title
   limit: do 40 znaków
   EN: Children
   PL:
270. [Rozdziały, etapy i zdolności Dantego [10920] — tytuł] 자식2
   źródło: StageNode-a1c9p2.json :: dataList[id=10920].title
   limit: do 40 znaków
   EN: Children 2
   PL:
271. [Rozdziały, etapy i zdolności Dantego [10921] — tytuł] 신입 사원
   źródło: StageNode-a1c9p2.json :: dataList[id=10921].title
   limit: do 40 znaków
   EN: New Hires
   PL:
272. [Rozdziały, etapy i zdolności Dantego [10922] — tytuł] 신입 사원2
   źródło: StageNode-a1c9p2.json :: dataList[id=10922].title
   limit: do 40 znaków
   EN: New Hires 2
   PL:
273. [Rozdziały, etapy i zdolności Dantego [10923] — tytuł] 관객
   źródło: StageNode-a1c9p2.json :: dataList[id=10923].title
   limit: do 40 znaków
   EN: Audience
   PL:
274. [Rozdziały, etapy i zdolności Dantego [10924] — tytuł] 숨바꼭질
   źródło: StageNode-a1c9p2.json :: dataList[id=10924].title
   limit: do 40 znaków
   EN: Hide-and-Seek
   PL:
275. [Rozdziały, etapy i zdolności Dantego [10925] — tytuł] 충격지네
   źródło: StageNode-a1c9p2.json :: dataList[id=10925].title
   limit: do 40 znaków
   EN: Shock Centipede
   PL:
276. [Rozdziały, etapy i zdolności Dantego [10926] — tytuł] 충격지네2
   źródło: StageNode-a1c9p2.json :: dataList[id=10926].title
   limit: do 40 znaków
   EN: Shock Centipede 2
   PL:
277. [Rozdziały, etapy i zdolności Dantego [10927] — tytuł] 계약
   źródło: StageNode-a1c9p2.json :: dataList[id=10927].title
   limit: do 40 znaków
   EN: The Contract
   PL:
278. [Rozdziały, etapy i zdolności Dantego [10928] — tytuł] 계약2
   źródło: StageNode-a1c9p2.json :: dataList[id=10928].title
   limit: do 40 znaków
   EN: The Contract 2
   PL:
279. [Rozdziały, etapy i zdolności Dantego [10929] — tytuł] 계약3
   źródło: StageNode-a1c9p2.json :: dataList[id=10929].title
   limit: do 40 znaków
   EN: The Contract 3
   PL:
280. [Rozdziały, etapy i zdolności Dantego [10930] — tytuł] 지령의 뜻
   źródło: StageNode-a1c9p2.json :: dataList[id=10930].title
   limit: do 40 znaków
   EN: Will of the Prescript
   PL:
281. [Rozdziały, etapy i zdolności Dantego [10931] — tytuł] 머금은 목화
   źródło: StageNode-a1c9p2.json :: dataList[id=10931].title
   limit: do 40 znaków
   EN: Drenched Gossypium
   PL:
282. [Rozdziały, etapy i zdolności Dantego [10932] — tytuł] 아름다운 청색 빛
   źródło: StageNode-a1c9p2.json :: dataList[id=10932].title
   limit: do 40 znaków
   EN: A Beautiful Hue of Teal
   PL:
283. [Rozdziały, etapy i zdolności Dantego [10933] — tytuł] 선명한 하나
   źródło: StageNode-a1c9p2.json :: dataList[id=10933].title
   limit: do 40 znaków
   EN: That Single Thread
   PL:
284. [Rozdziały, etapy i zdolności Dantego [10934] — tytuł] 집으로
   źródło: StageNode-a1c9p2.json :: dataList[id=10934].title
   limit: do 40 znaków
   EN: Homeward Bound
   PL:
285. [Rozdziały, etapy i zdolności Dantego [10935] — tytuł] 금고
   źródło: StageNode-a1c9p2.json :: dataList[id=10935].title
   limit: do 40 znaków
   EN: The Safe
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c9p3
- plik gry: `StageNode-a1c9p3.json`

286. [Rozdziały, etapy i zdolności Dantego [10936] — tytuł] 거미집 태우기
   źródło: StageNode-a1c9p3.json :: dataList[id=10936].title
   limit: do 40 znaków
   EN: Operation Spider Pyre
   PL:
287. [Rozdziały, etapy i zdolności Dantego [10937] — tytuł] 약지
   źródło: StageNode-a1c9p3.json :: dataList[id=10937].title
   limit: do 40 znaków
   EN: The Ring
   PL:
288. [Rozdziały, etapy i zdolności Dantego [10938] — tytuł] 중지
   źródło: StageNode-a1c9p3.json :: dataList[id=10938].title
   limit: do 40 znaków
   EN: The Middle
   PL:
289. [Rozdziały, etapy i zdolności Dantego [10939] — tytuł] 검지
   źródło: StageNode-a1c9p3.json :: dataList[id=10939].title
   limit: do 40 znaków
   EN: The Index
   PL:
290. [Rozdziały, etapy i zdolności Dantego [10940] — tytuł] 소지
   źródło: StageNode-a1c9p3.json :: dataList[id=10940].title
   limit: do 40 znaków
   EN: The Pinky
   PL:
291. [Rozdziały, etapy i zdolności Dantego [10941] — tytuł] 아라야
   źródło: StageNode-a1c9p3.json :: dataList[id=10941].title
   limit: do 40 znaków
   EN: Araya
   PL:
292. [Rozdziały, etapy i zdolności Dantego [10942] — tytuł] 티켓
   źródło: StageNode-a1c9p3.json :: dataList[id=10942].title
   limit: do 40 znaków
   EN: Ticket
   PL:
293. [Rozdziały, etapy i zdolności Dantego [10943] — tytuł] 부화
   źródło: StageNode-a1c9p3.json :: dataList[id=10943].title
   limit: do 40 znaków
   EN: Hatching
   PL:
294. [Rozdziały, etapy i zdolności Dantego [10944] — tytuł] 가족
   źródło: StageNode-a1c9p3.json :: dataList[id=10944].title
   limit: do 40 znaków
   EN: Family
   PL:
295. [Rozdziały, etapy i zdolności Dantego [10945] — tytuł] 어느 날 갑자기
   źródło: StageNode-a1c9p3.json :: dataList[id=10945].title
   limit: do 40 znaków
   EN: Suddenly, One Day
   PL:
296. [Rozdziały, etapy i zdolności Dantego [10946] — tytuł] 기다림
   źródło: StageNode-a1c9p3.json :: dataList[id=10946].title
   limit: do 40 znaków
   EN: Waiting
   PL:
297. [Rozdziały, etapy i zdolności Dantego [10947] — tytuł] 연민
   źródło: StageNode-a1c9p3.json :: dataList[id=10947].title
   limit: do 40 znaków
   EN: Pity
   PL:
298. [Rozdziały, etapy i zdolności Dantego [10948] — tytuł] 시간얽힘
   źródło: StageNode-a1c9p3.json :: dataList[id=10948].title
   limit: do 40 znaków
   EN: Temporal Entanglement
   PL:
299. [Rozdziały, etapy i zdolności Dantego [10949] — tytuł] 무아
   źródło: StageNode-a1c9p3.json :: dataList[id=10949].title
   limit: do 40 znaków
   EN: Non-self
   PL:
300. [Rozdziały, etapy i zdolności Dantego [10950] — tytuł] 거미줄
   źródło: StageNode-a1c9p3.json :: dataList[id=10950].title
   limit: do 40 znaków
   EN: The Spider's Thread
   PL:
301. [Rozdziały, etapy i zdolności Dantego [10951] — tytuł] 삼세인과
   źródło: StageNode-a1c9p3.json :: dataList[id=10951].title
   limit: do 80 znaków
   EN: Causality that Threads the Past, the Present, and the Future
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode1-0
- plik gry: `StageNode1-0.json`

302. [Rozdziały, etapy i zdolności Dantego [10001] — tytuł] 표범, 사자, 그리고 늑대
   źródło: StageNode1-0.json :: dataList[id=10001].title
   limit: do 40 znaków
   EN: The Panther, Lion, and Wolf
   PL: Pantera, Lew i Wilk
303. [Rozdziały, etapy i zdolności Dantego [10001] — opis] 검고 어두운 숲에서, 나는 길을 잃었다.
   źródło: StageNode1-0.json :: dataList[id=10001].desc
   limit: do 120 znaków
   EN: In a black, dusky forest, I lost the way.
   PL: Zgubiłem drogę w czarnym, ciemnym lesie.
304. [Rozdziały, etapy i zdolności Dantego [10001] — miejsce] 검은 숲
   źródło: StageNode1-0.json :: dataList[id=10001].place
   limit: do 40 znaków
   EN: A Dark Forest
   PL: Ciemny las
305. [Rozdziały, etapy i zdolności Dantego [10002] — tytuł] 자기소개
   źródło: StageNode1-0.json :: dataList[id=10002].title
   limit: do 40 znaków
   EN: Introductions
   PL: Prezentacja
306. [Rozdziały, etapy i zdolności Dantego [10002] — opis] 눈을 뜬 곳은 요상한 버스 안이었다. 자신을 베르길리우스라고 말한 자는, 나를 관리자라고 말하며 관리할 12명의 수감자를 소개하는데…
   źródło: StageNode1-0.json :: dataList[id=10002].desc
   limit: do 210 znaków
   EN: When I awoke, I was on a peculiar bus. The man who introduced himself as “Vergilius” showed me to the twelve Sinners I’ll be overseeing as their new manager…
   PL: Ocknąłem się w osobliwym autobusie. Ktoś, kto przedstawił się jako Vergilius, nazwał mnie Kierownikiem i przedstawił mi dwunastu Grzeszników, którymi mam kierować…
307. [Rozdziały, etapy i zdolności Dantego [10002] — miejsce] 검은 숲
   źródło: StageNode1-0.json :: dataList[id=10002].place
   (powtórzenie elementu 304 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
308. [Rozdziały, etapy i zdolności Dantego [10003] — tytuł] 여행길
   źródło: StageNode1-0.json :: dataList[id=10003].title
   limit: do 40 znaków
   EN: Hit the Road
   PL: W drogę
309. [Rozdziały, etapy i zdolności Dantego [10003] — opis] 수감자들과 함께하는 전투가 조금씩 익숙해져가는 것 같다. 하지만, 그들이 나와 함께 하는 것을 익숙해하는지는, 별개의 이야기가 아닐까…
   źródło: StageNode1-0.json :: dataList[id=10003].desc
   limit: do 160 znaków
   EN: I’m starting to get used to fighting alongside these Sinners. Though, whether they’re used to my presence is another story…
   PL: Chyba powoli przywykam do walki u boku Grzeszników. Ale czy oni przywykają do mnie u swojego boku, to już chyba zupełnie inna sprawa…
310. [Rozdziały, etapy i zdolności Dantego [10003] — miejsce] 검은 숲
   źródło: StageNode1-0.json :: dataList[id=10003].place
   (powtórzenie elementu 304 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
311. [Rozdziały, etapy i zdolności Dantego [10004] — tytuł] 가능성
   źródło: StageNode1-0.json :: dataList[id=10004].title
   limit: do 40 znaków
   EN: Possibilities
   PL: Możliwości
312. [Rozdziały, etapy i zdolności Dantego [10004] — opis] 거울 속에서 솟아 나온 가능성들이 나타났다. 파우스트는 내가 이 가능성들을 관리해야 한다고 말한다. 대체 과거의 나는 어쩌다가 이런 일을…
   źródło: StageNode1-0.json :: dataList[id=10004].desc
   limit: do 210 znaków
   EN: Various possibilities emerged from the Mirror. Faust says it’s my job to take care of them. Just who was I in the past, and how did I get myself roped into this…?
   PL: Z Lustra wyłoniły się możliwości. Faust mówi, że to ja mam nimi kierować. Jakim cudem ja z przeszłości wpakowałem się w coś takiego…
313. [Rozdziały, etapy i zdolności Dantego [10004] — miejsce] 검은 숲
   źródło: StageNode1-0.json :: dataList[id=10004].place
   (powtórzenie elementu 304 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: StageNode1-1
- plik gry: `StageNode1-1.json`

314. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 부릉부릉
   źródło: StageNode1-1.json :: dataList[id=10101].title
   limit: do 40 znaków
   EN: Vroom-vroom
   PL: Brum-brum
315. [Rozdziały, etapy i zdolności Dantego [10101] — miejsce] 메피스토펠레스 안
   źródło: StageNode1-1.json :: dataList[id=10101].place
   limit: do 40 znaków
   EN: Mephistopheles
   PL: Na pokładzie Mephistophelesa
316. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 버스 안은 어색하면서도 험악한 분위기가 맴돈다. '관리자' 라는 직위를 가지기는 했지만 여기서 내가 어떤 행동을 취해야 하는지 난감하다.  마침 맞은편에 보이는 벌레 팔을 가진 수감자에게 목적지가 어디인지 물어보기로 마음을 먹었다.
   źródło: StageNode1-1.json :: dataList[id=10101].desc
   limit: do 270 znaków
   EN: The ride is awkward and intimidating. Even though I’ve been handed the title of ‘Manager’, I have no idea what to do at a time like this. I decided to ask the Sinner with a bug’s arm where we’re currently headed.
   PL: W autobusie panuje atmosfera niezręczna, a zarazem groźna. Dostałem wprawdzie stanowisko “Kierownika”, ale nie mam pojęcia, co powinienem tu robić. Postanowiłem zapytać siedzącego naprzeciwko Grzesznika z robaczą ręką, dokąd jedziemy.
317. [Rozdziały, etapy i zdolności Dantego [10102] — tytuł] 댄스 타임
   źródło: StageNode1-1.json :: dataList[id=10102].title
   limit: do 40 znaków
   EN: Dance Time
   PL: Pora tańca
318. [Rozdziały, etapy i zdolności Dantego [10102] — miejsce] 4구 뒷골목 어딘가
   źródło: StageNode1-1.json :: dataList[id=10102].place
   limit: do 50 znaków
   EN: Some Backstreets of District 4
   PL: Gdzieś w Zaułkach Dystryktu 4
319. [Rozdziały, etapy i zdolności Dantego [10102] — opis] 시계를 돌리라는 협박과도 같은 부탁을 받고 죽음보다 끔찍한 고통을 연달아 겪었다. 달갑지 않은 형태로 버스는 고요해졌고 나도 입을 다물기로 했다. 이대로 잠자코 목적지인 4구로 간다면 좋으련만…
   źródło: StageNode1-1.json :: dataList[id=10102].desc
   limit: do 330 znaków
   EN: After being “asked” a favor I couldn’t turn down, I was forced to bear a series of pains worse than death rewinding the clock. The bus fell quiet in a less-than-pleasant way, and I kept my mouth shut. Let’s hope nothing else happens until we reach District 4…
   PL: Po prośbie, która brzmiała jak groźba - cofnij zegar - przeszedłem pod rząd kilka męczarni gorszych od śmierci. W autobusie zrobiło się cicho, choć wcale nie przyjemnie, więc i ja postanowiłem trzymać język za zębami. Gdybyśmy tylko tak spokojnie dojechali do Dystryktu 4…
320. [Rozdziały, etapy i zdolności Dantego [10103] — tytuł] 버스 갑판
   źródło: StageNode1-1.json :: dataList[id=10103].title
   limit: do 40 znaków
   EN: The Bus Deck
   PL: Pokład autobusu
321. [Rozdziały, etapy i zdolności Dantego [10103] — miejsce] 4구 뒷골목 어딘가
   źródło: StageNode1-1.json :: dataList[id=10103].place
   (powtórzenie elementu 318 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
322. [Rozdziały, etapy i zdolności Dantego [10103] — opis] 버스를 노리는 뒷골목의 불량배들이 습격했다. 하지만 왜인지, 곧바로 죽이지 않고 반쯤 의식이 있는 이들의 시체를 메피스토펠레스 앞에 놓기 시작하는데...
   źródło: StageNode1-1.json :: dataList[id=10103].desc
   limit: do 230 znaków
   EN: A band of thugs attacks us, trying to take the bus. For some reason, we leave them barely breathing instead of killing them outright, placing them in front of Mephistopheles…
   PL: Napadli na nas zbiry z Zaułków, które upatrzyły sobie autobus. Ale z jakiegoś powodu nie dobijamy ich od razu, tylko zaczynamy układać ich na wpół przytomne ciała przed Mephistophelesem…
323. [Rozdziały, etapy i zdolności Dantego [10104] — tytuł] 엔케팔린
   źródło: StageNode1-1.json :: dataList[id=10104].title
   limit: do 40 znaków
   EN: Enkephalin
   PL: Enkefalina
324. [Rozdziały, etapy i zdolności Dantego [10104] — miejsce] 4구 뒷골목 어딘가
   źródło: StageNode1-1.json :: dataList[id=10104].place
   (powtórzenie elementu 318 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
325. [Rozdziały, etapy i zdolności Dantego [10104] — opis] 수감자들보다 더 든든하게 시체를 해치우던 메피스토펠레스를 감상했다. 처음 봤을 때부터 범상치 않다고는 생각했지만, 대체 이 버스의 정체는 무엇일까? 파우스트가 할 말이 있는 듯 입술을 달싹인다.
   źródło: StageNode1-1.json :: dataList[id=10104].desc
   limit: do 320 znaków
   EN: We watched Mephistopheles as it consumed the corpses, its maw looking more reliable than the Sinners. I knew something was up from the moment I saw this bus for the first time, but what is this thing exactly? Faust seems to have something to say.
   PL: Podziwiałem Mephistophelesa, który rozprawiał się z ciałami sprawniej niż Grzesznicy. Od pierwszej chwili czułem, że to nie jest zwyczajny pojazd, ale czym właściwie jest ten autobus? Faust porusza wargami, jakby chciała coś powiedzieć.
326. [Rozdziały, etapy i zdolności Dantego [10105] — tytuł] 유리
   źródło: StageNode1-1.json :: dataList[id=10105].title
   limit: do 40 znaków
   EN: Yuri
   PL: Yuri
327. [Rozdziały, etapy i zdolności Dantego [10105] — miejsce] 4구 뒷골목 어딘가
   źródło: StageNode1-1.json :: dataList[id=10105].place
   (powtórzenie elementu 318 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
328. [Rozdziały, etapy i zdolności Dantego [10105] — opis] 버스의 '식사'가 어느 정도 끝나고, 베르길리우스가 곧 손님이 방문할 거라 외친다. 달갑지 않은 이 여정에 동행하는 이가 누구일지 궁금해진다.
   źródło: StageNode1-1.json :: dataList[id=10105].desc
   limit: do 230 znaków
   EN: When the bus had just about finished its “meal”, Vergilius shouted to me that we’re expecting a guest. I’m curious to see who’d be joining us on this less-than-pleasant trip.
   PL: Kiedy autobus mniej więcej skończył “posiłek”, Vergilius oznajmił, że zaraz zjawi się gość. Ciekawe, kto dołączy do tej niezbyt przyjemnej podróży.
329. [Rozdziały, etapy i zdolności Dantego [10106] — tytuł] 지도
   źródło: StageNode1-1.json :: dataList[id=10106].title
   limit: do 40 znaków
   EN: Map
   PL: Mapa
330. [Rozdziały, etapy i zdolności Dantego [10106] — miejsce] 4구 뒷골목 어딘가
   źródło: StageNode1-1.json :: dataList[id=10106].place
   (powtórzenie elementu 318 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
331. [Rozdziały, etapy i zdolności Dantego [10106] — opis] 도착한 손님은 한때 로보토미 코퍼레이션에서 근무를 했었다는 유리라는 이름의 해결사였다. 버스가 시체를 먹어 치우는 모습에도 익숙한 광경이라는 듯이 덤덤히 보는 모습을 보아하니 만만치 않게 고생을 겪었던 모양이다. 그런 유리 씨가 지도를 보더니 갑자기 안절부절못한 듯 운전석 쪽을 바라보는데…
   źródło: StageNode1-1.json :: dataList[id=10106].desc
   limit: do 350 znaków
   EN: Our guest was a Fixer named Yuri, a former employee of Lobotomy Corporation. Seeing as she showed an indifferent response to the bus devouring bodies, she must’ve gone through a lot herself. But then she grows nervous as she checks the map and looks at the driver’s seat…
   PL: Gościem okazała się Fikserka imieniem Yuri, która niegdyś pracowała w Lobotomy Corporation. Patrzyła spokojnie, jak autobus pożera trupy, jakby znała ten widok, więc musiała sporo przejść. I właśnie ta Yuri, zerknąwszy na mapę, nagle zaczęła nerwowo spoglądać w stronę fotela kierowcy…
332. [Rozdziały, etapy i zdolności Dantego [10107] — tytuł] 삼인방
   źródło: StageNode1-1.json :: dataList[id=10107].title
   limit: do 40 znaków
   EN: The Trio
   PL: Trójka
333. [Rozdziały, etapy i zdolności Dantego [10107] — miejsce] 4구 뒷골목 어딘가
   źródło: StageNode1-1.json :: dataList[id=10107].place
   (powtórzenie elementu 318 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Rozdziały, etapy i zdolności Dantego [10107] — opis] 이제라도 발견해서 다행일수도 있겠지만… 카론이 길치였다는 충격적인 사실이 밝혀졌다. 보다 못한 유리씨가 카론에게 지도 보는 방법을 알려주겠다며 팔을 걷어붙였고 보다 못한 싱클레어도 자연스럽게 합류했다. 조금 시끄럽긴 해도… 볼만한 광경인 것 같다.
   źródło: StageNode1-1.json :: dataList[id=10107].desc
   limit: do 420 znaków
   EN: I was shocked to learn that… Charon has virtually no sense of direction. Though, I guess it’s fortunate that it’s come to light this early into the trip. Yuri took matters into her own hands and started teaching her how to read a map, and Sinclair joined, too. They’re rather noisy, but still… I can’t say that I hate to see it.
   PL: Może i dobrze, że wyszło to już teraz… ale odkryliśmy wstrząsającą prawdę: Charon nie ma za grosz orientacji w terenie. Yuri nie mogła na to patrzeć i zakasała rękawy, oznajmiając, że nauczy Charon czytać mapę, a Sinclair, który też nie mógł na to patrzeć, jakoś sam się przyłączył. Trochę przy tym hałasu… ale miło popatrzeć.
335. [Rozdziały, etapy i zdolności Dantego [10108] — tytuł] 해충
   źródło: StageNode1-1.json :: dataList[id=10108].title
   limit: do 40 znaków
   EN: Pests
   PL: Szkodniki
336. [Rozdziały, etapy i zdolności Dantego [10108] — miejsce] 4구 뒷골목 어딘가
   źródło: StageNode1-1.json :: dataList[id=10108].place
   (powtórzenie elementu 318 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
337. [Rozdziały, etapy i zdolności Dantego [10108] — opis] 버스의 창문으로 뒷골목 풍경을 보던 로쟈가 갑자기 몸서리를 친다. 눈길이 향한 곳을 쳐다보니 벌레 머리를 한 자들이 모여있다. 그리고 그레고르의 얼굴도 삽시간에 굳어지기 시작했다. 로쟈가 느끼는 징그러운 감정과는 확연하게 다른 표정이었다.
   źródło: StageNode1-1.json :: dataList[id=10108].desc
   limit: do 310 znaków
   EN: Rodya looks out through the window at the Backstreets before flinching abruptly. Her eyes fell on a group of people with the heads of bugs. Then, Gregor’s expression shifted as well. It was not out of flinching disgust like Rodya, though.
   PL: Rodion, która wyglądała przez okno na Zaułki, nagle się wzdrygnęła. Spojrzałem tam, gdzie patrzyła: stała tam grupka ludzi z owadzimi głowami. W mgnieniu oka twarz Gregora też stężała. Ale jego mina wyraźnie różniła się od obrzydzenia, jakie czuła Rodion.
338. [Rozdziały, etapy i zdolności Dantego [10109] — tytuł] 가이드
   źródło: StageNode1-1.json :: dataList[id=10109].title
   limit: do 40 znaków
   EN: Guides
   PL: Przewodnicy
339. [Rozdziały, etapy i zdolności Dantego [10109] — miejsce] 4구 로보토미 지부 앞
   źródło: StageNode1-1.json :: dataList[id=10109].place
   limit: do 50 znaków
   EN: District 4 - LC Branch Entrance
   PL: Dystrykt 4 - przed filią L Corp.
340. [Rozdziały, etapy i zdolności Dantego [10109] — opis] 몇 번의 소동 끝에 우리는 옛 로보토미 코퍼레이션 지부에 도착했다. 지부의 입구 근처에는 처음 보는 사람들이 우리를 기다리는 듯 모여 있는데…
   źródło: StageNode1-1.json :: dataList[id=10109].desc
   limit: do 180 znaków
   EN: After a number of scuffles and scrapes, we arrived at an old Lobotomy Corporation branch. Near the entrance, new faces were waiting for us…
   PL: Po kilku zamieszaniach dotarliśmy do dawnej filii Lobotomy Corporation. Przy wejściu zebrali się nieznajomi, jakby na nas czekali…
341. [Rozdziały, etapy i zdolności Dantego [10110] — tytuł] 8급 해결사
   źródło: StageNode1-1.json :: dataList[id=10110].title
   limit: do 40 znaków
   EN: Grade 8 Fixers
   PL: Fikserzy 8. stopnia
342. [Rozdziały, etapy i zdolności Dantego [10110] — miejsce] 4구 로보토미 지부 앞
   źródło: StageNode1-1.json :: dataList[id=10110].place
   (powtórzenie elementu 339 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
343. [Rozdziały, etapy i zdolności Dantego [10110] — opis] 로보토미 지부 안으로 들어가기 직전, 베르길리우스가 갑자기 은밀하게 나를 부른다. 단둘이 할 말이 있는 낌새인 것 같다.
   źródło: StageNode1-1.json :: dataList[id=10110].desc
   limit: do 170 znaków
   EN: Just before we entered the LC branch facility, Vergilius stopped me all of a sudden. It seems he has something to say to me alone.
   PL: Tuż przed wejściem do filii L Corp. Vergilius nagle dyskretnie mnie przywołał. Wygląda na to, że chce ze mną porozmawiać w cztery oczy.
344. [Rozdziały, etapy i zdolności Dantego [10111] — tytuł] D-02 지부
   źródło: StageNode1-1.json :: dataList[id=10111].title
   limit: do 40 znaków
   EN: Branch D-02
   PL: Filia D-02
345. [Rozdziały, etapy i zdolności Dantego [10111] — miejsce] 4구 로보토미 지부 어딘가
   źródło: StageNode1-1.json :: dataList[id=10111].place
   limit: do 50 znaków
   EN: District 4 - LC Branch Interior
   PL: Dystrykt 4 - gdzieś w filii L Corp.
346. [Rozdziały, etapy i zdolności Dantego [10111] — opis] 우리는 지하로 내려갔다. 시체들이 즐비해 있는 이곳은 악취와 벌레들이 상당했다. 이 곳에 무슨 일이 있었던 걸까? 그리고 우리는 과연 황금가지를 무사히 탈환해올 수 있는 걸까?
   źródło: StageNode1-1.json :: dataList[id=10111].desc
   limit: do 250 znaków
   EN: We descended into a fetid underground facility. The place was lined with corpses and critters. Just what happened here? And can we come back in one piece with the Golden Bough in our hands?
   PL: Zeszliśmy pod ziemię. W tym miejscu, usłanym trupami, panował straszny smród i roiło się od robactwa. Co tu się wydarzyło? I czy zdołamy bez szwanku odbić Złotą Gałąź?

## Rozdziały, etapy i zdolności Dantego: StageNode1-2
- plik gry: `StageNode1-2.json`

347. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 카지노
   źródło: StageNode1-2.json :: dataList[id=10201].title
   limit: do 40 znaków
   EN: Casino
   PL: Kasyno
348. [Rozdziały, etapy i zdolności Dantego [10201] — miejsce] 2-1스테이지장소
   źródło: StageNode1-2.json :: dataList[id=10201].place
   limit: do 40 znaków
   EN: Stage 2-1 Location
   PL: Miejsce etapu 2-1
349. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 싸늘해진 공기 속 베르길리우스는 다음 작전을 위한 장소에 대해 설명한다.\n이번 황금가지가 있는 곳은 어디일까?
   źródło: StageNode1-2.json :: dataList[id=10201].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Under the chill air, Vergilius introduces us to our upcoming destination.\nWhere could the next Golden Bough be?
   PL: Gdy atmosfera stężała, Vergilius opisuje miejsce następnej operacji.\nGdzie tym razem jest Złota Gałąź?
350. [Rozdziały, etapy i zdolności Dantego [10202] — tytuł] 전당포
   źródło: StageNode1-2.json :: dataList[id=10202].title
   limit: do 40 znaków
   EN: The Pawnshop
   PL: Lombard
351. [Rozdziały, etapy i zdolności Dantego [10202] — miejsce] 전당포 거리 안
   źródło: StageNode1-2.json :: dataList[id=10202].place
   limit: do 40 znaków
   EN: Pawn Avenue
   PL: Na Ulicy Lombardów
352. [Rozdziały, etapy i zdolności Dantego [10202] — opis] 파우스트는 이번 작전에 대한 계획을 설명한다. \n임무 수행을 위해 우리가 가야 할 곳은 '전당포'다.
   źródło: StageNode1-2.json :: dataList[id=10202].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Faust explains what to do for this mission:\nAs our first step, we should pay a visit to a certain “pawnshop”.
   PL: Faust przedstawia plan operacji.\nŻeby wykonać zadanie, musimy pójść do “lombardu”.
353. [Rozdziały, etapy i zdolności Dantego [10203] — tytuł] 완벽한 작전
   źródło: StageNode1-2.json :: dataList[id=10203].title
   limit: do 40 znaków
   EN: A Flawless Plan
   PL: Doskonały plan
354. [Rozdziały, etapy i zdolności Dantego [10203] — miejsce] 전당포 거리 안
   źródło: StageNode1-2.json :: dataList[id=10203].place
   (powtórzenie elementu 351 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
355. [Rozdziały, etapy i zdolności Dantego [10203] — opis] 합동 작전을 위해 클리어 부서로부터 새로운 인물들이 등장했다.\n누군가들과는 달리 똑 부러지는 그들의 모습에 수감자들은 잔뜩 경계하게 되는데…
   źródło: StageNode1-2.json :: dataList[id=10203].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Our team will join hands with a duo from the Clearance Department.\nThe Sinners cast a skeptical glance at their competence and comportment…
   PL: Do wspólnej operacji dołączyły nowe osoby z Działu Sprzątania.\nW przeciwieństwie do niektórych są konkretni i bystrzy, więc Grzesznicy patrzą na nich mocno podejrzliwie…
356. [Rozdziały, etapy i zdolności Dantego [10204] — tytuł] 버러지
   źródło: StageNode1-2.json :: dataList[id=10204].title
   limit: do 40 znaków
   EN: Louse
   PL: Wszy
357. [Rozdziały, etapy i zdolności Dantego [10204] — miejsce] 전당포 거리 안
   źródło: StageNode1-2.json :: dataList[id=10204].place
   (powtórzenie elementu 351 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
358. [Rozdziały, etapy i zdolności Dantego [10204] — opis] 완벽해보였던 작전도 잠시, 역시나 계획은 꼬이게 된다.\n돈키호테의 돌발 행동으로 인해 수감자들은 콩콩이 파 일당들과 맞닥뜨리게 되는데…
   źródło: StageNode1-2.json :: dataList[id=10204].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The plan that seemed so perfect took little time to go awry.\nDon Quixote’s outburst runs us afoul with the Tingtang Gang…
   PL: Plan wydawał się doskonały, ale nie na długo: jak zwykle wszystko się posypało.\nPrzez wybryk Don Quixote Grzesznicy wpadają na ludzi z gangu Tingtang…
359. [Rozdziały, etapy i zdolności Dantego [10205] — tytuł] 우리들은 림버...
   źródło: StageNode1-2.json :: dataList[id=10205].title
   limit: do 40 znaków
   EN: Soldiers of Limbu―
   PL: Jesteśmy z Limbu…
360. [Rozdziały, etapy i zdolności Dantego [10205] — miejsce] 10구 뒷골목 어딘가
   źródło: StageNode1-2.json :: dataList[id=10205].place
   limit: do 50 znaków
   EN: Some Backstreets of District 10
   PL: Gdzieś w Zaułkach Dystryktu 10
361. [Rozdziały, etapy i zdolności Dantego [10205] — opis] 콩콩이 파 일당들과 계속 교전을 벌이는 중인 수감자들. 이 일대는 전부 콩콩이 파의 구역이었는지 적들은 끊임없이 등장한다.
   źródło: StageNode1-2.json :: dataList[id=10205].desc
   limit: do 170 znaków
   EN: The Sinners continue to fight off the Tingtang Gang’s goons. They just keep on appearing, suggesting that we’re in their territory.
   PL: Grzesznicy wciąż ścierają się z tingtangowcami. Wrogowie wyrastają bez końca, jakby cała okolica należała do gangu Tingtang.
362. [Rozdziały, etapy i zdolności Dantego [10206] — tytuł] 차 탑
   źródło: StageNode1-2.json :: dataList[id=10206].title
   limit: do 40 znaków
   EN: Towering Cars
   PL: Wieża z aut
363. [Rozdziały, etapy i zdolności Dantego [10206] — miejsce] 10구 뒷골목 어딘가
   źródło: StageNode1-2.json :: dataList[id=10206].place
   (powtórzenie elementu 360 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
364. [Rozdziały, etapy i zdolności Dantego [10206] — opis] 콩콩이 파 조직원으로부터 콩콩이 파 보스는 차 탑에 있다는 정보를 들었다. \nB 플랜을 위해 우리는 차 탑으로 가서 소망력을 빼앗고 콩콩이 파 조직원으로 위장해야 한다.
   źródło: StageNode1-2.json :: dataList[id=10206].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We learned from a Tingtanger that their boss is at the scrapyard housing car pagodas.\nFor our Plan B, we must take wishpower from the gang and borrow their clothes.
   PL: Od tingtangowca dowiedzieliśmy się, że szef gangu jest przy wieży z aut.\nW ramach planu B musimy tam pójść, odebrać im Moc Życzeń i przebrać się za tingtangowców.
365. [Rozdziały, etapy i zdolności Dantego [10207] — tytuł] 소망통
   źródło: StageNode1-2.json :: dataList[id=10207].title
   limit: do 40 znaków
   EN: Wish Canister
   PL: Kanister życzeń
366. [Rozdziały, etapy i zdolności Dantego [10207] — miejsce] 10구 뒷골목 어딘가
   źródło: StageNode1-2.json :: dataList[id=10207].place
   (powtórzenie elementu 360 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
367. [Rozdziały, etapy i zdolności Dantego [10207] — opis] 콩콩이 파 보스를 찾기 위해 우리는 계속 차 탑 일대를 뒤지고 있다.
   źródło: StageNode1-2.json :: dataList[id=10207].desc
   limit: do 120 znaków
   EN: The team searches around the car pagodas looking for the Tingtang Gang’s boss.
   PL: Przeczesujemy okolice wieży z aut w poszukiwaniu szefa gangu Tingtang.
368. [Rozdziały, etapy i zdolności Dantego [10208] — tytuł] 슬롯머신
   źródło: StageNode1-2.json :: dataList[id=10208].title
   limit: do 40 znaków
   EN: Slot Machines
   PL: Automaty do gry
369. [Rozdziały, etapy i zdolności Dantego [10208] — miejsce] 카지노 1층
   źródło: StageNode1-2.json :: dataList[id=10208].place
   limit: do 40 znaków
   EN: Casino 1F
   PL: Kasyno - poziom 1
370. [Rozdziały, etapy i zdolności Dantego [10208] — opis] 우여곡절 끝에 콩콩이 파들에게 옷을 빼앗고 카지노에 진입했다. 이번에야말로 반드시 작전을 성공시키리.
   źródło: StageNode1-2.json :: dataList[id=10208].desc
   limit: do 190 znaków
   EN: After a series of scuffles, we relieved the Tingtang Gang of their outfits and made our way into the casino. This time, we’ll succeed for sure.
   PL: Po wielu perypetiach odebraliśmy tingtangowcom ubrania i weszliśmy do kasyna. Tym razem operacja musi się udać.
371. [Rozdziały, etapy i zdolności Dantego [10209] — tytuł] 퍼포먼스
   źródło: StageNode1-2.json :: dataList[id=10209].title
   limit: do 40 znaków
   EN: A Performance
   PL: Performans
372. [Rozdziały, etapy i zdolności Dantego [10209] — miejsce] 카지노 1층
   źródło: StageNode1-2.json :: dataList[id=10209].place
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
373. [Rozdziały, etapy i zdolności Dantego [10209] — opis] 굳은 다짐은 순식간에 사그라들며 보기좋게 작전은 꼬여간다. 앞으로 넘어야 할 산은 많지만 카지노 경호원들의 눈에 띄어 버렸다.
   źródło: StageNode1-2.json :: dataList[id=10209].desc
   limit: do 250 znaków
   EN: Our newfound determination is swept away in a torrent of glitter, along with our backup plan. There are plenty of obstacles to overcome—particularly the security guards who just noticed us.
   PL: Niezłomne postanowienie rozwiało się w okamgnieniu, a operacja pięknie się posypała. Przed nami jeszcze wiele przeszkód, a tymczasem wpadliśmy w oko ochronie kasyna.
374. [Rozdziały, etapy i zdolności Dantego [10210] — tytuł] 모.분
   źródło: StageNode1-2.json :: dataList[id=10210].title
   limit: do 40 znaków
   EN: S.Y.N.C.
   PL: U.K.
375. [Rozdziały, etapy i zdolności Dantego [10210] — miejsce] 카지노 2층
   źródło: StageNode1-2.json :: dataList[id=10210].place
   limit: do 40 znaków
   EN: Casino 2F
   PL: Kasyno - poziom 2
376. [Rozdziały, etapy i zdolności Dantego [10210] — opis] 카지노 2층으로 넘어갔다. 이곳에선 또 어떤 일이 우리를 기다리고 있을지 아찔해진다.
   źródło: StageNode1-2.json :: dataList[id=10210].desc
   limit: do 120 znaków
   EN: We reached the second floor of the casino. It makes me dizzy imagining what troubles await.
   PL: Przeszliśmy na poziom 2 kasyna. Aż mi się kręci w głowie na myśl o tym, co tu na nas czeka.
377. [Rozdziały, etapy i zdolności Dantego [10211] — tytuł] 모.분 2
   źródło: StageNode1-2.json :: dataList[id=10211].title
   limit: do 40 znaków
   EN: Let That S.Y.N.C. In
   PL: U.K. 2
378. [Rozdziały, etapy i zdolności Dantego [10211] — miejsce] 카지노 2층
   źródło: StageNode1-2.json :: dataList[id=10211].place
   (powtórzenie elementu 375 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
379. [Rozdziały, etapy i zdolności Dantego [10211] — opis] 이곳을 접수하고 있는 다른 조직들과 맞닥뜨리게 되었다.
   źródło: StageNode1-2.json :: dataList[id=10211].desc
   limit: do 120 znaków
   EN: We encountered another Syndicate that has a stake in this casino.
   PL: Natknęliśmy się na inne organizacje, które opanowały to miejsce.
380. [Rozdziały, etapy i zdolności Dantego [10212] — tytuł] 춤사위
   źródło: StageNode1-2.json :: dataList[id=10212].title
   limit: do 40 znaków
   EN: Baile y Rola
   PL: Porywający taniec
381. [Rozdziały, etapy i zdolności Dantego [10212] — miejsce] 카지노 2층
   źródło: StageNode1-2.json :: dataList[id=10212].place
   (powtórzenie elementu 375 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
382. [Rozdziały, etapy i zdolności Dantego [10212] — opis] 1층과는 달리 굉장히 흥겨워 보이는 공기가 느껴진다. 무엇보다 테이블마다 정체 모를 악기들이 놓여있다. 이것들의 용도는 대체 뭐지?
   źródło: StageNode1-2.json :: dataList[id=10212].desc
   limit: do 210 znaków
   EN: The enthusiasm is in stark contrast to the atmosphere just a floor below. One can find a series of unknown musical instruments on every table. What are they for?
   PL: W przeciwieństwie do poziomu 1 panuje tu wyjątkowo radosna atmosfera. A przede wszystkim na każdym stole leżą jakieś dziwne instrumenty. Do czego one, u licha, służą?
383. [Rozdziały, etapy i zdolności Dantego [10213] — tytuł] 환영 인사
   źródło: StageNode1-2.json :: dataList[id=10213].title
   limit: do 40 znaków
   EN: A Warm Welcome
   PL: Powitanie
384. [Rozdziały, etapy i zdolności Dantego [10213] — miejsce] 카지노 3층
   źródło: StageNode1-2.json :: dataList[id=10213].place
   limit: do 40 znaków
   EN: Casino 3F
   PL: Kasyno - poziom 3
385. [Rozdziały, etapy i zdolności Dantego [10213] — opis] 싱클레어의 놀라운 활약으로 인해 우리는 3층으로 무사히 올라갔다. 하지만 한 눈에 보기에도 흉악하기 그지없어 보이는 다른 조직원이 우리를 환영해주고 있었다.
   źródło: StageNode1-2.json :: dataList[id=10213].desc
   limit: do 200 znaków
   EN: Thanks to Sinclair’s astonishing performance, we could reach the third floor. Our joy was short-lived as an imposing Syndicate was waiting for us there.
   PL: Dzięki zdumiewającemu popisowi Sinclaira bez szwanku dostaliśmy się na poziom 3. Ale tam witali nas już członkowie innej organizacji, z wyglądu wyjątkowo groźni.
386. [Rozdziały, etapy i zdolności Dantego [10214] — tytuł] 환영 인사 2
   źródło: StageNode1-2.json :: dataList[id=10214].title
   limit: do 40 znaków
   EN: An Overstayed Welcome
   PL: Powitanie 2
387. [Rozdziały, etapy i zdolności Dantego [10214] — miejsce] 카지노 3층
   źródło: StageNode1-2.json :: dataList[id=10214].place
   (powtórzenie elementu 384 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
388. [Rozdziały, etapy i zdolności Dantego [10214] — opis] 싱클레어의 놀라운 활약으로 인해 우리는 3층으로 무사히 올라갔다. 하지만 한 눈에 보기에도 흉악하기 그지없어 보이는 다른 조직원이 우리를 환영해주고 있었다.
   źródło: StageNode1-2.json :: dataList[id=10214].desc
   (powtórzenie elementu 385 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
389. [Rozdziały, etapy i zdolności Dantego [10215] — tytuł] 주둥이
   źródło: StageNode1-2.json :: dataList[id=10215].title
   limit: do 40 znaków
   EN: Gobsmack
   PL: Ozór
390. [Rozdziały, etapy i zdolności Dantego [10215] — miejsce] 카지노 3층
   źródło: StageNode1-2.json :: dataList[id=10215].place
   (powtórzenie elementu 384 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
391. [Rozdziały, etapy i zdolności Dantego [10215] — opis] 철공회 조직원들의 계속되는 교전으로 수감자들은 점점 지쳐간다. 하지만 그보다 더 견딜 수 없었던 건 바로…
   źródło: StageNode1-2.json :: dataList[id=10215].desc
   limit: do 140 znaków
   EN: The Sinners were growing weary from the prolonged encounter with the Tieqiu Crew. One of them in particular…
   PL: Grzesznicy coraz bardziej opadają z sił w ciągłych starciach z Ekipą Tieqiu. Ale jeszcze trudniej było znieść…
392. [Rozdziały, etapy i zdolności Dantego [10216] — tytuł] 선수 입장
   źródło: StageNode1-2.json :: dataList[id=10216].title
   limit: do 40 znaków
   EN: Contestants
   PL: Wejście zawodniczki
393. [Rozdziały, etapy i zdolności Dantego [10216] — miejsce] 카지노 꼭대기층
   źródło: StageNode1-2.json :: dataList[id=10216].place
   limit: do 40 znaków
   EN: High Rollers Floor
   PL: Kasyno - najwyższe piętro
394. [Rozdziały, etapy i zdolności Dantego [10216] — opis] 뜻하지 않은 료슈의 교습으로 인해 우리까지 상당한 정신 피해를 입은 채 꼭대기 층으로 갔다. 이제 이곳에서 황금가지를 걸고 도박을 벌여야 한다.
   źródło: StageNode1-2.json :: dataList[id=10216].desc
   limit: do 220 znaków
   EN: Ryōshū’s unexpected lesson in incredible violence opened a way to the top floor at the cost of our inner peace. Now we must win the Golden Bough in a game of chance.
   PL: Przez niespodziewaną lekcję Ryōshū i my odnieśliśmy spore szkody psychiczne, ale dotarliśmy na najwyższe piętro. Teraz musimy tu zagrać o Złotą Gałąź.
395. [Rozdziały, etapy i zdolności Dantego [10217] — tytuł] 동작 그만
   źródło: StageNode1-2.json :: dataList[id=10217].title
   limit: do 40 znaków
   EN: Stop Right There
   PL: Stój no
396. [Rozdziały, etapy i zdolności Dantego [10217] — miejsce] 카지노 꼭대기층
   źródło: StageNode1-2.json :: dataList[id=10217].place
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
397. [Rozdziały, etapy i zdolności Dantego [10217] — opis] 로쟈가 우리들의 대표로 도박 게임에 참가했다. 어느덧 도박은 마지막 판을 앞두고 있다.
   źródło: StageNode1-2.json :: dataList[id=10217].desc
   limit: do 120 znaków
   EN: Rodya nominated herself to play the game. The table was reaching its final round.
   PL: Rodion wzięła udział w grze jako nasza reprezentantka. Rozgrywka zbliża się do ostatniego rozdania.
398. [Rozdziały, etapy i zdolności Dantego [10218] — tytuł] 승자
   źródło: StageNode1-2.json :: dataList[id=10218].title
   limit: do 40 znaków
   EN: The Winner
   PL: Zwycięzca
399. [Rozdziały, etapy i zdolności Dantego [10218] — miejsce] 카지노 꼭대기층
   źródło: StageNode1-2.json :: dataList[id=10218].place
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
400. [Rozdziały, etapy i zdolności Dantego [10218] — opis] 대체 도박장 안에 무슨 일이 일어나는 건지 궁금증을 참을 수 없던 우리들은 대화를 엿듣다가 안으로 들어오게 되었다. 방 안은 잔뜩 튀어있는 피, 흔적만 겨우 남은 철공회 보스, 그리고 우리를 보며 잔잔히 웃고 있는 소냐 라는 자가 보였다.
   źródło: StageNode1-2.json :: dataList[id=10218].desc
   limit: do 270 znaków
   EN: Curious to know what was happening, we eavesdropped on the table. We barge in by accident to find a spatter of blood, the compressed remains of the Tieqiu Boss, and a man named Sonya giving us a soft smile.
   PL: Nie mogąc powstrzymać ciekawości, co się dzieje przy stole, podsłuchiwaliśmy i w końcu weszliśmy do środka. Ujrzeliśmy wszędzie bryzgi krwi, ślady, które zostały z Szefa Ekipy Tieqiu, i niejakiego Sonyę, który łagodnie się do nas uśmiechał.
401. [Rozdziały, etapy i zdolności Dantego [10219] — tytuł] J-03 지부
   źródło: StageNode1-2.json :: dataList[id=10219].title
   limit: do 40 znaków
   EN: Branch J-03
   PL: Filia J-03
402. [Rozdziały, etapy i zdolności Dantego [10219] — miejsce] 카지노 꼭대기층
   źródło: StageNode1-2.json :: dataList[id=10219].place
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
403. [Rozdziały, etapy i zdolności Dantego [10219] — opis] 도박은 로쟈의 승리로 끝났다. 우리는 이제 본격적으로 황금가지를 찾기 위해 지하로 내려가야 한다.
   źródło: StageNode1-2.json :: dataList[id=10219].desc
   limit: do 150 znaków
   EN: Rodya emerged victorious. Now we must descend to the underground floors to lay our claim on the Golden Bough.
   PL: Gra zakończyła się zwycięstwem Rodion. Teraz musimy zejść pod ziemię i na dobre zabrać się do szukania Złotej Gałęzi.

## Rozdziały, etapy i zdolności Dantego: StageNode1-3
- plik gry: `StageNode1-3.json`

404. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 흥얼거림
   źródło: StageNode1-3.json :: dataList[id=10301].title
   limit: do 40 znaków
   EN: Humming Along
   PL: Nucenie
405. [Rozdziały, etapy i zdolności Dantego [10301] — miejsce] 메피스토펠레스 안
   źródło: StageNode1-3.json :: dataList[id=10301].place
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 베르길리우스가 이번 작전의 목적지를 안내한다. 모두가 화기애애했던 분위기 속에서 유독 한 수감자만 심상치 않은 반응을 보이기 시작하는데…
   źródło: StageNode1-3.json :: dataList[id=10301].desc
   limit: do 180 znaków
   EN: Vergilius informs us of where we will be going next. While everyone seems happy and energetic, one Sinner is reacting rather strangely…
   PL: Vergilius przedstawia cel tej operacji. Wszyscy są w świetnych humorach, tylko jeden z Grzeszników zaczyna reagować dziwnie niespokojnie…
407. [Rozdziały, etapy i zdolności Dantego [10302] — tytuł] 심사
   źródło: StageNode1-3.json :: dataList[id=10302].title
   limit: do 40 znaków
   EN: Inspection
   PL: Kontrola
408. [Rozdziały, etapy i zdolności Dantego [10302] — miejsce] K사 검문소 길목
   źródło: StageNode1-3.json :: dataList[id=10302].place
   limit: do 40 znaków
   EN: Road to K Corp. Checkpoint
   PL: Droga do punktu kontrolnego K Corp.
409. [Rozdziały, etapy i zdolności Dantego [10302] — opis] 우리는 K사 둥지로 간다고 한다. 하지만 다들 반응이 하나 같이 놀랍다는 말투다. 둥지로 가기 위해서는 검문소를 거쳐야 한다는데 절차가 매우 까다로운 모양이다.
   źródło: StageNode1-3.json :: dataList[id=10302].desc
   limit: do 220 znaków
   EN: To everyone’s surprise, we’re told that our destination is K Corp’s Nest. The entry procedures one must go through to set foot in a Nest are supposedly quite complicated.
   PL: Podobno jedziemy do Gniazda K Corp. Wszyscy reagują na to tak samo zdumieni. Żeby dostać się do Gniazda, trzeba przejść przez punkt kontrolny, a procedury są tam ponoć bardzo drobiazgowe.
410. [Rozdziały, etapy i zdolności Dantego [10303] — tytuł] 코드 퍼플
   źródło: StageNode1-3.json :: dataList[id=10303].title
   limit: do 40 znaków
   EN: Code Purple
   PL: Kod purpurowy
411. [Rozdziały, etapy i zdolności Dantego [10303] — miejsce] K사 검문소
   źródło: StageNode1-3.json :: dataList[id=10303].place
   limit: do 40 znaków
   EN: K Corp. Checkpoint
   PL: Punkt kontrolny K Corp.
412. [Rozdziały, etapy i zdolności Dantego [10303] — opis] 베르길리우스와 이스마엘의 철저한 사전 연습 끝에 우리는 심사대 바로 앞까지 도착했다. 이대로 무사히 통과가 된다면 좋으련만…
   źródło: StageNode1-3.json :: dataList[id=10303].desc
   limit: do 190 znaków
   EN: We wait our turn to undergo the checkpoint official’s interview, with Vergilius and Ishmael instructing us on the process. Here’s hoping we’ll pass…
   PL: Po gruntownych próbach pod okiem Vergiliusa i Ishmael dotarliśmy tuż przed stanowisko kontroli. Gdybyśmy tylko przeszli bez przeszkód…
413. [Rozdziały, etapy i zdolności Dantego [10304] — tytuł] 금기
   źródło: StageNode1-3.json :: dataList[id=10304].title
   limit: do 40 znaków
   EN: Taboo
   PL: Tabu
414. [Rozdziały, etapy i zdolności Dantego [10304] — miejsce] K사 검문소
   źródło: StageNode1-3.json :: dataList[id=10304].place
   (powtórzenie elementu 411 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [Rozdziały, etapy i zdolności Dantego [10304] — opis] 불의를 참지 못하는 우리의 돈키호테가 또다시 일을 저질러 버렸다. K사 둥지 한복판에서 사방에서 직원들이 몰려오기 시작하고 베르길리우스는 단단히 화가 난 듯 팔짱을 끼고 가만히 구경하기 시작했다.
   źródło: StageNode1-3.json :: dataList[id=10304].desc
   limit: do 300 znaków
   EN: Our Dear Don Quixote’s intolerance for injustice rears its troublesome head again. Armed staff from K Corp. surround us on all sides, all the while Vergilius watches with his arms crossed, upset at our repeated failures to behave.
   PL: Nasza Don Quixote, która nie znosi niesprawiedliwości, znów narozrabiała. W samym środku Gniazda K Corp. ze wszystkich stron zbiegają się pracownicy, a Vergilius, najwyraźniej porządnie zły, skrzyżował ręce i przygląda się w milczeniu.
416. [Rozdziały, etapy i zdolności Dantego [10305] — tytuł] 금기 2
   źródło: StageNode1-3.json :: dataList[id=10305].title
   limit: do 40 znaków
   EN: Verboten
   PL: Tabu 2
417. [Rozdziały, etapy i zdolności Dantego [10305] — miejsce] K사 검문소
   źródło: StageNode1-3.json :: dataList[id=10305].place
   (powtórzenie elementu 411 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Rozdziały, etapy i zdolności Dantego [10305] — opis] 우리는 계속 K사 경비들과 싸우는 중이다. 적들은 타격이 거의 없어 보이고… 우리는 점점 지쳐간다.
   źródło: StageNode1-3.json :: dataList[id=10305].desc
   limit: do 140 znaków
   EN: The confrontation with K Corp’s guards continues. They seem to hardly take a scratch… adding to our fatigue.
   PL: Wciąż walczymy ze strażnikami K Corp. Wrogowie zdają się prawie nie odnosić obrażeń… a my słabniemy coraz bardziej.
419. [Rozdziały, etapy i zdolności Dantego [10306] — tytuł] HP 탄
   źródło: StageNode1-3.json :: dataList[id=10306].title
   limit: do 40 znaków
   EN: HP Bullets
   PL: Pociski HP
420. [Rozdziały, etapy i zdolności Dantego [10306] — miejsce] K사 검문소
   źródło: StageNode1-3.json :: dataList[id=10306].place
   (powtórzenie elementu 411 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
421. [Rozdziały, etapy i zdolności Dantego [10306] — opis] K사의 특이점인 HP탄의 기술로 인해 우리가 적군에게 간신히 입힌 치명상들은 눈 깜짝할 새에 회복된다. 수감자들의 인내심은 점점 바닥나간다.
   źródło: StageNode1-3.json :: dataList[id=10306].desc
   limit: do 180 znaków
   EN: HP Bullets infused with K Corp’s Singularity render all damage we inflict on our foes useless. The Sinners are running out of patience.
   PL: Dzięki pociskom HP, Osobliwości K Corp., śmiertelne rany, które z trudem zadajemy wrogom, goją się w mgnieniu oka. Grzesznikom kończy się cierpliwość.
422. [Rozdziały, etapy i zdolności Dantego [10307] — tytuł] 지크프리트
   źródło: StageNode1-3.json :: dataList[id=10307].title
   limit: do 40 znaków
   EN: Siegfried
   PL: Siegfried
423. [Rozdziały, etapy i zdolności Dantego [10307] — miejsce] K사 검문소
   źródło: StageNode1-3.json :: dataList[id=10307].place
   (powtórzenie elementu 411 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [Rozdziały, etapy i zdolności Dantego [10307] — opis] 밖에서부터 엄청난 속도로 돌진하는 자가 보인다. 지나칠 정도로 경쾌하고 과하게 쾌활한 그의 이름은 지크프리트라고 한다. 베르길리우스와는 안면이 있는 사이인 듯 인사를 나누더니 수감자들을 향해 순식간에 달려들기 시작한다.
   źródło: StageNode1-3.json :: dataList[id=10307].desc
   limit: do 300 znaków
   EN: A man approaches from outside with tremendous speed. This exceedingly jovial and uncomfortably energetic fellow is Siegfried, who appears to have an acquaintance with Vergilius; after a friendly exchange, he rushes at our Sinners.
   PL: Ktoś pędzi ku nam z zewnątrz z zawrotną prędkością. Ten aż przesadnie żwawy i nadmiernie radosny jegomość nazywa się Siegfried. Wymienia pozdrowienia z Vergiliusem, jakby się znali, po czym w okamgnieniu rzuca się na Grzeszników.
425. [Rozdziały, etapy i zdolności Dantego [10308] — tytuł] 다시 에피,소드
   źródło: StageNode1-3.json :: dataList[id=10308].title
   limit: do 40 znaków
   EN: Effie—Saude, too
   PL: Znów Effie-zod. I Saude
426. [Rozdziały, etapy i zdolności Dantego [10308] — miejsce] K사 검문소 바깥
   źródło: StageNode1-3.json :: dataList[id=10308].place
   limit: do 40 znaków
   EN: Road to K Corp. Checkpoint
   PL: Przed punktem kontrolnym K Corp.
427. [Rozdziały, etapy i zdolności Dantego [10308] — opis] 정신없는 지크프리트와의 첫 만남 후, 검문소 앞에서 낯익은 얼굴들을 만났다. 여전히 의기양양하게 인사를 건네는 그들은…
   źródło: StageNode1-3.json :: dataList[id=10308].desc
   limit: do 190 znaków
   EN: After a chaotic encounter with Siegfried, we meet with a couple of familiar faces at the exit, greeting us with the same confidence and comportment…
   PL: Po chaotycznym pierwszym spotkaniu z Siegfriedem natknęliśmy się przed punktem kontrolnym na znajome twarze. Wciąż tak samo pewni siebie, witają nas…
428. [Rozdziały, etapy i zdolności Dantego [10309] — tytuł] 그날의 거래
   źródło: StageNode1-3.json :: dataList[id=10309].title
   limit: do 40 znaków
   EN: The Deal They Struck
   PL: Umowa z tamtego dnia
429. [Rozdziały, etapy i zdolności Dantego [10309] — miejsce] 메피스토펠레스 안
   źródło: StageNode1-3.json :: dataList[id=10309].place
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [Rozdziały, etapy i zdolności Dantego [10309] — opis] 버스로 복귀했지만, 분위기가 어딘가 좋지 않다. 아마 베르길리우스는 이 일을 그냥 넘기지 않으려는 모양이다. 힘내라, 돈키호테…!
   źródło: StageNode1-3.json :: dataList[id=10309].desc
   limit: do 210 znaków
   EN: Returning to the bus, I sense an uneasiness in the air. It looks like Vergilius isn’t going to let today’s incident go unpunished. Buena suerte, Don Quixote…!
   PL: Wróciliśmy do autobusu, ale atmosfera jest jakaś nieprzyjemna. Vergilius chyba nie zamierza puścić tego płazem. Trzymaj się, Don Quixote…!
431. [Rozdziały, etapy i zdolności Dantego [10310] — tytuł] 이단 심문관
   źródło: StageNode1-3.json :: dataList[id=10310].title
   limit: do 40 znaków
   EN: Inquisitors
   PL: Inkwizytorzy
432. [Rozdziały, etapy i zdolności Dantego [10310] — miejsce] 칼프 마을 입구
   źródło: StageNode1-3.json :: dataList[id=10310].place
   limit: do 40 znaków
   EN: Calw - Town Entrance
   PL: Wjazd do Calw
433. [Rozdziały, etapy i zdolności Dantego [10310] — opis] 한차례의 소동이 마무리되고 우리는 드디어 목적지를 향해 출발한다. K사의 '칼프'라는 곳으로 가는 길, 잠깐의 평화로움을 맛보기도 전에 자신을 '이단심문관'이라고 소개하는 이들에 의해 버스의 유리창이 꿰뚫린다.
   źródło: StageNode1-3.json :: dataList[id=10310].desc
   limit: do 270 znaków
   EN: With everything sorted out, we finally resume our journey to the town of Calw. Before we can bask in our momentary peace, someone claiming to be an “inquisitor” leaves a hole in the back window of our bus.
   PL: Zamieszanie dobiegło końca i wreszcie ruszamy do celu. W drodze do miejsca zwanego Calw, w K Corp., zanim zdążyliśmy nacieszyć się chwilą spokoju, ludzie przedstawiający się jako “Inkwizytorzy” przebili szybę autobusu.
434. [Rozdziały, etapy i zdolności Dantego [10311] — tytuł] 이단 심문관 2
   źródło: StageNode1-3.json :: dataList[id=10311].title
   limit: do 40 znaków
   EN: Inquisitors 2
   PL: Inkwizytorzy 2
435. [Rozdziały, etapy i zdolności Dantego [10311] — miejsce] 칼프 마을 입구
   źródło: StageNode1-3.json :: dataList[id=10311].place
   (powtórzenie elementu 432 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Rozdziały, etapy i zdolności Dantego [10311] — opis] 선발대로부터 연락이 왔다. 무전기에서부터 들려오는 정체불명의 목소리는 심상치 않은 일이 벌어지고 있다는 걸 암시하고 있었다. 싱클레어는 겁에 질리기 시작했다.
   źródło: StageNode1-3.json :: dataList[id=10311].desc
   limit: do 230 znaków
   EN: The advance party contacted us at last. The mysterious voice coming from the transmitter was a telltale sign that something was up, throwing Sinclair into another fit of terror.
   PL: Odezwała się grupa zwiadowcza. Nieznany głos z krótkofalówki zdradzał, że dzieje się coś niedobrego. Sinclair zaczął wpadać w przerażenie.
437. [Rozdziały, etapy i zdolności Dantego [10312] — tytuł] 이단 심문관 3
   źródło: StageNode1-3.json :: dataList[id=10312].title
   limit: do 40 znaków
   EN: Inquisitors 3
   PL: Inkwizytorzy 3
438. [Rozdziały, etapy i zdolności Dantego [10312] — miejsce] 칼프 마을 입구
   źródło: StageNode1-3.json :: dataList[id=10312].place
   (powtórzenie elementu 432 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
439. [Rozdziały, etapy i zdolności Dantego [10312] — opis] 이단 심문관들이 계속해서 밀려든다. 아무렇지 않게 내 머리를 내어오라는 저들은 대체 뭐 하는 놈들일까.
   źródło: StageNode1-3.json :: dataList[id=10312].desc
   limit: do 140 znaków
   EN: Groups of Inquisitors continue to assail us. Who are they, and why are they so fixated on taking my head?
   PL: Inkwizytorzy nacierają raz za razem. Co to za jedni, że ot tak żądają mojej głowy?
440. [Rozdziały, etapy i zdolności Dantego [10313] — tytuł] 거룩한 밤
   źródło: StageNode1-3.json :: dataList[id=10313].title
   limit: do 40 znaków
   EN: Silent Night
   PL: Święta noc
441. [Rozdziały, etapy i zdolności Dantego [10313] — miejsce] 칼프 마을 안
   źródło: StageNode1-3.json :: dataList[id=10313].place
   limit: do 40 znaków
   EN: Town of Calw
   PL: W Calw
442. [Rozdziały, etapy i zdolności Dantego [10313] — opis] 목적지인 '칼프' 마을로 도착했다. 마을 어딘가에서부터 익숙한 노래가 들려오며, 나무 곳곳에는 끔찍한 장신구들이 주렁주렁 달려 있다.
   źródło: StageNode1-3.json :: dataList[id=10313].desc
   limit: do 170 znaków
   EN: We’ve reached the town of Calw. A familiar song welcomes us, followed by the morbid sight of trees festooned with horrifying things.
   PL: Dotarliśmy do celu, do miasteczka Calw. Skądś dobiega znajoma piosenka, a na drzewach gęsto wiszą potworne ozdoby.
443. [Rozdziały, etapy i zdolności Dantego [10314] — tytuł] 거룩한 밤 2
   źródło: StageNode1-3.json :: dataList[id=10314].title
   limit: do 40 znaków
   EN: Holy Night
   PL: Święta noc 2
444. [Rozdziały, etapy i zdolności Dantego [10314] — miejsce] 칼프 마을 안
   źródło: StageNode1-3.json :: dataList[id=10314].place
   (powtórzenie elementu 441 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
445. [Rozdziały, etapy i zdolności Dantego [10314] — opis] 싱클레어의 고향인 '칼프' 마을은 주민들 대부분이 의체 부품 제작에 종사하고 있는 마을이었다. 뒤틀림 현상이 잦아질수록 기피 대상이 되어가는 의체 보유자들에 대한 파우스트의 설명을 들었다.
   źródło: StageNode1-3.json :: dataList[id=10314].desc
   limit: do 250 znaków
   EN: Sinclair’s hometown of Calw was a village of artisan prosthetists. Faust detailed the growing tendency of the public to avoid prosthesis users as the Distortion Phenomenon becomes more frequent.
   PL: W Calw, rodzinnym miasteczku Sinclaira, większość mieszkańców wytwarza części do protez. Faust opowiedziała nam o posiadaczach protez, których unika się tym bardziej, im częściej dochodzi do Zniekształceń.
446. [Rozdziały, etapy i zdolności Dantego [10315] — tytuł] 정화
   źródło: StageNode1-3.json :: dataList[id=10315].title
   limit: do 40 znaków
   EN: Purification
   PL: Oczyszczenie
447. [Rozdziały, etapy i zdolności Dantego [10315] — miejsce] 칼프 마을 안
   źródło: StageNode1-3.json :: dataList[id=10315].place
   (powtórzenie elementu 441 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Rozdziały, etapy i zdolności Dantego [10315] — opis] 마을 구석에는 의체들이 쓰레기장처럼 쌓여 있다. 문득 내 본체란 무엇일지에 대해 생각해 본다.
   źródło: StageNode1-3.json :: dataList[id=10315].desc
   limit: do 160 znaków
   EN: Prosthetic bodies pile up like a landfill in a corner of the town. It brings me to think about what my “true self” is.
   PL: W kącie miasteczka protezy piętrzą się jak na wysypisku. Nagle zastanawiam się, czym właściwie jest moje prawdziwe ja.
449. [Rozdziały, etapy i zdolności Dantego [10316] — tytuł] 용기
   źródło: StageNode1-3.json :: dataList[id=10316].title
   limit: do 40 znaków
   EN: Fortitude
   PL: Odwaga
450. [Rozdziały, etapy i zdolności Dantego [10316] — miejsce] 칼프 마을 안
   źródło: StageNode1-3.json :: dataList[id=10316].place
   (powtórzenie elementu 441 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
451. [Rozdziały, etapy i zdolności Dantego [10316] — opis] 공포를 억누르려고 하는 싱클레어의 필사적인 모습이 안타까워 보인다. 싱클레어는 나를 보며 오래전 자신의 친구를 떠올린다.
   źródło: StageNode1-3.json :: dataList[id=10316].desc
   limit: do 160 znaków
   EN: I can only feel pity for Sinclair’s struggle to repress his fear. In looking at me, he is soon reminded of an old friend.
   PL: Żal patrzeć, jak rozpaczliwie Sinclair stara się stłumić strach. Patrząc na mnie, przypomina sobie dawnego przyjaciela.
452. [Rozdziały, etapy i zdolności Dantego [10317] — tytuł] 화마
   źródło: StageNode1-3.json :: dataList[id=10317].title
   limit: do 40 znaków
   EN: Bonfire
   PL: Pożoga
453. [Rozdziały, etapy i zdolności Dantego [10317] — miejsce] 싱클레어 저택 입구
   źródło: StageNode1-3.json :: dataList[id=10317].place
   limit: do 40 znaków
   EN: The Sinclair Estate
   PL: Przed posiadłością Sinclairów
454. [Rozdziały, etapy i zdolności Dantego [10317] — opis] 싱클레어의 저택 앞으로 도착했다. 저택 앞에는 의체 시체들이 못에 박힌 채 매달려 있다. 우리는 그중에 차마 똑바로 쳐다볼 수 없는 누군가의 모습을 발견한다.
   źródło: StageNode1-3.json :: dataList[id=10317].desc
   limit: do 200 znaków
   EN: We arrived at the Sinclair family estate. Crucified prosthetic bodies await us in the courtyard. One of them is someone we can’t bear to see straight.
   PL: Stanęliśmy przed posiadłością Sinclairów. Przed nią wiszą przybite gwoździami ciała z protezami. Wśród nich dostrzegamy kogoś, na kogo nie potrafimy spojrzeć wprost.
455. [Rozdziały, etapy i zdolności Dantego [10318] — tytuł] 화마 2
   źródło: StageNode1-3.json :: dataList[id=10318].title
   limit: do 40 znaków
   EN: Scheiterhaufen
   PL: Pożoga 2
456. [Rozdziały, etapy i zdolności Dantego [10318] — miejsce] 싱클레어 저택 입구
   źródło: StageNode1-3.json :: dataList[id=10318].place
   (powtórzenie elementu 453 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
457. [Rozdziały, etapy i zdolności Dantego [10318] — opis] 크로머는 불타오르는 저택 안으로 들어갔다. 아무 타격 없이 걸어오는 귀도의 모습에 수감자들의 진력은 단숨에 꺾여간다.
   źródło: StageNode1-3.json :: dataList[id=10318].desc
   limit: do 130 znaków
   EN: Kromer walked inside the burning mansion. The Sinners are dismayed by Guido’s unflinching advance.
   PL: Kromer weszła do płonącej rezydencji. Na widok Guida, który idzie ku nam bez draśnięcia, Grzesznicy w jednej chwili tracą ducha.
458. [Rozdziały, etapy i zdolności Dantego [10319] — tytuł] 나쁜 꿈
   źródło: StageNode1-3.json :: dataList[id=10319].title
   limit: do 40 znaków
   EN: A Bad Dream
   PL: Zły sen
459. [Rozdziały, etapy i zdolności Dantego [10319] — miejsce] 싱클레어 저택 입구
   źródło: StageNode1-3.json :: dataList[id=10319].place
   (powtórzenie elementu 453 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Rozdziały, etapy i zdolności Dantego [10319] — opis] 겨우 귀도를 물리쳤지만 싱클레어는 힘겨워한다. 가눌 수 없는 죄책감이 끊임없이 그를 몰아세우고 있는 것 같다.
   źródło: StageNode1-3.json :: dataList[id=10319].desc
   limit: do 170 znaków
   EN: We barely managed to defeat Guido, but Sinclair seems to be struggling to endure the immeasurable guilt weighing down on him.
   PL: Z trudem pokonaliśmy Guida, ale Sinclair ledwo się trzyma. Chyba bez przerwy dręczy go nieznośne poczucie winy.
461. [Rozdziały, etapy i zdolności Dantego [10320] — tytuł] 지하 통로
   źródło: StageNode1-3.json :: dataList[id=10320].title
   limit: do 40 znaków
   EN: Underpass
   PL: Podziemny korytarz
462. [Rozdziały, etapy i zdolności Dantego [10320] — miejsce] 싱클레어 저택 지하통로 어딘가
   źródło: StageNode1-3.json :: dataList[id=10320].place
   limit: do 50 znaków
   EN: Passage Under the Sinclair Estate
   PL: Gdzieś w podziemiach posiadłości Sinclairów
463. [Rozdziały, etapy i zdolności Dantego [10320] — opis] 싱클레어는 우리를 지하실로 안내했다. 지하실에는 수상한 통로가 이어져 있다. N사 파견원들이 만들어 놓았을 거라는 파우스트의 추측이 있었다.
   źródło: StageNode1-3.json :: dataList[id=10320].desc
   limit: do 150 znaków
   EN: Sinclair showed us to the basement with a suspicious passage. Faust assumes this tunnel was made by N Corp’s staff.
   PL: Sinclair zaprowadził nas do piwnicy, z której ciągnie się podejrzany korytarz. Faust przypuszcza, że wykopali go wysłannicy N Corp.
464. [Rozdziały, etapy i zdolności Dantego [10321] — tytuł] 지하 통로 2
   źródło: StageNode1-3.json :: dataList[id=10321].title
   limit: do 40 znaków
   EN: Unterführung
   PL: Podziemny korytarz 2
465. [Rozdziały, etapy i zdolności Dantego [10321] — miejsce] 싱클레어 저택 지하통로 어딘가
   źródło: StageNode1-3.json :: dataList[id=10321].place
   (powtórzenie elementu 462 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
466. [Rozdziały, etapy i zdolności Dantego [10321] — opis] 우리는 지하 통로를 계속 지나간다. 로보토미 지부가 점점 가까워지는 것 같다.
   źródło: StageNode1-3.json :: dataList[id=10321].desc
   limit: do 120 znaków
   EN: We continue following the underground passage. The branch facility feels closer.
   PL: Idziemy dalej podziemnym korytarzem. Filia L Corp. chyba jest coraz bliżej.
467. [Rozdziały, etapy i zdolności Dantego [10322] — tytuł] K-02  지부
   źródło: StageNode1-3.json :: dataList[id=10322].title
   limit: do 40 znaków
   EN: Branch K-02
   PL: Filia K-02
468. [Rozdziały, etapy i zdolności Dantego [10322] — miejsce] 싱클레어 저택 지하통로 어딘가
   źródło: StageNode1-3.json :: dataList[id=10322].place
   (powtórzenie elementu 462 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
469. [Rozdziały, etapy i zdolności Dantego [10322] — opis] 우리는 로보토미 지부로 도착했다. 그곳은 마치 고문실처럼 각종 기구와 살점, 기계들이 마구잡이로 널브러져 있다.
   źródło: StageNode1-3.json :: dataList[id=10322].desc
   limit: do 180 znaków
   EN: We’ve arrived at the branch. The room we walked into was like a torture chamber, lined with devices, contraptions, and bits of flesh.
   PL: Dotarliśmy do filii L Corp. Jak w sali tortur, wszędzie walają się narzędzia, strzępy ciał i maszyny.

## Rozdziały, etapy i zdolności Dantego: StageNode1-4
- plik gry: `StageNode1-4.json`

470. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 전원 하차
   źródło: StageNode1-4.json :: dataList[id=10401].title
   limit: do 40 znaków
   EN: Off the Bus
   PL:
471. [Rozdziały, etapy i zdolności Dantego [10401] — miejsce] 메피스토펠레스 안
   źródło: StageNode1-4.json :: dataList[id=10401].place
   limit: do 40 znaków
   EN: Aboard Mephistopheles
   PL:
472. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 정신을 차려보니 평화로워야 하는 둥지 한복판 속에서 죽어가는 수감자들이 보인다. 눈앞에 있는 것은… 무슨 일이 있었던 건지 찬찬히 복기를 해보기 시작했다.
   źródło: StageNode1-4.json :: dataList[id=10401].desc
   limit: do 260 znaków
   EN: I found myself looking at dead and dying Sinners in the middle of the Nest, a place that's supposed to be peaceful. And in front of me is... I began tracing back my memories to figure out what happened.
   PL:
473. [Rozdziały, etapy i zdolności Dantego [10402] — tytuł] 인재와 천재
   źródło: StageNode1-4.json :: dataList[id=10402].title
   limit: do 40 znaków
   EN: Talent and Genius
   PL:
474. [Rozdziały, etapy i zdolności Dantego [10402] — miejsce] K사 둥지 한복판
   źródło: StageNode1-4.json :: dataList[id=10402].place
   limit: do 40 znaków
   EN: K Corp's Nest
   PL:
475. [Rozdziały, etapy i zdolności Dantego [10402] — opis] 어째서 K사의 둥지에 환상체가 보이는 걸까. 모든 걸 해결할 때까지 돌아오지 말라는 베르길리우스의 눈빛은 진심인 듯 보였다. 혼비백산하며 도망가는 군중들을 지나쳐 가며 아비규환의 중심지로 향해간다.
   źródło: StageNode1-4.json :: dataList[id=10402].desc
   limit: do 300 znaków
   EN: Why are there Abnormalities in the middle of K Corp's Nest? Vergilius seemed to mean it when he said we could return to the bus after we've dealt with this commotion. Passing by frightened crowds, we head to the center of the mess.
   PL:
476. [Rozdziały, etapy i zdolności Dantego [10403] — tytuł] 드론과 환상체
   źródło: StageNode1-4.json :: dataList[id=10403].title
   limit: do 40 znaków
   EN: Drones and Abnormalities
   PL:
477. [Rozdziały, etapy i zdolności Dantego [10403] — miejsce] K사 둥지 한복판
   źródło: StageNode1-4.json :: dataList[id=10403].place
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
478. [Rozdziały, etapy i zdolności Dantego [10403] — opis] 앞을 가로막는 수상한 드론까지 처리해 가며 소동을 해결하고 있다. 아무리 봐도 상당히 비싸 보이는 데다가 K사라는 로고까지 박혀 있어 파괴하기 영 꺼림칙하기 그지없다.
   źródło: StageNode1-4.json :: dataList[id=10403].desc
   limit: do 250 znaków
   EN: Getting suspicious drones out of the way, we're dealing with the chaos. They look quite expensive at a glance, and the K Corp. logo on them makes me all the more hesitant about destroying them.
   PL:
479. [Rozdziały, etapy i zdolności Dantego [10404] — tytuł] 드론과 환상체 2
   źródło: StageNode1-4.json :: dataList[id=10404].title
   limit: do 40 znaków
   EN: Drones and Abnormalities 2
   PL:
480. [Rozdziały, etapy i zdolności Dantego [10404] — miejsce] K사 둥지 한복판
   źródło: StageNode1-4.json :: dataList[id=10404].place
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
481. [Rozdziały, etapy i zdolności Dantego [10404] — opis] 앞을 가로막는 수상한 드론까지 처리해 가며 소동을 해결하고 있다. 아무리 봐도 상당히 비싸 보이는 데다가 K사라는 로고까지 박혀 있어 파괴하기 영 꺼림칙하기 그지없다.
   źródło: StageNode1-4.json :: dataList[id=10404].desc
   (powtórzenie elementu 478 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
482. [Rozdziały, etapy i zdolności Dantego [10405] — tytuł] 드론과 환상체 3
   źródło: StageNode1-4.json :: dataList[id=10405].title
   limit: do 40 znaków
   EN: Drones and Abnormalities 3
   PL:
483. [Rozdziały, etapy i zdolności Dantego [10405] — miejsce] K사 둥지 한복판
   źródło: StageNode1-4.json :: dataList[id=10405].place
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
484. [Rozdziały, etapy i zdolności Dantego [10405] — opis] 앞을 가로막는 수상한 드론까지 처리해 가며 소동을 해결하고 있다. 아무리 봐도 상당히 비싸 보이는 데다가 K사라는 로고까지 박혀 있어 파괴하기 영 꺼림칙하기 그지없다.
   źródło: StageNode1-4.json :: dataList[id=10405].desc
   (powtórzenie elementu 478 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
485. [Rozdziały, etapy i zdolności Dantego [10406] — tytuł] 복귀
   źródło: StageNode1-4.json :: dataList[id=10406].title
   limit: do 40 znaków
   EN: Return
   PL:
486. [Rozdziały, etapy i zdolności Dantego [10406] — miejsce] K사 둥지 한복판
   źródło: StageNode1-4.json :: dataList[id=10406].place
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
487. [Rozdziały, etapy i zdolności Dantego [10406] — opis] 드디어 그 귀찮았던 드론들은 보이지 않는다. 이제 다시 정신을 가다듬고 우리가 진정으로 해치워야 하는 적, 환상체를 처리해야 한다.
   źródło: StageNode1-4.json :: dataList[id=10406].desc
   limit: do 160 znaków
   EN: We no longer see those annoying drones. Now, it's us between the Abnormalities, the threat we actually should remove.
   PL:
488. [Rozdziały, etapy i zdolności Dantego [10407] — tytuł] 의뢰인
   źródło: StageNode1-4.json :: dataList[id=10407].title
   limit: do 40 znaków
   EN: The Client
   PL:
489. [Rozdziały, etapy i zdolności Dantego [10407] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10407].place
   limit: do 40 znaków
   EN: K Corp. Laboratory
   PL:
490. [Rozdziały, etapy i zdolności Dantego [10407] — opis] 우여곡절 끝에 환상체를 물리치고 버스로 돌아갔다. 우리에게 의뢰를 맡긴다는 사람이 대체 누구일까. 희미하게 들리는 이스마엘의 콧노래를 애써 못 들은 척하며 버스 밖 풍경을 감상했다.
   źródło: StageNode1-4.json :: dataList[id=10407].desc
   limit: do 220 znaków
   EN: We managed to defeat the Abnormalities and got back on the bus. Who could be giving us a request? I looked out the window, pretending not to hear Ishmael's faint humming.
   PL:
491. [Rozdziały, etapy i zdolności Dantego [10408] — tytuł] 입사
   źródło: StageNode1-4.json :: dataList[id=10408].title
   limit: do 40 znaków
   EN: Application
   PL:
492. [Rozdziały, etapy i zdolności Dantego [10408] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10408].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
493. [Rozdziały, etapy i zdolności Dantego [10408] — opis] 다시 안 볼거라 생각했던 얼굴과 마주쳤다. 재회에 대해 딱히 반가워하는 수감자들은 없는 듯 보였다. 자신을 의뢰인이라고 소개한 '동랑'이라는 자가 내게 친근하게 말을 걸어왔다. 하지만 내 말은 수감자 외에는 닿지 않을 텐데...
   źródło: StageNode1-4.json :: dataList[id=10408].desc
   limit: do 350 znaków
   EN: We saw someone we never thought we would see again. But, the Sinners didn't seem too thrilled about the reunion. The client, who says his name is 'Dongrang', starts a friendly conversation. This is despite the fact that no one other than the Sinners can hear what I say...
   PL:
494. [Rozdziały, etapy i zdolności Dantego [10409] — tytuł] 재생 앰플
   źródło: StageNode1-4.json :: dataList[id=10409].title
   limit: do 40 znaków
   EN: Regeneration Ampules
   PL:
495. [Rozdziały, etapy i zdolności Dantego [10409] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10409].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
496. [Rozdziały, etapy i zdolności Dantego [10409] — opis] K사의 재생 기술에 대해 자랑을 늘어놓던 동랑은 한술 더 떠서 실험실을 보여주겠다고 했다.  삼조의 경악한 표정은 아랑곳하지 않은 채 우리는 동랑의 실험실을 향해 걸어갔다.
   źródło: StageNode1-4.json :: dataList[id=10409].desc
   limit: do 210 znaków
   EN: After boasting about K Corp's regeneration technology, Dongrang invited us to his lab. Disregarding Samjo's visible shock, we followed Dongrang into his workplace.
   PL:
497. [Rozdziały, etapy i zdolności Dantego [10410] — tytuł] 테러 단체
   źródło: StageNode1-4.json :: dataList[id=10410].title
   limit: do 40 znaków
   EN: Terrorist Organization
   PL:
498. [Rozdziały, etapy i zdolności Dantego [10410] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10410].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
499. [Rozdziały, etapy i zdolności Dantego [10410] — opis] 연구실에 침입자들이 생겼다. 삼조는 그들을 테러 단체라고 말했으나 침입자들은 그 명명을 불쾌하게 여기며 자신들을 '기술 해방 연합'이라고 소개했다. 명칭이 중요하진 않았다. 우리가 이 폭발에서 무사히 탈출하고 의뢰를 수행하려면 저들과 싸울 수밖에.
   źródło: StageNode1-4.json :: dataList[id=10410].desc
   limit: do 330 znaków
   EN: Intruders broke into the lab. Samjo called them terrorists, but they rejected the notion and instead introduced themselves as the 'technology liberation alliance'. Whatever they are, we have to fight them to survive the attack and proceed with the request.
   PL:
500. [Rozdziały, etapy i zdolności Dantego [10411] — tytuł] 테러 단체 2
   źródło: StageNode1-4.json :: dataList[id=10411].title
   limit: do 40 znaków
   EN: Terrorist Organization 2
   PL:
501. [Rozdziały, etapy i zdolności Dantego [10411] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10411].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [Rozdziały, etapy i zdolności Dantego [10411] — opis] 연구실에 침입자들이 생겼다. 삼조는 그들을 테러 단체라고 말했으나 침입자들은 그 명명을 불쾌하게 여기며 자신들을 '기술 해방 연합'이라고 소개했다. 명칭이 중요하진 않았다. 우리가 이 폭발에서 무사히 탈출하고 의뢰를 수행하려면 저들과 싸울 수밖에.
   źródło: StageNode1-4.json :: dataList[id=10411].desc
   (powtórzenie elementu 499 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [Rozdziały, etapy i zdolności Dantego [10412] — tytuł] 붕괴 앰플
   źródło: StageNode1-4.json :: dataList[id=10412].title
   limit: do 40 znaków
   EN: Decay Ampules
   PL:
504. [Rozdziały, etapy i zdolności Dantego [10412] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10412].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [Rozdziały, etapy i zdolności Dantego [10412] — opis] 연구실에 침입자들이 생겼다. 삼조는 그들을 테러 단체라고 말했으나 침입자들은 그 명명을 불쾌하게 여기며 자신들을 '기술 해방 연합'이라고 소개했다. 명칭이 중요하진 않았다. 우리가 이 폭발에서 무사히 탈출하고 의뢰를 수행하려면 저들과 싸울 수밖에.
   źródło: StageNode1-4.json :: dataList[id=10412].desc
   (powtórzenie elementu 499 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
506. [Rozdziały, etapy i zdolności Dantego [10413] — tytuł] 붕괴 앰플 2
   źródło: StageNode1-4.json :: dataList[id=10413].title
   limit: do 40 znaków
   EN: Decay Ampules 2
   PL:
507. [Rozdziały, etapy i zdolności Dantego [10413] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10413].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [Rozdziały, etapy i zdolności Dantego [10413] — opis] 연구실에 침입자들이 생겼다. 삼조는 그들을 테러 단체라고 말했으나 침입자들은 그 명명을 불쾌하게 여기며 자신들을 '기술 해방 연합'이라고 소개했다. 명칭이 중요하진 않았다. 우리가 이 폭발에서 무사히 탈출하고 의뢰를 수행하려면 저들과 싸울 수밖에.
   źródło: StageNode1-4.json :: dataList[id=10413].desc
   (powtórzenie elementu 499 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
509. [Rozdziały, etapy i zdolności Dantego [10414] — tytuł] 붕괴 앰플 3
   źródło: StageNode1-4.json :: dataList[id=10414].title
   limit: do 40 znaków
   EN: Decay Ampules 3
   PL:
510. [Rozdziały, etapy i zdolności Dantego [10414] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10414].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
511. [Rozdziały, etapy i zdolności Dantego [10414] — opis] 연구실에 침입자들이 생겼다. 삼조는 그들을 테러 단체라고 말했으나 침입자들은 그 명명을 불쾌하게 여기며 자신들을 '기술 해방 연합'이라고 소개했다. 명칭이 중요하진 않았다. 우리가 이 폭발에서 무사히 탈출하고 의뢰를 수행하려면 저들과 싸울 수밖에.
   źródło: StageNode1-4.json :: dataList[id=10414].desc
   (powtórzenie elementu 499 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
512. [Rozdziały, etapy i zdolności Dantego [10415] — tytuł] 탈환
   źródło: StageNode1-4.json :: dataList[id=10415].title
   limit: do 40 znaków
   EN: Reclaiming
   PL:
513. [Rozdziały, etapy i zdolności Dantego [10415] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10415].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
514. [Rozdziały, etapy i zdolności Dantego [10415] — opis] 기계들과 몇 차례 간의 전투를 거듭하며 점점 지쳐가던 찰나, 누군가의 의기양양한 목소리가 들려왔다.
   źródło: StageNode1-4.json :: dataList[id=10415].desc
   limit: do 120 znaków
   EN: As continued battles against the machines were wearing us out, I heard a confident voice.
   PL:
515. [Rozdziały, etapy i zdolności Dantego [10416] — tytuł] 인간의 시대
   źródło: StageNode1-4.json :: dataList[id=10416].title
   limit: do 40 znaków
   EN: Age of Humanity
   PL:
516. [Rozdziały, etapy i zdolności Dantego [10416] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10416].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Rozdziały, etapy i zdolności Dantego [10416] — opis] 슈렌느와 장미스패너 공방 해결사들까지 합류하면서 우리는 로보토미 지부로 향했다. 이번 임무에는 유독 인원이 많아 보인다. 테러범들이 점령하고 있다던데 괜찮은 걸까?
   źródło: StageNode1-4.json :: dataList[id=10416].desc
   limit: do 300 znaków
   EN: Accompanying Shrenne and Fixers from Rosespanner Workshop, we headed for the Lobotomy Corp. branch. Feels like a lot of people are involved in this mission. Are we really gonna be safe walking into a place occupied by terrorists?
   PL:
518. [Rozdziały, etapy i zdolności Dantego [10417] — tytuł] 기술해방연합
   źródło: StageNode1-4.json :: dataList[id=10417].title
   limit: do 50 znaków
   EN: Technology Liberation Alliance
   PL:
519. [Rozdziały, etapy i zdolności Dantego [10417] — miejsce] K사 로보토미 지부
   źródło: StageNode1-4.json :: dataList[id=10417].place
   limit: do 40 znaków
   EN: Nest K Lobotomy Corp. Branch
   PL:
520. [Rozdziały, etapy i zdolności Dantego [10417] — opis] 로보토미 지부에는 테러범들이 아닌, K사에서 보았던 기계들이 점령해 있었다.  하지만 이 기계들, 어째서인지 파괴를 하면 우리를 벌레 같은 것으로 비하하는 정체불명의 목소리가 재생된다.
   źródło: StageNode1-4.json :: dataList[id=10417].desc
   limit: do 250 znaków
   EN: In the branch facility, we ran into the same machines we saw at K Corp. instead of terrorists. For some reason, these machines are playing a strange voice that calls us worms when we destroy them.
   PL:
521. [Rozdziały, etapy i zdolności Dantego [10418] — tytuł] 최우수 직원
   źródło: StageNode1-4.json :: dataList[id=10418].title
   limit: do 40 znaków
   EN: Best Employee
   PL:
522. [Rozdziały, etapy i zdolności Dantego [10418] — miejsce] K사 로보토미 지부
   źródło: StageNode1-4.json :: dataList[id=10418].place
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [Rozdziały, etapy i zdolności Dantego [10418] — opis] 삼조 씨의 말에 의하면, 기술 해방 연합이라는 단체 중 한 명으로 K사 연구소 출신이 있다고 한다.  대체 어떤 목적을 가진 단체길래 이런 기계들을 만들고, 테러를 감행하면서까지 K사 연구소를 급습하는 것일까.
   źródło: StageNode1-4.json :: dataList[id=10418].desc
   limit: do 280 znaków
   EN: According to Samjo, one of the technology liberation alliance's members is a former K Corp. laboratory worker. What does that organization build these machines for, and why do they attack and terrorize K Corp's labs?
   PL:
524. [Rozdziały, etapy i zdolności Dantego [10419] — tytuł] 최우수 직원 2
   źródło: StageNode1-4.json :: dataList[id=10419].title
   limit: do 40 znaków
   EN: Best Employee 2
   PL:
525. [Rozdziały, etapy i zdolności Dantego [10419] — miejsce] K사 로보토미 지부
   źródło: StageNode1-4.json :: dataList[id=10419].place
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
526. [Rozdziały, etapy i zdolności Dantego [10419] — opis] K사 연구소 출신이라던 란이라는 자를 만났다. 제대로 된 대화도 나눠 보기 전, 그녀는 이해가 가지 않는 말을 남기고 영영 모습을 감췄다. 그리고 슈렌느는 왜 인지 계속해서 허탈한 표정이다.
   źródło: StageNode1-4.json :: dataList[id=10419].desc
   limit: do 260 znaków
   EN: We met Ran, who apparently used to work for a K Corp. laboratory. Before we could properly talk with her, she vanished forever, leaving mysterious words. And Shrenne looks despondent for whatever reason.
   PL:
527. [Rozdziały, etapy i zdolności Dantego [10420] — tytuł] 최우수 직원 3
   źródło: StageNode1-4.json :: dataList[id=10420].title
   limit: do 40 znaków
   EN: Best Employee 3
   PL:
528. [Rozdziały, etapy i zdolności Dantego [10420] — miejsce] K사 로보토미 지부
   źródło: StageNode1-4.json :: dataList[id=10420].place
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [Rozdziały, etapy i zdolności Dantego [10420] — opis] K사 연구소 출신이라던 란이라는 자를 만났다. 제대로 된 대화도 나눠 보기 전, 그녀는 이해가 가지 않는 말을 남기고 영영 모습을 감췄다. 그리고 슈렌느는 왜 인지 계속해서 허탈한 표정이다.
   źródło: StageNode1-4.json :: dataList[id=10420].desc
   (powtórzenie elementu 526 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
530. [Rozdziały, etapy i zdolności Dantego [10421] — tytuł] 배신자
   źródło: StageNode1-4.json :: dataList[id=10421].title
   limit: do 40 znaków
   EN: Traitor
   PL:
531. [Rozdziały, etapy i zdolności Dantego [10421] — miejsce] K사 로보토미 지부
   źródło: StageNode1-4.json :: dataList[id=10421].place
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
532. [Rozdziały, etapy i zdolności Dantego [10421] — opis] 오티스가 자꾸 슈렌느 쪽을 노려보며 무언가 결론을 내렸다는 듯, 발걸음을 멈췄다. 무슨 판단을 끝마쳤는지 알 수가 없는 나로서는 잠자코 오티스의 말을 들어보기로 했다.
   źródło: StageNode1-4.json :: dataList[id=10421].desc
   limit: do 210 znaków
   EN: Glaring at Shrenne, Outis stops on the way, having made some kind of conclusion. I couldn't begin to guess what it could be, so I decided to stay and listen.
   PL:
533. [Rozdziały, etapy i zdolności Dantego [10422] — tytuł] 배신자 2
   źródło: StageNode1-4.json :: dataList[id=10422].title
   limit: do 40 znaków
   EN: Traitor 2
   PL:
534. [Rozdziały, etapy i zdolności Dantego [10422] — miejsce] K사 로보토미 지부
   źródło: StageNode1-4.json :: dataList[id=10422].place
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [Rozdziały, etapy i zdolności Dantego [10422] — opis] 오티스와 뫼르소의 말로는 우리 중에 배신자가 있다고 했다. 장미스패너 공방에서 왔다던 니코라는 자는 시치미를 떼지만 충분히 합리적인 의심이 가능한 상황이었다. 아까까지만 해도 아무렇지 않게 대화를 나누던 자와 무기를 맞대고 있는 수감자들을 바라보았다. 지금은 비록 외부 세력들에 의한 배신이었지만... '우리'의 결속은 언제까지 이어질 수 있을까. 문득 그런 생각이 들었다.
   źródło: StageNode1-4.json :: dataList[id=10422].desc
   limit: do 440 znaków
   EN: Outis and Meursault claimed that there's a traitor in our group. Niko from Rosespanner Workshop denied the accusation, but the suspicion wasn't without reason. The Sinners were now confronting the people they were talking with mere moments ago. This one is an outsider turning against us, but... it made me wonder how long "our" bond could last.
   PL:
536. [Rozdziały, etapy i zdolności Dantego [10423] — tytuł] 배신자 3
   źródło: StageNode1-4.json :: dataList[id=10423].title
   limit: do 40 znaków
   EN: Traitor 3
   PL:
537. [Rozdziały, etapy i zdolności Dantego [10423] — miejsce] K사 로보토미 지부
   źródło: StageNode1-4.json :: dataList[id=10423].place
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [Rozdziały, etapy i zdolności Dantego [10423] — opis] 장미스패너 공방 해결사들과 슈렌느가 벌인 짓이었다는 사실이 밝혀졌다. 제대로 된 이유를 묻기도 전, 재생 앰플을 강제로 맞게 된 해결사 하나가 손쓸 새도 없이 녹아버렸다. 재생 앰플은... 신체를 복구해 주는 앰플이 아니었던가? 일단은 니코 씨와 다른 해결사들도 상대해야 한다.
   źródło: StageNode1-4.json :: dataList[id=10423].desc
   limit: do 400 znaków
   EN: It was revealed that Shrenne and Rosespanner Workshop Fixers were in cahoots with the enemy. Before we could ask the reason, one of the Fixers melted down after a forced injection of the regeneration ampule. Wasn't that... supposed to heal the body? For now, we have Niko and the remaining Fixers to deal with.
   PL:
539. [Rozdziały, etapy i zdolności Dantego [10424] — tytuł] 배신자 4
   źródło: StageNode1-4.json :: dataList[id=10424].title
   limit: do 40 znaków
   EN: Traitor 4
   PL:
540. [Rozdziały, etapy i zdolności Dantego [10424] — miejsce] K사 로보토미 지부
   źródło: StageNode1-4.json :: dataList[id=10424].place
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [Rozdziały, etapy i zdolności Dantego [10424] — opis] 장미스패너 공방 해결사들과 슈렌느가 벌인 짓이었다는 사실이 밝혀졌다. 제대로 된 이유를 묻기도 전, 재생 앰플을 강제로 맞게 된 해결사 하나가 손쓸 새도 없이 녹아버렸다. 재생 앰플은... 신체를 복구해 주는 앰플이 아니었던가? 일단은 니코 씨와 다른 해결사들도 상대해야 한다.
   źródło: StageNode1-4.json :: dataList[id=10424].desc
   (powtórzenie elementu 538 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
542. [Rozdziały, etapy i zdolności Dantego [10425] — tytuł] 배신자 5
   źródło: StageNode1-4.json :: dataList[id=10425].title
   limit: do 40 znaków
   EN: Traitor 5
   PL:
543. [Rozdziały, etapy i zdolności Dantego [10425] — miejsce] K사 로보토미 지부
   źródło: StageNode1-4.json :: dataList[id=10425].place
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [Rozdziały, etapy i zdolności Dantego [10425] — opis] 장미스패너 공방 해결사들과 슈렌느가 벌인 짓이었다는 사실이 밝혀졌다. 제대로 된 이유를 묻기도 전, 재생 앰플을 강제로 맞게 된 해결사 하나가 손쓸 새도 없이 녹아버렸다. 재생 앰플은... 신체를 복구해 주는 앰플이 아니었던가? 일단은 니코 씨와 다른 해결사들도 상대해야 한다.
   źródło: StageNode1-4.json :: dataList[id=10425].desc
   (powtórzenie elementu 538 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
545. [Rozdziały, etapy i zdolności Dantego [10426] — tytuł] 붉은 선
   źródło: StageNode1-4.json :: dataList[id=10426].title
   limit: do 40 znaków
   EN: A Red Line
   PL:
546. [Rozdziały, etapy i zdolności Dantego [10426] — miejsce] K사 로보토미 지부
   źródło: StageNode1-4.json :: dataList[id=10426].place
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
547. [Rozdziały, etapy i zdolności Dantego [10426] — opis] 장미스패너 공방의 해결사들을 전부 물리치고, 이제는 슈렌느를 추궁해야 한다. 슈렌느는 당황해하는 기색 없이 이 모든 상황들을 가만히 지켜보고 있다.
   źródło: StageNode1-4.json :: dataList[id=10426].desc
   limit: do 210 znaków
   EN: Now that the Rosespanner Workshop Fixers are defeated, it's time to question Shrenne. She stands still and watches the situation unfold without a hint of panic.
   PL:
548. [Rozdziały, etapy i zdolności Dantego [10427] — tytuł] 재회
   źródło: StageNode1-4.json :: dataList[id=10427].title
   limit: do 40 znaków
   EN: Reunion
   PL:
549. [Rozdziały, etapy i zdolności Dantego [10427] — miejsce] K사 로보토미 지부
   źródło: StageNode1-4.json :: dataList[id=10427].place
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
550. [Rozdziały, etapy i zdolności Dantego [10427] — opis] 누군가가 보낸 암살자로 인해 슈렌느 마저도 맥없이 숨을 거뒀다. 슈렌느와는 입사 동기라고 했던 동랑은 크게 충격을 받은 것 같진 않아 보였다. 그에게 있어서 내부 분열이란 건 일종의 굴레라고 한다. 나는 수감자를 어디까지 믿고 있을까, 수감자들은 나를 어느 정도로 믿고 있을까. 답이 나오지 않는 질문들을 남겨놓은 채로 황금가지가 공명하는 곳으로 향했다.
   źródło: StageNode1-4.json :: dataList[id=10427].desc
   limit: do 470 znaków
   EN: Assassins claimed Shrenne's life. Dongrang didn't appear too shocked by her death even though they had joined the Wing at the same time. He says internal conflict is like a cycle of some kind. How much trust do I have in the Sinners, and how much trust do they have in me? With questions I won't be able to answer, we headed for the place where the Golden Bough resonated.
   PL:
551. [Rozdziały, etapy i zdolności Dantego [10428] — tytuł] 구멍
   źródło: StageNode1-4.json :: dataList[id=10428].title
   limit: do 40 znaków
   EN: Hole
   PL:
552. [Rozdziały, etapy i zdolności Dantego [10428] — miejsce] K사 로보토미 지부
   źródło: StageNode1-4.json :: dataList[id=10428].place
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
553. [Rozdziały, etapy i zdolności Dantego [10428] — opis] 갑작스러운 동백의 기습으로 이상의 가슴팍이 꿰뚫렸다. 시간을 돌리면 메꿔질 구멍이겠지만 그것만으로도 괜찮은 걸까. 가만히 눈을 감은 채 잠들어 있는 이상이 무슨 꿈을 꾸고 있을지 알 길은 없었다.
   źródło: StageNode1-4.json :: dataList[id=10428].desc
   limit: do 300 znaków
   EN: Dongbaek's unexpected attack pierced Yi Sang's chest. Winding time would heal the wound, but will it really fill the hole in his heart? I had no way to know what dream Yi Sang could have been dreaming, resting with his eyes closed.
   PL:
554. [Rozdziały, etapy i zdolności Dantego [10429] — tytuł] 습격
   źródło: StageNode1-4.json :: dataList[id=10429].title
   limit: do 40 znaków
   EN: Raid
   PL:
555. [Rozdziały, etapy i zdolności Dantego [10429] — miejsce] K사 로보토미 지부
   źródło: StageNode1-4.json :: dataList[id=10429].place
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [Rozdziały, etapy i zdolności Dantego [10429] — opis] 아무 일 없던 것 마냥 이상은 다시 눈을 떴고, 삼조의 전화기에는 진동 소리가 연달아 울리기 시작한다.
   źródło: StageNode1-4.json :: dataList[id=10429].desc
   limit: do 150 znaków
   EN: Yi Sang came back to his senses as though nothing happened. Meanwhile, Samjo's phone starts ringing incessantly.
   PL:
557. [Rozdziały, etapy i zdolności Dantego [10430] — tytuł] 별자리
   źródło: StageNode1-4.json :: dataList[id=10430].title
   limit: do 40 znaków
   EN: Constellations
   PL:
558. [Rozdziały, etapy i zdolności Dantego [10430] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10430].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
559. [Rozdziały, etapy i zdolności Dantego [10430] — opis] 연구소에 갑작스러운 습격이 생겼다. 보아하니 기술해방연합원들은 환상체를 알로 되돌릴 기술까지 습득한 모양이다. 우리는 서둘러 K사 연구소로 향했다.
   źródło: StageNode1-4.json :: dataList[id=10430].desc
   limit: do 250 znaków
   EN: The K Corp. laboratory was unexpectedly attacked. It seems that the technology liberation alliance has acquired the ability to revert Abnormalities to eggs. We hurried back to the building.
   PL:
560. [Rozdziały, etapy i zdolności Dantego [10431] — tytuł] 강탈
   źródło: StageNode1-4.json :: dataList[id=10431].title
   limit: do 40 znaków
   EN: Seized
   PL:
561. [Rozdziały, etapy i zdolności Dantego [10431] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10431].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [Rozdziały, etapy i zdolności Dantego [10431] — opis] 기술해방연합원들의 해킹으로 인해 재생 앰플을 투여해 주던 K사의 기계가 우리를 적군으로 인식했다. 어쩔 수 없이 K사 전투원들을 물리치며 앞으로 나아가야 한다.
   źródło: StageNode1-4.json :: dataList[id=10431].desc
   limit: do 230 znaków
   EN: Hacked by technology liberation alliance members, K Corp's ampule-distributing machines turned against us. We have to defeat K Corp. security forces and make our way through.
   PL:
563. [Rozdziały, etapy i zdolności Dantego [10432] — tytuł] 강탈 2
   źródło: StageNode1-4.json :: dataList[id=10432].title
   limit: do 40 znaków
   EN: Seized 2
   PL:
564. [Rozdziały, etapy i zdolności Dantego [10432] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10432].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
565. [Rozdziały, etapy i zdolności Dantego [10432] — opis] 기술해방연합원들의 해킹으로 인해 재생 앰플을 투여해 주던 K사의 기계가 우리를 적군으로 인식했다. 어쩔 수 없이 K사 전투원들을 물리치며 앞으로 나아가야 한다.
   źródło: StageNode1-4.json :: dataList[id=10432].desc
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
566. [Rozdziały, etapy i zdolności Dantego [10433] — tytuł] 똑똑한 악인
   źródło: StageNode1-4.json :: dataList[id=10433].title
   limit: do 40 znaków
   EN: Bright Villains
   PL:
567. [Rozdziały, etapy i zdolności Dantego [10433] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10433].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [Rozdziały, etapy i zdolności Dantego [10433] — opis] 기술해방연합원은 후퇴조차 하지 않은 채 우리를 기다리고 있었다. 마치 준비한 비장의 무기라도 있는 것처럼…
   źródło: StageNode1-4.json :: dataList[id=10433].desc
   limit: do 150 znaków
   EN: The liberation alliance member was waiting for us instead of retreating. As if they have a secret weapon prepared...
   PL:
569. [Rozdziały, etapy i zdolności Dantego [10434] — tytuł] 똑똑한 악인 2
   źródło: StageNode1-4.json :: dataList[id=10434].title
   limit: do 40 znaków
   EN: Bright Villains 2
   PL:
570. [Rozdziały, etapy i zdolności Dantego [10434] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10434].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [Rozdziały, etapy i zdolności Dantego [10434] — opis] 기술해방연합원은 후퇴조차 하지 않은 채 우리를 기다리고 있었다. 마치 준비한 비장의 무기라도 있는 것처럼…
   źródło: StageNode1-4.json :: dataList[id=10434].desc
   (powtórzenie elementu 568 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [Rozdziały, etapy i zdolności Dantego [10435] — tytuł] 긴급 호출
   źródło: StageNode1-4.json :: dataList[id=10435].title
   limit: do 40 znaków
   EN: Urgent Call
   PL:
573. [Rozdziały, etapy i zdolności Dantego [10435] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10435].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
574. [Rozdziały, etapy i zdolności Dantego [10435] — opis] 또다시 삼조의 전화기에 불이 나고 있다. 어쩌면 동랑과 삼조가 자리를 비웠을 때, 그들에게는 얻지 못했던 유용한 정보를 찾을 수 있을지도…
   źródło: StageNode1-4.json :: dataList[id=10435].desc
   limit: do 200 znaków
   EN: Samjo's phone is ringing like crazy again. Maybe we can try and find useful information we couldn't get from Dongrang and Samjo while they're away...
   PL:
575. [Rozdziały, etapy i zdolności Dantego [10436] — tytuł] 긴급 호출 2
   źródło: StageNode1-4.json :: dataList[id=10436].title
   limit: do 40 znaków
   EN: Urgent Call 2
   PL:
576. [Rozdziały, etapy i zdolności Dantego [10436] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10436].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
577. [Rozdziały, etapy i zdolności Dantego [10436] — opis] 동랑과 삼조가 잠시 자리를 비운 사이, 뫼르소를 보내 슈렌느의 메일함을 조사하라고 했다. 어쩌면 기술해방연합이라는 단체에 대해 조금 더 알 수 있을지도 모른다.
   źródło: StageNode1-4.json :: dataList[id=10436].desc
   limit: do 200 znaków
   EN: While Dongrang and Samjo were away, we sent Meursault to investigate Shrenne's mailbox. Maybe we'll learn more about the technology liberation alliance.
   PL:
578. [Rozdziały, etapy i zdolności Dantego [10437] — tytuł] 긴급 호출 3
   źródło: StageNode1-4.json :: dataList[id=10437].title
   limit: do 40 znaków
   EN: Urgent Call 3
   PL:
579. [Rozdziały, etapy i zdolności Dantego [10437] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10437].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Rozdziały, etapy i zdolności Dantego [10437] — opis] 동랑과 삼조가 잠시 자리를 비운 사이, 뫼르소를 보내 슈렌느의 메일함을 조사하라고 했다. 어쩌면 기술해방연합이라는 단체에 대해 조금 더 알 수 있을지도 모른다.
   źródło: StageNode1-4.json :: dataList[id=10437].desc
   (powtórzenie elementu 577 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [Rozdziały, etapy i zdolności Dantego [10438] — tytuł] 찬란한 과거
   źródło: StageNode1-4.json :: dataList[id=10438].title
   limit: do 40 znaków
   EN: Glorious Past
   PL:
582. [Rozdziały, etapy i zdolności Dantego [10438] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10438].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
583. [Rozdziały, etapy i zdolności Dantego [10438] — opis] 뫼르소가 복귀했다. 과연 그가 가지고 온 정보에 어떤 내용이 담겨있을지 알아보자.
   źródło: StageNode1-4.json :: dataList[id=10438].desc
   limit: do 120 znaków
   EN: Meursault has returned. Let's see what information he brought with him.
   PL:
584. [Rozdziały, etapy i zdolności Dantego [10439] — tytuł] 찬란한 과거 2
   źródło: StageNode1-4.json :: dataList[id=10439].title
   limit: do 40 znaków
   EN: Glorious Past 2
   PL:
585. [Rozdziały, etapy i zdolności Dantego [10439] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10439].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Rozdziały, etapy i zdolności Dantego [10439] — opis] 기술해방연합원들의 해킹으로 인해 재생 앰플을 투여해 주던 K사의 기계가 우리를 적군으로 인식했다. 어쩔 수 없이 K사 전투원들을 물리치며 앞으로 나아가야 한다.
   źródło: StageNode1-4.json :: dataList[id=10439].desc
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
587. [Rozdziały, etapy i zdolności Dantego [10440] — tytuł] 찬란한 과거 3
   źródło: StageNode1-4.json :: dataList[id=10440].title
   limit: do 40 znaków
   EN: Glorious Past 3
   PL:
588. [Rozdziały, etapy i zdolności Dantego [10440] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10440].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
589. [Rozdziały, etapy i zdolności Dantego [10440] — opis] 기술해방연합원들의 해킹으로 인해 재생 앰플을 투여해 주던 K사의 기계가 우리를 적군으로 인식했다. 어쩔 수 없이 K사 전투원들을 물리치며 앞으로 나아가야 한다.
   źródło: StageNode1-4.json :: dataList[id=10440].desc
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [Rozdziały, etapy i zdolności Dantego [10441] — tytuł] 1등급
   źródło: StageNode1-4.json :: dataList[id=10441].title
   limit: do 40 znaków
   EN: Class 1
   PL:
591. [Rozdziały, etapy i zdolności Dantego [10441] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10441].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Rozdziały, etapy i zdolności Dantego [10441] — opis] 맞은편에서 범상치 않아 보이는 외형의 K사 전투원들이 보인다. 동랑과 삼조도 이야기를 잘 마쳤는지 우리와 다시 합류했다.
   źródło: StageNode1-4.json :: dataList[id=10441].desc
   limit: do 170 znaków
   EN: We see ominous-looking K Corp. staff on the other side. Dongrang and Samjo rejoined our group; it seems the talk went well enough.
   PL:
593. [Rozdziały, etapy i zdolności Dantego [10442] — tytuł] 1등급 2
   źródło: StageNode1-4.json :: dataList[id=10442].title
   limit: do 40 znaków
   EN: Class 1 2
   PL:
594. [Rozdziały, etapy i zdolności Dantego [10442] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10442].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
595. [Rozdziały, etapy i zdolności Dantego [10442] — opis] 맞은편에서 범상치 않아 보이는 외형의 K사 전투원들이 보인다. 동랑과 삼조도 이야기를 잘 마쳤는지 우리와 다시 합류했다.
   źródło: StageNode1-4.json :: dataList[id=10442].desc
   (powtórzenie elementu 592 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [Rozdziały, etapy i zdolności Dantego [10443] — tytuł] 기술이 없는 시대
   źródło: StageNode1-4.json :: dataList[id=10443].title
   limit: do 40 znaków
   EN: An Age Without Technology
   PL:
597. [Rozdziały, etapy i zdolności Dantego [10443] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10443].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Rozdziały, etapy i zdolności Dantego [10443] — opis] 낯익은 얼굴의 기술해방연합원을 마주쳤다. 일전에 란이라는 자와 함께 연구실을 침입했었던 자다.
   źródło: StageNode1-4.json :: dataList[id=10443].desc
   limit: do 160 znaków
   EN: We met a familiar technology liberation alliance member. That's the one who was with Ran in the last laboratory raid.
   PL:
599. [Rozdziały, etapy i zdolności Dantego [10444] — tytuł] 기술이 없는 시대 2
   źródło: StageNode1-4.json :: dataList[id=10444].title
   limit: do 40 znaków
   EN: An Age Without Technology 2
   PL:
600. [Rozdziały, etapy i zdolności Dantego [10444] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10444].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [Rozdziały, etapy i zdolności Dantego [10444] — opis] 마리르라는 자를 물리쳤다. 기술해방연합이라는 단체의 목표는 기술이 없는 시대를 향한 회귀였다.
   źródło: StageNode1-4.json :: dataList[id=10444].desc
   limit: do 200 znaków
   EN: We defeated Marile. With that, we finally learned that the technology liberation alliance's goal was to return to an era where there was no technology.
   PL:
602. [Rozdziały, etapy i zdolności Dantego [10445] — tytuł] 입사 제안
   źródło: StageNode1-4.json :: dataList[id=10445].title
   limit: do 40 znaków
   EN: Offer to Join
   PL:
603. [Rozdziały, etapy i zdolności Dantego [10445] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10445].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [Rozdziały, etapy i zdolności Dantego [10445] — opis] 료슈가 못마땅한 기색으로 이상을 부른다. 그리고 우리는 서로의 입사 이유에 대해 이야기 해보기 시작했다.
   źródło: StageNode1-4.json :: dataList[id=10445].desc
   limit: do 120 znaków
   EN: An unhappy Ryōshū calls Yi Sang. We began talking about our reasons for joining the company.
   PL:
605. [Rozdziały, etapy i zdolności Dantego [10446] — tytuł] 입사 제안 2
   źródło: StageNode1-4.json :: dataList[id=10446].title
   limit: do 40 znaków
   EN: Offer to Join 2
   PL:
606. [Rozdziały, etapy i zdolności Dantego [10446] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10446].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
607. [Rozdziały, etapy i zdolności Dantego [10446] — opis] 동랑이 말한 '감상실'로 향하며 마주치는 적들을 물리쳐야 한다.
   źródło: StageNode1-4.json :: dataList[id=10446].desc
   limit: do 120 znaków
   EN: To get to the 'screening room' Dongrang mentioned, we have to defeat the foes on the way.
   PL:
608. [Rozdziały, etapy i zdolności Dantego [10447] — tytuł] 감상실
   źródło: StageNode1-4.json :: dataList[id=10447].title
   limit: do 40 znaków
   EN: Screening Room
   PL:
609. [Rozdziały, etapy i zdolności Dantego [10447] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10447].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [Rozdziały, etapy i zdolności Dantego [10447] — opis] 드디어 '감상실'에 도착했다. 어두워서 잘 보이지 않았지만 이 공간의 중심이 되는 무언가가 우리를 내려다보는 듯 매달려 있다.
   źródło: StageNode1-4.json :: dataList[id=10447].desc
   limit: do 200 znaków
   EN: We made our way to the 'screening room'. It was dark, but we could see something at the center hanging down from above, like it was looking down at us.
   PL:
611. [Rozdziały, etapy i zdolności Dantego [10448] — tytuł] 봉우리
   źródło: StageNode1-4.json :: dataList[id=10448].title
   limit: do 40 znaków
   EN: Bud
   PL:
612. [Rozdziały, etapy i zdolności Dantego [10448] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10448].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [Rozdziały, etapy i zdolności Dantego [10448] — opis] 과거의 끊어졌다고 생각했던 인연들이 다시 만났고, 동백은 특이점 회수에 대한 강한 집념을 내비쳤다.
   źródło: StageNode1-4.json :: dataList[id=10448].desc
   limit: do 150 znaków
   EN: Past bonds thought to be severed have met again; Dongbaek showed obsessive determination to reclaim the Singularity.
   PL:
614. [Rozdziały, etapy i zdolności Dantego [10449] — tytuł] 아무것도
   źródło: StageNode1-4.json :: dataList[id=10449].title
   limit: do 40 znaków
   EN: Nothing
   PL:
615. [Rozdziały, etapy i zdolności Dantego [10449] — miejsce] 재배치된 K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10449].place
   limit: do 50 znaków
   EN: Rearranged K Corp. Laboratory
   PL:
616. [Rozdziały, etapy i zdolności Dantego [10449] — opis] 동백이 찔린 황금가지에서부터 강렬한 황금빛이 반짝였다가 사라졌다. 이윽고 우리가 있던 K사가 우그러지고 뒤틀린다. 무슨 일이 일어나는 것일까.
   źródło: StageNode1-4.json :: dataList[id=10449].desc
   limit: do 250 znaków
   EN: An intense golden glow blinked from the Golden Bough that was stabbed into Dongbaek. Soon enough, the space in the K Corp. building around us begins to twist and morph. What could be happening?
   PL:
617. [Rozdziały, etapy i zdolności Dantego [10450] — tytuł] 아무것도 2
   źródło: StageNode1-4.json :: dataList[id=10450].title
   limit: do 40 znaków
   EN: Nothing 2
   PL:
618. [Rozdziały, etapy i zdolności Dantego [10450] — miejsce] 재배치된 K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10450].place
   (powtórzenie elementu 615 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
619. [Rozdziały, etapy i zdolności Dantego [10450] — opis] 동백이 찔린 황금가지에서부터 강렬한 황금빛이 반짝였다가 사라졌다. 이윽고 우리가 있던 K사가 우그러지고 뒤틀린다. 무슨 일이 일어나는 것일까.
   źródło: StageNode1-4.json :: dataList[id=10450].desc
   (powtórzenie elementu 616 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Rozdziały, etapy i zdolności Dantego [10451] — tytuł] 결속
   źródło: StageNode1-4.json :: dataList[id=10451].title
   limit: do 40 znaków
   EN: Binding
   PL:
621. [Rozdziały, etapy i zdolności Dantego [10451] — miejsce] 재배치된 K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10451].place
   (powtórzenie elementu 615 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Rozdziały, etapy i zdolności Dantego [10451] — opis] 죽은 게 분명하다고 생각했던 해방연합대원들이 우리를 공격해 온다. 재배치 되어가는 공간 속에서 계속해서 앞으로 나아간다. 멀지 않은 곳에 있는 황금가지의 행방을 찾아.
   źródło: StageNode1-4.json :: dataList[id=10451].desc
   limit: do 240 znaków
   EN: Technology liberation alliance members we were sure were dead start attacking us. We keep moving forward in the rearranging space, looking for the Golden Bough that's still near us.
   PL:
623. [Rozdziały, etapy i zdolności Dantego [10452] — tytuł] 결속 2
   źródło: StageNode1-4.json :: dataList[id=10452].title
   limit: do 40 znaków
   EN: Binding 2
   PL:
624. [Rozdziały, etapy i zdolności Dantego [10452] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10452].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
625. [Rozdziały, etapy i zdolności Dantego [10452] — opis] 죽은 게 분명하다고 생각했던 해방연합대원들이 우리를 공격해 온다. 재배치 되어가는 공간 속에서 계속해서 앞으로 나아간다. 멀지 않은 곳에 있는 황금가지의 행방을 찾아.
   źródło: StageNode1-4.json :: dataList[id=10452].desc
   (powtórzenie elementu 622 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
626. [Rozdziały, etapy i zdolności Dantego [10453] — tytuł] 결속 3
   źródło: StageNode1-4.json :: dataList[id=10453].title
   limit: do 40 znaków
   EN: Binding 3
   PL:
627. [Rozdziały, etapy i zdolności Dantego [10453] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10453].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
628. [Rozdziały, etapy i zdolności Dantego [10453] — opis] 죽은 게 분명하다고 생각했던 해방연합대원들이 우리를 공격해 온다. 재배치 되어가는 공간 속에서 계속해서 앞으로 나아간다. 멀지 않은 곳에 있는 황금가지의 행방을 찾아.
   źródło: StageNode1-4.json :: dataList[id=10453].desc
   (powtórzenie elementu 622 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
629. [Rozdziały, etapy i zdolności Dantego [10454] — tytuł] 기억 속 구인회
   źródło: StageNode1-4.json :: dataList[id=10454].title
   limit: do 40 znaków
   EN: Reminisced League of Nine
   PL:
630. [Rozdziały, etapy i zdolności Dantego [10454] — miejsce] K사 연구소
   źródło: StageNode1-4.json :: dataList[id=10454].place
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
631. [Rozdziały, etapy i zdolności Dantego [10454] — opis] 죽은 게 분명하다고 생각했던 해방연합대원들이 우리를 공격해 온다. 재배치 되어가는 공간 속에서 계속해서 앞으로 나아간다. 멀지 않은 곳에 있는 황금가지의 행방을 찾아.
   źródło: StageNode1-4.json :: dataList[id=10454].desc
   (powtórzenie elementu 622 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: StageNode91-10
- plik gry: `StageNode91-10.json`

632. [Rozdziały, etapy i zdolności Dantego [911001] — tytuł] 일등석
   źródło: StageNode91-10.json :: dataList[id=911001].title
   limit: do 40 znaków
   EN: First Class
   PL:
633. [Rozdziały, etapy i zdolności Dantego [911002] — tytuł] 북부 해결사
   źródło: StageNode91-10.json :: dataList[id=911002].title
   limit: do 40 znaków
   EN: The Northern Fixer
   PL:
634. [Rozdziały, etapy i zdolności Dantego [911003] — tytuł] 사라진 승객
   źródło: StageNode91-10.json :: dataList[id=911003].title
   limit: do 40 znaków
   EN: Disappearing Passengers
   PL:
635. [Rozdziały, etapy i zdolności Dantego [911004] — tytuł] 열람 불가
   źródło: StageNode91-10.json :: dataList[id=911004].title
   limit: do 40 znaków
   EN: Inaccessible
   PL:
636. [Rozdziały, etapy i zdolności Dantego [911005] — tytuł] 멀티크랙 사무소
   źródło: StageNode91-10.json :: dataList[id=911005].title
   limit: do 40 znaków
   EN: MultiCrack Office
   PL:
637. [Rozdziały, etapy i zdolności Dantego [911006] — tytuł] 지옥도
   źródło: StageNode91-10.json :: dataList[id=911006].title
   limit: do 40 znaków
   EN: Painting of Hell
   PL:
638. [Rozdziały, etapy i zdolności Dantego [911007] — tytuł] 지옥도2
   źródło: StageNode91-10.json :: dataList[id=911007].title
   limit: do 40 znaków
   EN: Painting of Hell 2
   PL:
639. [Rozdziały, etapy i zdolności Dantego [911008] — tytuł] 혈귀
   źródło: StageNode91-10.json :: dataList[id=911008].title
   limit: do 40 znaków
   EN: Bloodfiends
   PL:
640. [Rozdziały, etapy i zdolności Dantego [911009] — tytuł] 정리 요원
   źródło: StageNode91-10.json :: dataList[id=911009].title
   limit: do 40 znaków
   EN: The Cleanup Agent
   PL:
641. [Rozdziały, etapy i zdolności Dantego [911010] — tytuł] 다음 칸으로
   źródło: StageNode91-10.json :: dataList[id=911010].title
   limit: do 40 znaków
   EN: Next Car
   PL:
642. [Rozdziały, etapy i zdolności Dantego [911011] — tytuł] 다음 칸으로2
   źródło: StageNode91-10.json :: dataList[id=911011].title
   limit: do 40 znaków
   EN: Next Car 2
   PL:
643. [Rozdziały, etapy i zdolności Dantego [911012] — tytuł] 의체 해결사
   źródło: StageNode91-10.json :: dataList[id=911012].title
   limit: do 40 znaków
   EN: Prosthetic Fixers
   PL:
644. [Rozdziały, etapy i zdolności Dantego [911013] — tytuł] 거느리는 자
   źródło: StageNode91-10.json :: dataList[id=911013].title
   limit: do 40 znaków
   EN: The One Who Lords
   PL:
645. [Rozdziały, etapy i zdolności Dantego [911014] — tytuł] 협상
   źródło: StageNode91-10.json :: dataList[id=911014].title
   limit: do 40 znaków
   EN: The Negotiation
   PL:
646. [Rozdziały, etapy i zdolności Dantego [911015] — tytuł] 불확실성
   źródło: StageNode91-10.json :: dataList[id=911015].title
   limit: do 40 znaków
   EN: Uncertainty
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode91-11
- plik gry: `StageNode91-11.json`

647. [Rozdziały, etapy i zdolności Dantego [911101] — tytuł] 제4회 발푸르기스의 밤
   źródło: StageNode91-11.json :: dataList[id=911101].title
   limit: do 40 znaków
   EN: The 4th Walpurgis Night
   PL:
648. [Rozdziały, etapy i zdolności Dantego [911103] — tytuł] 제4회 발푸르기스의 밤
   źródło: StageNode91-11.json :: dataList[id=911103].title
   (powtórzenie elementu 647 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: StageNode91-13
- plik gry: `StageNode91-13.json`

649. [Rozdziały, etapy i zdolności Dantego [911301] — tytuł] 제5회 발푸르기스의 밤
   źródło: StageNode91-13.json :: dataList[id=911301].title
   limit: do 40 znaków
   EN: The 5th Walpurgis Night
   PL:
650. [Rozdziały, etapy i zdolności Dantego [911303] — tytuł] 제5회 발푸르기스의 밤
   źródło: StageNode91-13.json :: dataList[id=911303].title
   (powtórzenie elementu 649 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: StageNode91-14
- plik gry: `StageNode91-14.json`

651. [Rozdziały, etapy i zdolności Dantego [911401] — tytuł] 데이터 수집
   źródło: StageNode91-14.json :: dataList[id=911401].title
   limit: do 40 znaków
   EN: Data Collection
   PL:
652. [Rozdziały, etapy i zdolności Dantego [911402] — tytuł] 건강검진
   źródło: StageNode91-14.json :: dataList[id=911402].title
   limit: do 40 znaków
   EN: Regular Health Check-up
   PL:
653. [Rozdziały, etapy i zdolności Dantego [911403] — tytuł] 이동 장치
   źródło: StageNode91-14.json :: dataList[id=911403].title
   limit: do 40 znaków
   EN: The Vehicle
   PL:
654. [Rozdziały, etapy i zdolności Dantego [911404] — tytuł] 호엔하임
   źródło: StageNode91-14.json :: dataList[id=911404].title
   limit: do 40 znaków
   EN: Hohenheim
   PL:
655. [Rozdziały, etapy i zdolności Dantego [911405] — tytuł] 조수
   źródło: StageNode91-14.json :: dataList[id=911405].title
   limit: do 40 znaków
   EN: The Assistant
   PL:
656. [Rozdziały, etapy i zdolności Dantego [911406] — tytuł] 의미 없는 분노
   źródło: StageNode91-14.json :: dataList[id=911406].title
   limit: do 40 znaków
   EN: Meaningless Wrath
   PL:
657. [Rozdziały, etapy i zdolności Dantego [911407] — tytuł] 방향 잃은 나태
   źródło: StageNode91-14.json :: dataList[id=911407].title
   limit: do 40 znaków
   EN: Directionless Sloth
   PL:
658. [Rozdziały, etapy i zdolności Dantego [911408] — tytuł] 스스로 가라앉는
   źródło: StageNode91-14.json :: dataList[id=911408].title
   limit: do 40 znaków
   EN: Sinking on Purpose
   PL:
659. [Rozdziały, etapy i zdolności Dantego [911409] — tytuł] 무뎌진 작살
   źródło: StageNode91-14.json :: dataList[id=911409].title
   limit: do 40 znaków
   EN: Dulled Harpoon
   PL:
660. [Rozdziały, etapy i zdolności Dantego [911410] — tytuł] 따끔따끔
   źródło: StageNode91-14.json :: dataList[id=911410].title
   limit: do 40 znaków
   EN: Stinging
   PL:
661. [Rozdziały, etapy i zdolności Dantego [911411] — tytuł] 호기심의 대가
   źródło: StageNode91-14.json :: dataList[id=911411].title
   limit: do 40 znaków
   EN: The Price of Curiosity
   PL:
662. [Rozdziały, etapy i zdolności Dantego [911412] — tytuł] 서열
   źródło: StageNode91-14.json :: dataList[id=911412].title
   limit: do 40 znaków
   EN: The Hierarchy
   PL:
663. [Rozdziały, etapy i zdolności Dantego [911413] — tytuł] 새로운 일련번호
   źródło: StageNode91-14.json :: dataList[id=911413].title
   limit: do 40 znaków
   EN: New Classification Codes
   PL:
664. [Rozdziały, etapy i zdolności Dantego [911414] — tytuł] 마지막 검진
   źródło: StageNode91-14.json :: dataList[id=911414].title
   limit: do 40 znaków
   EN: The Final Check-up
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode91-16
- plik gry: `StageNode91-16.json`

665. [Rozdziały, etapy i zdolności Dantego [911601] — tytuł] 신년
   źródło: StageNode91-16.json :: dataList[id=911601].title
   limit: do 40 znaków
   EN: Happy New Year
   PL:
666. [Rozdziały, etapy i zdolności Dantego [911602] — tytuł] 결투
   źródło: StageNode91-16.json :: dataList[id=911602].title
   limit: do 40 znaków
   EN: The Duel
   PL:
667. [Rozdziały, etapy i zdolności Dantego [911603] — tytuł] 안내자
   źródło: StageNode91-16.json :: dataList[id=911603].title
   limit: do 40 znaków
   EN: A Guide
   PL:
668. [Rozdziały, etapy i zdolności Dantego [911604] — tytuł] 습격
   źródło: StageNode91-16.json :: dataList[id=911604].title
   limit: do 40 znaków
   EN: Ambush
   PL:
669. [Rozdziały, etapy i zdolności Dantego [911605] — tytuł] 객잔
   źródło: StageNode91-16.json :: dataList[id=911605].title
   limit: do 40 znaków
   EN: Kezhan
   PL:
670. [Rozdziały, etapy i zdolności Dantego [911606] — tytuł] 의심
   źródło: StageNode91-16.json :: dataList[id=911606].title
   limit: do 40 znaków
   EN: Suspicion
   PL:
671. [Rozdziały, etapy i zdolności Dantego [911607] — tytuł] 관망
   źródło: StageNode91-16.json :: dataList[id=911607].title
   limit: do 40 znaków
   EN: Witnessing
   PL:
672. [Rozdziały, etapy i zdolności Dantego [911608] — tytuł] 흑수
   źródło: StageNode91-16.json :: dataList[id=911608].title
   limit: do 40 znaków
   EN: The Heishou Pack
   PL:
673. [Rozdziały, etapy i zdolności Dantego [911609] — tytuł] 사이화
   źródło: StageNode91-16.json :: dataList[id=911609].title
   limit: do 40 znaków
   EN: Shi Yihua
   PL:
674. [Rozdziały, etapy i zdolności Dantego [911610] — tytuł] 예상치 못한 적
   źródło: StageNode91-16.json :: dataList[id=911610].title
   limit: do 40 znaków
   EN: Unexpected Foe
   PL:
675. [Rozdziały, etapy i zdolności Dantego [911611] — tytuł] 뒷골목의 밤
   źródło: StageNode91-16.json :: dataList[id=911611].title
   limit: do 40 znaków
   EN: Night in the Backstreets
   PL:
676. [Rozdziały, etapy i zdolności Dantego [911612] — tytuł] 동맹
   źródło: StageNode91-16.json :: dataList[id=911612].title
   limit: do 40 znaków
   EN: Alliance
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode91-17
- plik gry: `StageNode91-17.json`

677. [Rozdziały, etapy i zdolności Dantego [911701] — tytuł] 제6회 발푸르기스의 밤
   źródło: StageNode91-17.json :: dataList[id=911701].title
   limit: do 40 znaków
   EN: The 6th Walpurgis Night
   PL:
678. [Rozdziały, etapy i zdolności Dantego [911703] — tytuł] 제6회 발푸르기스의 밤
   źródło: StageNode91-17.json :: dataList[id=911703].title
   (powtórzenie elementu 677 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: StageNode91-19
- plik gry: `StageNode91-19.json`

679. [Rozdziały, etapy i zdolności Dantego [911901] — tytuł] 가주의 증명
   źródło: StageNode91-19.json :: dataList[id=911901].title
   limit: do 40 znaków
   EN: The Family Hierarch's Proof
   PL:
680. [Rozdziały, etapy i zdolności Dantego [911902] — tytuł] 12명의 선생님
   źródło: StageNode91-19.json :: dataList[id=911902].title
   limit: do 40 znaków
   EN: Twelve Teachers
   PL:
681. [Rozdziały, etapy i zdolności Dantego [911903] — tytuł] 또 한 명의 학생
   źródło: StageNode91-19.json :: dataList[id=911903].title
   limit: do 40 znaków
   EN: Another Student
   PL:
682. [Rozdziały, etapy i zdolności Dantego [911904] — tytuł] 30일간의 수업
   źródło: StageNode91-19.json :: dataList[id=911904].title
   limit: do 40 znaków
   EN: Thirty Days of Classes
   PL:
683. [Rozdziały, etapy i zdolności Dantego [911905] — tytuł] 최종 시험
   źródło: StageNode91-19.json :: dataList[id=911905].title
   limit: do 40 znaków
   EN: Finals
   PL:
684. [Rozdziały, etapy i zdolności Dantego [911906] — tytuł] 가주 구출 작전
   źródło: StageNode91-19.json :: dataList[id=911906].title
   limit: do 40 znaków
   EN: Hierarch Rescue Operation
   PL:
685. [Rozdziały, etapy i zdolności Dantego [911907] — tytuł] 가주 구출 작전 2
   źródło: StageNode91-19.json :: dataList[id=911907].title
   limit: do 40 znaków
   EN: Hierarch Rescue Operation 2
   PL:
686. [Rozdziały, etapy i zdolności Dantego [911908] — tytuł] 필두
   źródło: StageNode91-19.json :: dataList[id=911908].title
   limit: do 40 znaków
   EN: The Adept
   PL:
687. [Rozdziały, etapy i zdolności Dantego [911909] — tytuł] 스승
   źródło: StageNode91-19.json :: dataList[id=911909].title
   limit: do 40 znaków
   EN: The Master
   PL:
688. [Rozdziały, etapy i zdolności Dantego [911910] — tytuł] 가주 구출 작전 3
   źródło: StageNode91-19.json :: dataList[id=911910].title
   limit: do 40 znaków
   EN: Hierarch Rescue Operation 3
   PL:
689. [Rozdziały, etapy i zdolności Dantego [911911] — tytuł] 청출어람
   źródło: StageNode91-19.json :: dataList[id=911911].title
   limit: do 50 znaków
   EN: When the Student Becomes the Master
   PL:
690. [Rozdziały, etapy i zdolności Dantego [911912] — tytuł] 증명
   źródło: StageNode91-19.json :: dataList[id=911912].title
   limit: do 40 znaków
   EN: The Proof
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode91-20
- plik gry: `StageNode91-20.json`

691. [Rozdziały, etapy i zdolności Dantego [912001] — tytuł] 낯선 바다
   źródło: StageNode91-20.json :: dataList[id=912001].title
   limit: do 40 znaków
   EN: The Unknown Sea
   PL:
692. [Rozdziały, etapy i zdolności Dantego [912002] — tytuł] 죽은 등대의 마을
   źródło: StageNode91-20.json :: dataList[id=912002].title
   limit: do 50 znaków
   EN: Village of the Dead Lighthouse
   PL:
693. [Rozdziały, etapy i zdolności Dantego [912003] — tytuł] 테라
   źródło: StageNode91-20.json :: dataList[id=912003].title
   limit: do 40 znaków
   EN: Terra
   PL:
694. [Rozdziały, etapy i zdolności Dantego [912004] — tytuł] 마사스호
   źródło: StageNode91-20.json :: dataList[id=912004].title
   limit: do 40 znaków
   EN: Vessel Masas
   PL:
695. [Rozdziały, etapy i zdolności Dantego [912005] — tytuł] 작은 파도
   źródło: StageNode91-20.json :: dataList[id=912005].title
   limit: do 40 znaków
   EN: Small Tide
   PL:
696. [Rozdziały, etapy i zdolności Dantego [912006] — tytuł] 재판관
   źródło: StageNode91-20.json :: dataList[id=912006].title
   limit: do 40 znaków
   EN: The Inquisitor
   PL:
697. [Rozdziały, etapy i zdolności Dantego [912007] — tytuł] 돌아가는 시계
   źródło: StageNode91-20.json :: dataList[id=912007].title
   limit: do 40 znaków
   EN: Spinning Clock
   PL:
698. [Rozdziały, etapy i zdolności Dantego [912008] — tytuł] 삼자 협의
   źródło: StageNode91-20.json :: dataList[id=912008].title
   limit: do 40 znaków
   EN: Three-way Agreement
   PL:
699. [Rozdziały, etapy i zdolności Dantego [912009] — tytuł] 등대 탈환 작전
   źródło: StageNode91-20.json :: dataList[id=912009].title
   limit: do 50 znaków
   EN: Operation Lighthouse Retrieval
   PL:
700. [Rozdziały, etapy i zdolności Dantego [912010] — tytuł] 거센 파도
   źródło: StageNode91-20.json :: dataList[id=912010].title
   limit: do 40 znaków
   EN: Rough Tides
   PL:
701. [Rozdziały, etapy i zdolności Dantego [912011] — tytuł] 동화 속의 기사
   źródło: StageNode91-20.json :: dataList[id=912011].title
   limit: do 40 znaków
   EN: The Fabled Knight
   PL:
702. [Rozdziały, etapy i zdolności Dantego [912012] — tytuł] 로도스 아일랜드
   źródło: StageNode91-20.json :: dataList[id=912012].title
   limit: do 40 znaków
   EN: Rhodes Island
   PL:
703. [Rozdziały, etapy i zdolności Dantego [912013] — tytuł] 도시의 빛
   źródło: StageNode91-20.json :: dataList[id=912013].title
   limit: do 40 znaków
   EN: Light of the City
   PL:
704. [Rozdziały, etapy i zdolności Dantego [912014] — tytuł] 선의의 순례
   źródło: StageNode91-20.json :: dataList[id=912014].title
   limit: do 40 znaków
   EN: Pilgrimage of Compassion
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode91-21
- plik gry: `StageNode91-21.json`

705. [Rozdziały, etapy i zdolności Dantego [912101] — tytuł] 낯선 바다
   źródło: StageNode91-21.json :: dataList[id=912101].title
   (powtórzenie elementu 691 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
706. [Rozdziały, etapy i zdolności Dantego [912102] — tytuł] 죽은 등대의 마을
   źródło: StageNode91-21.json :: dataList[id=912102].title
   (powtórzenie elementu 692 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
707. [Rozdziały, etapy i zdolności Dantego [912103] — tytuł] 테라
   źródło: StageNode91-21.json :: dataList[id=912103].title
   (powtórzenie elementu 693 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
708. [Rozdziały, etapy i zdolności Dantego [912104] — tytuł] 마사스호
   źródło: StageNode91-21.json :: dataList[id=912104].title
   (powtórzenie elementu 694 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
709. [Rozdziały, etapy i zdolności Dantego [912105] — tytuł] 작은 파도
   źródło: StageNode91-21.json :: dataList[id=912105].title
   (powtórzenie elementu 695 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
710. [Rozdziały, etapy i zdolności Dantego [912106] — tytuł] 재판관
   źródło: StageNode91-21.json :: dataList[id=912106].title
   (powtórzenie elementu 696 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
711. [Rozdziały, etapy i zdolności Dantego [912107] — tytuł] 돌아가는 시계
   źródło: StageNode91-21.json :: dataList[id=912107].title
   (powtórzenie elementu 697 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
712. [Rozdziały, etapy i zdolności Dantego [912108] — tytuł] 삼자 협의
   źródło: StageNode91-21.json :: dataList[id=912108].title
   (powtórzenie elementu 698 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
713. [Rozdziały, etapy i zdolności Dantego [912109] — tytuł] 등대 탈환 작전
   źródło: StageNode91-21.json :: dataList[id=912109].title
   (powtórzenie elementu 699 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
714. [Rozdziały, etapy i zdolności Dantego [912110] — tytuł] 거센 파도
   źródło: StageNode91-21.json :: dataList[id=912110].title
   (powtórzenie elementu 700 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
715. [Rozdziały, etapy i zdolności Dantego [912111] — tytuł] 동화 속의 기사
   źródło: StageNode91-21.json :: dataList[id=912111].title
   (powtórzenie elementu 701 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
716. [Rozdziały, etapy i zdolności Dantego [912112] — tytuł] 로도스 아일랜드
   źródło: StageNode91-21.json :: dataList[id=912112].title
   (powtórzenie elementu 702 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
717. [Rozdziały, etapy i zdolności Dantego [912113] — tytuł] 도시의 빛
   źródło: StageNode91-21.json :: dataList[id=912113].title
   (powtórzenie elementu 703 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
718. [Rozdziały, etapy i zdolności Dantego [912114] — tytuł] 선의의 순례
   źródło: StageNode91-21.json :: dataList[id=912114].title
   (powtórzenie elementu 704 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: StageNode91-23
- plik gry: `StageNode91-23.json`

719. [Rozdziały, etapy i zdolności Dantego [912301] — tytuł] 제8회 발푸르기스의 밤
   źródło: StageNode91-23.json :: dataList[id=912301].title
   limit: do 40 znaków
   EN: The 8th Walpurgis Night
   PL:
720. [Rozdziały, etapy i zdolności Dantego [912303] — tytuł] 제8회 발푸르기스의 밤
   źródło: StageNode91-23.json :: dataList[id=912303].title
   (powtórzenie elementu 719 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: StageNode91-24
- plik gry: `StageNode91-24.json`

721. [Rozdziały, etapy i zdolności Dantego [912401] — tytuł] 데이터 수집
   źródło: StageNode91-24.json :: dataList[id=912401].title
   (powtórzenie elementu 651 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
722. [Rozdziały, etapy i zdolności Dantego [912402] — tytuł] 건강검진
   źródło: StageNode91-24.json :: dataList[id=912402].title
   (powtórzenie elementu 652 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
723. [Rozdziały, etapy i zdolności Dantego [912403] — tytuł] 이동 장치
   źródło: StageNode91-24.json :: dataList[id=912403].title
   (powtórzenie elementu 653 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
724. [Rozdziały, etapy i zdolności Dantego [912404] — tytuł] 호엔하임
   źródło: StageNode91-24.json :: dataList[id=912404].title
   (powtórzenie elementu 654 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
725. [Rozdziały, etapy i zdolności Dantego [912405] — tytuł] 조수
   źródło: StageNode91-24.json :: dataList[id=912405].title
   (powtórzenie elementu 655 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
726. [Rozdziały, etapy i zdolności Dantego [912406] — tytuł] 의미 없는 분노
   źródło: StageNode91-24.json :: dataList[id=912406].title
   (powtórzenie elementu 656 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
727. [Rozdziały, etapy i zdolności Dantego [912407] — tytuł] 방향 잃은 나태
   źródło: StageNode91-24.json :: dataList[id=912407].title
   (powtórzenie elementu 657 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
728. [Rozdziały, etapy i zdolności Dantego [912408] — tytuł] 스스로 가라앉는
   źródło: StageNode91-24.json :: dataList[id=912408].title
   (powtórzenie elementu 658 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
729. [Rozdziały, etapy i zdolności Dantego [912409] — tytuł] 무뎌진 작살
   źródło: StageNode91-24.json :: dataList[id=912409].title
   (powtórzenie elementu 659 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
730. [Rozdziały, etapy i zdolności Dantego [912410] — tytuł] 따끔따끔
   źródło: StageNode91-24.json :: dataList[id=912410].title
   (powtórzenie elementu 660 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [Rozdziały, etapy i zdolności Dantego [912411] — tytuł] 호기심의 대가
   źródło: StageNode91-24.json :: dataList[id=912411].title
   (powtórzenie elementu 661 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
732. [Rozdziały, etapy i zdolności Dantego [912412] — tytuł] 서열
   źródło: StageNode91-24.json :: dataList[id=912412].title
   (powtórzenie elementu 662 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
733. [Rozdziały, etapy i zdolności Dantego [912413] — tytuł] 새로운 일련번호
   źródło: StageNode91-24.json :: dataList[id=912413].title
   (powtórzenie elementu 663 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
734. [Rozdziały, etapy i zdolności Dantego [912414] — tytuł] 마지막 검진
   źródło: StageNode91-24.json :: dataList[id=912414].title
   (powtórzenie elementu 664 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: StageNode91-25
- plik gry: `StageNode91-25.json`

735. [Rozdziały, etapy i zdolności Dantego [912501] — tytuł] 장례식
   źródło: StageNode91-25.json :: dataList[id=912501].title
   limit: do 40 znaków
   EN: Funeral
   PL:
736. [Rozdziały, etapy i zdolności Dantego [912502] — tytuł] 생존자
   źródło: StageNode91-25.json :: dataList[id=912502].title
   limit: do 40 znaków
   EN: Survivor
   PL:
737. [Rozdziały, etapy i zdolności Dantego [912503] — tytuł] 웨이페어러
   źródło: StageNode91-25.json :: dataList[id=912503].title
   limit: do 40 znaków
   EN: Wayfarer
   PL:
738. [Rozdziały, etapy i zdolności Dantego [912504] — tytuł] 유물과 표지
   źródło: StageNode91-25.json :: dataList[id=912504].title
   limit: do 40 znaków
   EN: Relics and the Sign
   PL:
739. [Rozdziały, etapy i zdolności Dantego [912505] — tytuł] 렌케츠엔
   źródło: StageNode91-25.json :: dataList[id=912505].title
   limit: do 40 znaków
   EN: Renketsuen
   PL:
740. [Rozdziały, etapy i zdolności Dantego [912506] — tytuł] 사루
   źródło: StageNode91-25.json :: dataList[id=912506].title
   limit: do 40 znaków
   EN: Saru
   PL:
741. [Rozdziały, etapy i zdolności Dantego [912507] — tytuł] 학교
   źródło: StageNode91-25.json :: dataList[id=912507].title
   limit: do 40 znaków
   EN: School
   PL:
742. [Rozdziały, etapy i zdolności Dantego [912508] — tytuł] 불행
   źródło: StageNode91-25.json :: dataList[id=912508].title
   limit: do 40 znaków
   EN: Miseries
   PL:
743. [Rozdziały, etapy i zdolności Dantego [912509] — tytuł] 기억
   źródło: StageNode91-25.json :: dataList[id=912509].title
   limit: do 40 znaków
   EN: Memories
   PL:
744. [Rozdziały, etapy i zdolności Dantego [912510] — tytuł] 지하실
   źródło: StageNode91-25.json :: dataList[id=912510].title
   limit: do 40 znaków
   EN: Basement
   PL:
745. [Rozdziały, etapy i zdolności Dantego [912511] — tytuł] 조용히 잊혀지는
   źródło: StageNode91-25.json :: dataList[id=912511].title
   limit: do 40 znaków
   EN: Into Oblivion, in Silence
   PL:
746. [Rozdziały, etapy i zdolności Dantego [912512] — tytuł] 만단지예
   źródło: StageNode91-25.json :: dataList[id=912512].title
   limit: do 40 znaków
   EN: S.A.N.G.R.I.A.
   PL:
747. [Rozdziały, etapy i zdolności Dantego [912513] — tytuł] 좋은 기억
   źródło: StageNode91-25.json :: dataList[id=912513].title
   limit: do 40 znaków
   EN: Good Memories
   PL:
748. [Rozdziały, etapy i zdolności Dantego [912514] — tytuł] 다음 목적지
   źródło: StageNode91-25.json :: dataList[id=912514].title
   limit: do 40 znaków
   EN: The Next Destination
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode91-27
- plik gry: `StageNode91-27.json`

749. [Rozdziały, etapy i zdolności Dantego [912701] — tytuł] 면담
   źródło: StageNode91-27.json :: dataList[id=912701].title
   limit: do 40 znaków
   EN: Consultation Session
   PL:
750. [Rozdziały, etapy i zdolności Dantego [912702] — tytuł] 합류
   źródło: StageNode91-27.json :: dataList[id=912702].title
   limit: do 40 znaków
   EN: Rendezvous
   PL:
751. [Rozdziały, etapy i zdolności Dantego [912703] — tytuł] 변곡점 찾기
   źródło: StageNode91-27.json :: dataList[id=912703].title
   limit: do 50 znaków
   EN: Search for the Inflection Point
   PL:
752. [Rozdziały, etapy i zdolności Dantego [912704] — tytuł] 오해
   źródło: StageNode91-27.json :: dataList[id=912704].title
   limit: do 40 znaków
   EN: Misconceptions
   PL:
753. [Rozdziały, etapy i zdolności Dantego [912705] — tytuł] 필름
   źródło: StageNode91-27.json :: dataList[id=912705].title
   limit: do 40 znaków
   EN: Film
   PL:
754. [Rozdziały, etapy i zdolności Dantego [912706] — tytuł] 사진들
   źródło: StageNode91-27.json :: dataList[id=912706].title
   limit: do 40 znaków
   EN: Photos
   PL:
755. [Rozdziały, etapy i zdolności Dantego [912707] — tytuł] 통조림
   źródło: StageNode91-27.json :: dataList[id=912707].title
   limit: do 40 znaków
   EN: Cans
   PL:
756. [Rozdziały, etapy i zdolności Dantego [912708] — tytuł] 금기
   źródło: StageNode91-27.json :: dataList[id=912708].title
   (powtórzenie elementu 413 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
757. [Rozdziały, etapy i zdolności Dantego [912709] — tytuł] 추적
   źródło: StageNode91-27.json :: dataList[id=912709].title
   limit: do 40 znaków
   EN: Pursuit
   PL:
758. [Rozdziały, etapy i zdolności Dantego [912710] — tytuł] 추적2
   źródło: StageNode91-27.json :: dataList[id=912710].title
   limit: do 40 znaków
   EN: Pursuit 2
   PL:
759. [Rozdziały, etapy i zdolności Dantego [912711] — tytuł] ???의 심상
   źródło: StageNode91-27.json :: dataList[id=912711].title
   limit: do 40 znaków
   EN: ???'s Fathoms
   PL:
760. [Rozdziały, etapy i zdolności Dantego [912712] — tytuł] 피사체
   źródło: StageNode91-27.json :: dataList[id=912712].title
   limit: do 40 znaków
   EN: The Subject
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode91-29
- plik gry: `StageNode91-29.json`

761. [Rozdziały, etapy i zdolności Dantego [912901] — tytuł] 제10회 발푸르기스의 밤
   źródło: StageNode91-29.json :: dataList[id=912901].title
   limit: do 40 znaków
   EN: The 10th Walpurgis Night
   PL:
762. [Rozdziały, etapy i zdolności Dantego [912903] — tytuł] 제10회 발푸르기스의 밤
   źródło: StageNode91-29.json :: dataList[id=912903].title
   (powtórzenie elementu 761 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: StageNode91-3
- plik gry: `StageNode91-3.json`

763. [Rozdziały, etapy i zdolności Dantego [910301] — tytuł] 치킨 어택
   źródło: StageNode91-3.json :: dataList[id=910301].title
   limit: do 40 znaków
   EN: Chicken Attack
   PL: Atak kurczaków
764. [Rozdziały, etapy i zdolności Dantego [910301] — miejsce] K사 번화가 골목
   źródło: StageNode91-3.json :: dataList[id=910301].place
   limit: do 40 znaków
   EN: Nest K Downtown Alley
   PL: Zaułek w śródmieściu Gniazda K Corp.
765. [Rozdziały, etapy i zdolności Dantego [910301] — opis] 다음 임무를 받기 위해 K사의 번화가에 도착했다.\n고소하고 감각적인 내음이 수감자들의 코를 향해 뛰어들어, 모두가 추억에 젖으려는 그 때,\n걸어 다니는 생닭들이 직접 수감자들에게 뛰어들기 시작했다.\n인간들에게 먹혀왔던 굴욕을 표출하는 것일까…?
   źródło: StageNode91-3.json :: dataList[id=910301].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: To receive a briefing for our next mission, we arrived downtown in K Corp’s Nest.\nAs a whiff of a roasty scent was about to take the Sinners for a nostalgia trip, a flock of walking raw chickens began to attack them.\nAre they trying to exact revenge for all their brethren that humans fried and gobbled up…?
   PL: Po następną misję przyjechaliśmy do śródmieścia Gniazda K Corp.\nGdy apetyczny, kuszący zapach wdarł się Grzesznikom do nosów i wszyscy już mieli się rozmarzyć,\nna Grzeszników rzuciły się chodzące surowe kury.\nCzyżby wyładowywały upokorzenie, że tak długo zjadali je ludzie…?
766. [Rozdziały, etapy i zdolności Dantego [910302] — tytuł] 치킨 어택 2
   źródło: StageNode91-3.json :: dataList[id=910302].title
   limit: do 40 znaków
   EN: Hen Havoc
   PL: Atak kurczaków 2
767. [Rozdziały, etapy i zdolności Dantego [910302] — miejsce] K사 번화가 골목
   źródło: StageNode91-3.json :: dataList[id=910302].place
   (powtórzenie elementu 764 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
768. [Rozdziały, etapy i zdolności Dantego [910302] — opis] 다음 임무를 받기 위해 K사의 번화가에 도착했다.\n고소하고 감각적인 내음이 수감자들의 코를 향해 뛰어들어, 모두가 추억에 젖으려는 그 때,\n걸어 다니는 생닭들이 직접 수감자들에게 뛰어들기 시작했다.\n인간들에게 먹혀왔던 굴욕을 표출하는 것일까…?
   źródło: StageNode91-3.json :: dataList[id=910302].desc
   (powtórzenie elementu 765 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
769. [Rozdziały, etapy i zdolności Dantego [910303] — tytuł] 헬스 치킨
   źródło: StageNode91-3.json :: dataList[id=910303].title
   limit: do 40 znaków
   EN: Hell’s Chicken
   PL: Hell’s Chicken
770. [Rozdziały, etapy i zdolności Dantego [910303] — miejsce] 은봉이네 호프집 앞
   źródło: StageNode91-3.json :: dataList[id=910303].place
   limit: do 50 znaków
   EN: Front of Eunbong’s Bar & Fryers
   PL: Przed Barem u Eunbong
771. [Rozdziały, etapy i zdolności Dantego [910303] — opis] 뒤틀림을 해소하기 위해서 지목된 방법은…\n뒤틀림이 만족할만한 ‘닭요리’를 만드는 것이었다.\n수감자들은 저마다 팔을 걷어붙이며 자신 있게 요리를 준비하는데…\n담배부터 꺼야 하는 건 아닐까?
   źródło: StageNode91-3.json :: dataList[id=910303].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: One idea we came up with to unravel the Distortion… was to present some “chicken-based cooking” that would appease it.\nThe Sinners confidently start preparing their dishes, but…\nShouldn’t they put their cigarettes out first?
   PL: Sposób na rozwiązanie Zniekształcenia, na który padło…\nto przyrządzenie “dania z kurczaka”, które zadowoli Zniekształcenie.\nGrzesznicy zakasują rękawy i pewni siebie biorą się do gotowania, ale…\nczy nie powinni najpierw zgasić papierosów?
772. [Rozdziały, etapy i zdolności Dantego [910304] — tytuł] 헬스 치킨 2
   źródło: StageNode91-3.json :: dataList[id=910304].title
   limit: do 40 znaków
   EN: Hell’s Chickapalooza
   PL: Hell’s Chicken 2
773. [Rozdziały, etapy i zdolności Dantego [910304] — miejsce] 은봉이네 호프집 앞
   źródło: StageNode91-3.json :: dataList[id=910304].place
   (powtórzenie elementu 770 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
774. [Rozdziały, etapy i zdolności Dantego [910304] — opis] 뒤틀림을 해소하기 위해서 지목된 방법은…\n뒤틀림이 만족할만한 ‘닭요리’를 만드는 것이었다.\n수감자들은 저마다 팔을 걷어붙이며 자신 있게 요리를 준비하는데…\n담배부터 꺼야 하는 건 아닐까?
   źródło: StageNode91-3.json :: dataList[id=910304].desc
   (powtórzenie elementu 771 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
775. [Rozdziały, etapy i zdolności Dantego [910305] — tytuł] 닭요리를 부탁해
   źródło: StageNode91-3.json :: dataList[id=910305].title
   limit: do 40 znaków
   EN: A Chicken in Hand
   PL: Danie z kurczaka, poproszę
776. [Rozdziały, etapy i zdolności Dantego [910305] — miejsce] 은봉이네 호프집 주방
   źródło: StageNode91-3.json :: dataList[id=910305].place
   limit: do 50 znaków
   EN: Eunbong’s Bar & Fryers Kitchen
   PL: Kuchnia Baru u Eunbong
777. [Rozdziały, etapy i zdolności Dantego [910305] — opis] 서로 그룹을 나눈 수감자들이 차례차례 음식을 선보이기 시작한다.\n어째서 대결의 형태를 띄게 되었는지는 아직도 모르겠지만…\n뒤틀린 식당 주인이 만족할만한 요리에 도달하기까지는 아직 요원해 보인다.\n뭐, 누가 봐도 만족할만한 요리는 아니긴 하지만…
   źródło: StageNode91-3.json :: dataList[id=910305].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Split into two groups, the Sinners present their dishes.\nI still don’t get how this turned into a competition…\nBut, in any case, they have a long way to go to sate the distorted restaurant owner’s palate.\nOr anyone else’s, if I’m being honest here…
   PL: Podzieleni na drużyny Grzesznicy po kolei prezentują swoje dania.\nWciąż nie rozumiem, jak to się zmieniło w pojedynek…\nAle do dania, które zadowoli zniekształconego właściciela, jeszcze daleka droga.\nCo prawda takie dania nie zadowoliłyby nikogo…
778. [Rozdziały, etapy i zdolności Dantego [910306] — tytuł] 닭요리를 부탁해 2
   źródło: StageNode91-3.json :: dataList[id=910306].title
   limit: do 40 znaków
   EN: A Chicken in Another Hand
   PL: Danie z kurczaka, poproszę 2
779. [Rozdziały, etapy i zdolności Dantego [910306] — miejsce] 은봉이네 호프집 주방
   źródło: StageNode91-3.json :: dataList[id=910306].place
   (powtórzenie elementu 776 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
780. [Rozdziały, etapy i zdolności Dantego [910306] — opis] 서로 그룹을 나눈 수감자들이 차례차례 음식을 선보이기 시작한다.\n어째서 대결의 형태를 띄게 되었는지는 아직도 모르겠지만…\n뒤틀린 식당 주인이 만족할만한 요리에 도달하기까지는 아직 요원해 보인다.\n뭐, 누가 봐도 만족할만한 요리는 아니긴 하지만…
   źródło: StageNode91-3.json :: dataList[id=910306].desc
   (powtórzenie elementu 777 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
781. [Rozdziały, etapy i zdolności Dantego [910307] — tytuł] 마스터 치킨 셰프
   źródło: StageNode91-3.json :: dataList[id=910307].title
   limit: do 40 znaków
   EN: Iron Chicken Chef
   PL: Kurczakowy MasterChef
782. [Rozdziały, etapy i zdolności Dantego [910307] — miejsce] 은봉이네 호프집 주방
   źródło: StageNode91-3.json :: dataList[id=910307].place
   (powtórzenie elementu 776 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
783. [Rozdziały, etapy i zdolności Dantego [910307] — opis] 음식을 맛본 식당 주인의 반응은 최악이었다.\n남아있는 기회 또한, 얼마 되지 않는 것 같다.\n이젠 수감자들 중에서 가장 그럴듯한 자에게 부탁하는 수밖에 없겠지…?
   źródło: StageNode91-3.json :: dataList[id=910307].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The owner’s reaction couldn’t have been worse.\nWe only have a few chances remaining, too.\nIt looks like our only option is to count on the Sinners who seem like they know their stuff, I hope…?
   PL: Reakcja właściciela po skosztowaniu była fatalna.\nSzans też zostało już chyba niewiele.\nPozostaje chyba tylko poprosić tego z Grzeszników, kto wydaje się najbardziej obiecujący…?
784. [Rozdziały, etapy i zdolności Dantego [910308] — tytuł] 마스터 치킨 셰프
   źródło: StageNode91-3.json :: dataList[id=910308].title
   limit: do 40 znaków
   EN: Master Chicken Chef
   PL: Kurczakowy MasterChef
785. [Rozdziały, etapy i zdolności Dantego [910308] — miejsce] 은봉이네 호프집 주방
   źródło: StageNode91-3.json :: dataList[id=910308].place
   (powtórzenie elementu 776 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
786. [Rozdziały, etapy i zdolności Dantego [910308] — opis] 음식을 맛본 식당 주인의 반응은 최악이었다.\n남아있는 기회 또한, 얼마 되지 않는 것 같다.\n이젠 수감자들 중에서 가장 그럴듯한 자에게 부탁하는 수밖에 없겠지…?
   źródło: StageNode91-3.json :: dataList[id=910308].desc
   (powtórzenie elementu 783 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
787. [Rozdziały, etapy i zdolności Dantego [910309] — tytuł] 사장님의 순한맛 심도
   źródło: StageNode91-3.json :: dataList[id=910309].title
   limit: do 50 znaków
   EN: A Restaurateur’s Mild Fathoms
   PL: Głębie właściciela: wersja łagodna
788. [Rozdziały, etapy i zdolności Dantego [910309] — miejsce] 은봉이네 호프집 주방
   źródło: StageNode91-3.json :: dataList[id=910309].place
   (powtórzenie elementu 776 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
789. [Rozdziały, etapy i zdolności Dantego [910310] — tytuł] 사장님의 매운맛 심도
   źródło: StageNode91-3.json :: dataList[id=910310].title
   limit: do 50 znaków
   EN: A Restaurateur’s Spicy Fathoms
   PL: Głębie właściciela: wersja ostra
790. [Rozdziały, etapy i zdolności Dantego [910310] — miejsce] 은봉이네 호프집 주방
   źródło: StageNode91-3.json :: dataList[id=910310].place
   (powtórzenie elementu 776 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: StageNode91-4
- plik gry: `StageNode91-4.json`

791. [Rozdziały, etapy i zdolności Dantego [910401] — tytuł] 바다다!
   źródło: StageNode91-4.json :: dataList[id=910401].title
   limit: do 40 znaków
   EN: The Beach Episode!
   PL:
792. [Rozdziały, etapy i zdolności Dantego [910401] — miejsce] 메피스토펠레스 내부
   źródło: StageNode91-4.json :: dataList[id=910401].place
   limit: do 40 znaków
   EN: Aboard Mephistopheles
   PL:
793. [Rozdziały, etapy i zdolności Dantego [910401] — opis] 길고 긴 터널을 지나, 우리는 대호수라고 불리는 곳에 도착했다.\n널찍하고 푸른 해안을 보며, 수감자들은 저마다 부푼 마음을 안고 무얼 하며 휴양할 것인지 말한다.\n하지만… 우리가 정말 쉴 수 있을까?
   źródło: StageNode91-4.json :: dataList[id=910401].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: After a long, long journey through a tunnel, we finally arrived at a place called the Great Lake.\nTaking in the view of the vast and turquoise waters, the Sinners begin excitedly chattering about what they want to do at the beach.\nBut... are we really here on vacation?
   PL:
794. [Rozdziały, etapy i zdolności Dantego [910402] — tytuł] 폐품 갯벌
   źródło: StageNode91-4.json :: dataList[id=910402].title
   limit: do 40 znaków
   EN: Mudflat Scrapyard
   PL:
795. [Rozdziały, etapy i zdolności Dantego [910402] — miejsce] 21구 뒷골목 어딘가
   źródło: StageNode91-4.json :: dataList[id=910402].place
   limit: do 40 znaków
   EN: Backstreets of District 21
   PL:
796. [Rozdziały, etapy i zdolności Dantego [910402] — opis] 결국 도착한 곳은 끈덕지고 구릿한 냄새가 가득한 녹색의 갯벌이었다.\n주변에는 대체 어디서부터 쓸려온 것인지 알 수 없는 폐품이 산처럼 쌓여있고, 저 멀리 푸른 바다의 모습은 그림의 떡인 양 멀게만 느껴진다.\n대체 이 곳에서 뭘 하려는 거지?
   źródło: StageNode91-4.json :: dataList[id=910402].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Of course, our destination was some squelchy, green, and fetid mudflat.\nThough I can see the blue sea in the distance, it feels as far away as a dream... buried in mountains of trash from who-knows-where.\nWhat could we possibly be here for?
   PL:
797. [Rozdziały, etapy i zdolności Dantego [910403] — tytuł] 크랲게?
   źródło: StageNode91-4.json :: dataList[id=910403].title
   limit: do 40 znaków
   EN: Trash Crabs?
   PL:
798. [Rozdziały, etapy i zdolności Dantego [910403] — miejsce] 21구 뒷골목 어딘가
   źródło: StageNode91-4.json :: dataList[id=910403].place
   (powtórzenie elementu 795 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
799. [Rozdziały, etapy i zdolności Dantego [910403] — opis] 폐품의 산 속에는 몸 이곳 저곳에 잡동사니를 붙이고 다니는 게… 와 비슷한 것이 있었다. 이스마엘의 말을 듣자하니, 이 U사 뒷골목에서 유명한 것들인 모양이다.\n그보다, 계속해서 이스마엘의 표정이 어두운데… 무슨 일이지?
   źródło: StageNode91-4.json :: dataList[id=910403].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: From mountainous refuse, out crawled crustacean creatures covered in all sorts of scrap. According to Ishmael, they're pretty infamous in the Backstreets of U Corp.\nSpeaking of which... I wonder what's going on with her? She's been in the doldrums all day.
   PL:
800. [Rozdziały, etapy i zdolności Dantego [910404] — tytuł] 보트 센터 사람들
   źródło: StageNode91-4.json :: dataList[id=910404].title
   limit: do 40 znaków
   EN: The Boatwrights
   PL:
801. [Rozdziały, etapy i zdolności Dantego [910404] — miejsce] 어금니 보트 센터
   źródło: StageNode91-4.json :: dataList[id=910404].place
   limit: do 40 znaków
   EN: Molar Boatworks
   PL:
802. [Rozdziały, etapy i zdolności Dantego [910404] — opis] 미카와 레인이라는 자들은 우리를 이미 아는 듯 했다. LCCB에서 우리가 올 것을 알리고 간 모양이다.\n다음 목적지를 향하기 위해서는 이 곳에서 메피스토펠레스를 개조해야만 하는 것 같다.
   źródło: StageNode91-4.json :: dataList[id=910404].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The pair called Mika and Rain seems to have been expecting us. I guess the LCCB already informed them of our arrival.\nLooks like we're going to have to modify Mephistopheles in order to get to our next destination.
   PL:
803. [Rozdziały, etapy i zdolności Dantego [910405] — tytuł] 폐품 수집 시간!
   źródło: StageNode91-4.json :: dataList[id=910405].title
   limit: do 40 znaków
   EN: Time to Collect Scrap!
   PL:
804. [Rozdziały, etapy i zdolności Dantego [910405] — miejsce] 21구 뒷골목 어딘가
   źródło: StageNode91-4.json :: dataList[id=910405].place
   (powtórzenie elementu 795 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
805. [Rozdziały, etapy i zdolności Dantego [910405] — opis] 폐품을 모으고, 버스를 배로 바꿀 시간이다.
   źródło: StageNode91-4.json :: dataList[id=910405].desc
   limit: do 120 znaków
   EN: Time to salvage scrap and prepare the bus for both hell and high water.
   PL:
806. [Rozdziały, etapy i zdolności Dantego [910406] — tytuł] 잡동사니 버스개조
   źródło: StageNode91-4.json :: dataList[id=910406].title
   limit: do 40 znaków
   EN: Makeshift Bus Mods
   PL:
807. [Rozdziały, etapy i zdolności Dantego [910406] — miejsce] 어금니 보트 센터
   źródło: StageNode91-4.json :: dataList[id=910406].place
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
808. [Rozdziały, etapy i zdolności Dantego [910406] — opis] 마침내 작업을 시작해 볼만한 정도의 부품을 모았다.\n이제, 수감자들과 잠시 쉴 수 있을까?\n그렇다면… 쉬는 동안 이스마엘과 대화라도 해봐야 할 것 같다.
   źródło: StageNode91-4.json :: dataList[id=910406].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We finally collected enough scrap for them to start working on the bus modifications.\nI wonder if we can get some time off?\nIf we do... then I should try talking to Ishmael.
   PL:
809. [Rozdziały, etapy i zdolności Dantego [910407] — tytuł] 비치… 발리볼?
   źródło: StageNode91-4.json :: dataList[id=910407].title
   limit: do 40 znaków
   EN: Beach... Volleyball?
   PL:
810. [Rozdziały, etapy i zdolności Dantego [910407] — miejsce] 21구 뒷골목 어딘가
   źródło: StageNode91-4.json :: dataList[id=910407].place
   (powtórzenie elementu 795 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
811. [Rozdziały, etapy i zdolności Dantego [910407] — opis] 자꾸만 어그러져 가는 이스마엘과 수감자들 간의 사이를 어떻게 해결해야 할지 고민되던 차에, 돈키호테와 이상이 말해준 비치 발리볼을 해보기로 했다.\n함께 운동하면서 서로 사이들이 돈독해지면 좋겠다.
   źródło: StageNode91-4.json :: dataList[id=910407].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Taking Don Quixote and Yi Sang's advice to mend the growing rift between Ishmael and the other Sinners, I decided that we should all try out a few rounds of beach volleyball.\nMaybe this activity can be an opportunity to build some rapport.
   PL:
812. [Rozdziały, etapy i zdolności Dantego [910408] — tytuł] 와해
   źródło: StageNode91-4.json :: dataList[id=910408].title
   limit: do 40 znaków
   EN: Dissolution
   PL:
813. [Rozdziały, etapy i zdolności Dantego [910408] — miejsce] 어금니 보트 센터
   źródło: StageNode91-4.json :: dataList[id=910408].place
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
814. [Rozdziały, etapy i zdolności Dantego [910408] — opis] 기대와는 다르게… 비치 발리볼은 완전히 망해버렸다.\n다들 좋지 않은 표정으로 크<size=110%>랲</size>게들과 싸우고 있다.\n역시… 뭐라고 한 마디라도 해둬야 될 것 같다.
   źródło: StageNode91-4.json :: dataList[id=910408].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <size=110%>, </size>, \n
   EN: The beach volleyball plan completely backfired…\nEveryone has a scowl on their face as they fight off the trash crabs.\nI have to do something about this…
   PL:
815. [Rozdziały, etapy i zdolności Dantego [910409] — tytuł] 폐품 수집 시간…
   źródło: StageNode91-4.json :: dataList[id=910409].title
   limit: do 40 znaków
   EN: Time to Collect Scrap...
   PL:
816. [Rozdziały, etapy i zdolności Dantego [910409] — miejsce] 21구 뒷골목 어딘가
   źródło: StageNode91-4.json :: dataList[id=910409].place
   (powtórzenie elementu 795 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
817. [Rozdziały, etapy i zdolności Dantego [910409] — opis] 상황은 갯벌의 색깔보다 어둡고 침침하지만…\n그래도 폐품을 모아야만 한다.
   źródło: StageNode91-4.json :: dataList[id=910409].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The situation's bleaker than the color of this mudflat...\nBut, we have to keep collecting more scrap.
   PL:
818. [Rozdziały, etapy i zdolności Dantego [910410] — tytuł] 불편한 시간
   źródło: StageNode91-4.json :: dataList[id=910410].title
   limit: do 40 znaków
   EN: Troubled Waters
   PL:
819. [Rozdziały, etapy i zdolności Dantego [910410] — miejsce] 어금니 보트 센터
   źródło: StageNode91-4.json :: dataList[id=910410].place
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
820. [Rozdziały, etapy i zdolności Dantego [910410] — opis] 처음보다 많은 폐품을 모으는 동안, 며칠이 또 흘러갔다.\n그동안 수감자들끼리 일하는 것을 멀찍이 지켜보기로 했다.\n이스마엘과 히스클리프를 어떻게 해야 할지 고민하면서…
   źródło: StageNode91-4.json :: dataList[id=910410].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We continued to collect scrap for a few more days.\nI decided to watch as the Sinners got to work,\nwondering what I could do about Ishmael and Heathcliff...
   PL:
821. [Rozdziały, etapy i zdolności Dantego [910411] — tytuł] 마지막 조각
   źródło: StageNode91-4.json :: dataList[id=910411].title
   limit: do 40 znaków
   EN: The Last Scrap
   PL:
822. [Rozdziały, etapy i zdolności Dantego [910411] — miejsce] 어금니 보트 센터
   źródło: StageNode91-4.json :: dataList[id=910411].place
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
823. [Rozdziały, etapy i zdolności Dantego [910411] — opis] 아직 아무것도 해결되지는 않았지만, 메피스토펠레스의 개조만큼은 벌써 막바지에 다다랐다.\n미카는 진지한 표정으로 시운전을 위해 모두를 불러모아 달라고 부탁했다.\n개조가 끝난 것은 좋지만… 이대로 다음 목적지로 나아가도 되는 걸까?
   źródło: StageNode91-4.json :: dataList[id=910411].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Nothing's been resolved, but Mephistopheles' modifications are almost complete.\nMika grimly requested that everyone gather to watch the test drive.\nI'm glad that the modifications are finally complete... but can we really press on in this state?
   PL:
824. [Rozdziały, etapy i zdolności Dantego [910412] — tytuł] 킹크랲게 사냥
   źródło: StageNode91-4.json :: dataList[id=910412].title
   limit: do 40 znaków
   EN: King Trash Crab Hunt
   PL:
825. [Rozdziały, etapy i zdolności Dantego [910412] — miejsce] 21구 뒷골목 어딘가
   źródło: StageNode91-4.json :: dataList[id=910412].place
   (powtórzenie elementu 795 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
826. [Rozdziały, etapy i zdolności Dantego [910412] — opis] 킹크<size=110%>랲</size>게와 싸우고, 커다란 폐품을 얻어보자.
   źródło: StageNode91-4.json :: dataList[id=910412].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <size=110%>, </size>
   EN: Let's battle the King Trash Crab, and get us a huge piece of scrap.
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode91-5
- plik gry: `StageNode91-5.json`

827. [Rozdziały, etapy i zdolności Dantego [910501] — tytuł] 무료
   źródło: StageNode91-5.json :: dataList[id=910501].title
   limit: do 40 znaków
   EN: Tedium
   PL:
828. [Rozdziały, etapy i zdolności Dantego [910501] — miejsce] 메피스토펠레스 버스배
   źródło: StageNode91-5.json :: dataList[id=910501].place
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
829. [Rozdziały, etapy i zdolności Dantego [910501] — opis] 호수에서의 대기가 점점 길어져가고, 수감자들은 심심함에 지쳐 나가 떨어질 것만 같다.\n그때, 히스클리프가 초조한 듯 베르길리우스에게 말을 거는데…
   źródło: StageNode91-5.json :: dataList[id=910501].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Our wait in the Lake grows ever longer. One by one, the Sinners begin succumbing to the tedium.\nThen Heathcliff suddenly and anxiously calls over to Vergilius...
   PL:
830. [Rozdziały, etapy i zdolności Dantego [910502] — tytuł] 솔깃한 제안
   źródło: StageNode91-5.json :: dataList[id=910502].title
   limit: do 40 znaków
   EN: A Tempting Offer
   PL:
831. [Rozdziały, etapy i zdolności Dantego [910502] — miejsce] 메피스토펠레스 버스배
   źródło: StageNode91-5.json :: dataList[id=910502].place
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
832. [Rozdziały, etapy i zdolności Dantego [910502] — opis] 돈키호테는 의미심장한 표정으로, 우리를 조종석으로 데리고 갔다.\n거기엔 뒷문에 변동이 생겼을 때 파우스트가 들여다보던 모니터가 있었고… 알 수 없는 문자들이 늘어놓아져 있었다.
   źródło: StageNode91-5.json :: dataList[id=910502].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Don Quixote brought us to the helm of the ship.\nThere it was, the monitor that Faust would analyze whenever we had a Backdoor volatility. ... And there they were again, those unknown symbols.
   PL:
833. [Rozdziały, etapy i zdolności Dantego [910503] — tytuł] 뜻 밖의 여정
   źródło: StageNode91-5.json :: dataList[id=910503].title
   limit: do 40 znaków
   EN: An Unexpected Journey
   PL:
834. [Rozdziały, etapy i zdolności Dantego [910503] — miejsce] 버스의 뒷문
   źródło: StageNode91-5.json :: dataList[id=910503].place
   limit: do 40 znaków
   EN: Bus’s Backdoor
   PL:
835. [Rozdziały, etapy i zdolności Dantego [910503] — opis] 돈키호테가 보았다던 그 뒷문을 열고 들어가자, 그곳엔 공장 같아 보이는 공간이 펼쳐져 있었다.\n돈키호테는 이미 이곳에 와본 적이 있는지, 자연스럽게 누군가를 부르는데…
   źródło: StageNode91-5.json :: dataList[id=910503].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We entered the Backdoor Don Quixote claimed to have seen. In it was... what appeared to be a factory.\nClearly not her first time in this establishment, Don Quixote calls over to someone...
   PL:
836. [Rozdziały, etapy i zdolności Dantego [910504] — tytuł] 괴물들의 선물
   źródło: StageNode91-5.json :: dataList[id=910504].title
   limit: do 40 znaków
   EN: Monstrous Gifts
   PL:
837. [Rozdziały, etapy i zdolności Dantego [910504] — miejsce] 선물공장 응접실
   źródło: StageNode91-5.json :: dataList[id=910504].place
   limit: do 40 znaków
   EN: Gift Factory Reception Hall
   PL:
838. [Rozdziały, etapy i zdolności Dantego [910504] — opis] 썰매 안의 주머니에서 튀어나온 것은, 조그마한 꼬마와 사지가 성치 못한 여러 사람들이었다.\n아무래도 납치를 당해서 이곳까지 오게 된 것 같은데, 무슨 일이 있었던 걸까.
   źródło: StageNode91-5.json :: dataList[id=910504].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: What popped out from the sack we found atop the sleigh were... several mutilated bodies and a small child.\nIt looks like they were kidnapped here... I wonder what happened.
   PL:
839. [Rozdziały, etapy i zdolności Dantego [910505] — tytuł] 감동의 재회
   źródło: StageNode91-5.json :: dataList[id=910505].title
   limit: do 40 znaków
   EN: A Touching Reunion
   PL:
840. [Rozdziały, etapy i zdolności Dantego [910505] — miejsce] 선물 분류 공장
   źródło: StageNode91-5.json :: dataList[id=910505].place
   limit: do 40 znaków
   EN: Gift Distribution Factory
   PL:
841. [Rozdziały, etapy i zdolności Dantego [910505] — opis] 히스클리프와 돈키호테가 쓰러지고 절체절명의 상황, 수감자들이 나를 찾아와준 덕에 목숨을 건질 수 있었다.\n하지만… 가스에 의해 쓰러졌던 두 사람이 보이질 않는다.
   źródło: StageNode91-5.json :: dataList[id=910505].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Heathcliff and Don Quixote were both out cold, but I managed to survive thanks to the Sinners who came for me.\n... But I don't see the two unconscious Sinners anywhere.
   PL:
842. [Rozdziały, etapy i zdolności Dantego [910506] — tytuł] 두 사람을 찾아서
   źródło: StageNode91-5.json :: dataList[id=910506].title
   limit: do 40 znaków
   EN: To Find the Pair
   PL:
843. [Rozdziały, etapy i zdolności Dantego [910506] — miejsce] 선물 분류 공장
   źródło: StageNode91-5.json :: dataList[id=910506].place
   (powtórzenie elementu 840 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
844. [Rozdziały, etapy i zdolności Dantego [910506] — opis] 이 공장 어딘가로 끌려갔을 것이다. 아마 크레용씨도 함께 있겠지… 빨리 찾아서 돌아가야만 한다.
   źródło: StageNode91-5.json :: dataList[id=910506].desc
   limit: do 170 znaków
   EN: They must've been taken to a different sector of this factory. Crayon must be there with them... We have to find them, quick.
   PL:
845. [Rozdziały, etapy i zdolności Dantego [910507] — tytuł] 두 사람을 찾아서
   źródło: StageNode91-5.json :: dataList[id=910507].title
   (powtórzenie elementu 842 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
846. [Rozdziały, etapy i zdolności Dantego [910507] — miejsce] 선물 분류 공장
   źródło: StageNode91-5.json :: dataList[id=910507].place
   (powtórzenie elementu 840 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
847. [Rozdziały, etapy i zdolności Dantego [910507] — opis] 이 공장 어딘가로 끌려갔을 것이다. 아마 크레용씨도 함께 있겠지… 빨리 찾아서 돌아가야만 한다.
   źródło: StageNode91-5.json :: dataList[id=910507].desc
   (powtórzenie elementu 844 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
848. [Rozdziały, etapy i zdolności Dantego [910508] — tytuł] 누구를 위하여 선물은 만들어지는가
   źródło: StageNode91-5.json :: dataList[id=910508].title
   limit: do 40 znaków
   EN: For Whom the Gnomes Pack
   PL:
849. [Rozdziały, etapy i zdolności Dantego [910508] — miejsce] 선물 취합 공장
   źródło: StageNode91-5.json :: dataList[id=910508].place
   limit: do 40 znaków
   EN: Gift Assembly Factory
   PL:
850. [Rozdziały, etapy i zdolności Dantego [910508] — opis] 공장은 생각보다 크고 복잡한 구조를 갖추고 있었다. 대체 이들은 누구를 위해서, 왜 선물을 만들고 있는 걸까.
   źródło: StageNode91-5.json :: dataList[id=910508].desc
   limit: do 170 znaków
   EN: The factory was much larger and much more complicated than it first appeared. Who are the gnomes making these gifts for? And why?
   PL:
851. [Rozdziały, etapy i zdolności Dantego [910509] — tytuł] 누구를 위하여 선물은 만들어지는가
   źródło: StageNode91-5.json :: dataList[id=910509].title
   (powtórzenie elementu 848 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
852. [Rozdziały, etapy i zdolności Dantego [910509] — miejsce] 선물 취합 공장
   źródło: StageNode91-5.json :: dataList[id=910509].place
   (powtórzenie elementu 849 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
853. [Rozdziały, etapy i zdolności Dantego [910509] — opis] 공장은 생각보다 크고 복잡한 구조를 갖추고 있었다. 대체 이들은 누구를 위해서, 왜 선물을 만들고 있는 걸까.
   źródło: StageNode91-5.json :: dataList[id=910509].desc
   (powtórzenie elementu 850 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
854. [Rozdziały, etapy i zdolności Dantego [910510] — tytuł] 증오를 찍어낸 선물
   źródło: StageNode91-5.json :: dataList[id=910510].title
   limit: do 40 znaków
   EN: Gift of Hatred, Given Shape
   PL:
855. [Rozdziały, etapy i zdolności Dantego [910510] — miejsce] 선물 제작소
   źródło: StageNode91-5.json :: dataList[id=910510].place
   limit: do 40 znaków
   EN: Gift Assembly
   PL:
856. [Rozdziały, etapy i zdolności Dantego [910510] — opis] 뫼르소가 가리킨 곳은 선물을 만드는 공간이었다. 잡아 온 '재료'로 선물을 찍어내는 모습은, 충격적이지 않을 수 없었다.\n그리고, 겨우 찾아낸 두 수감자들도 선물이 되기 직전이었다…
   źródło: StageNode91-5.json :: dataList[id=910510].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The location pointed out by Meursault was the gift assembly line. The sight of them assembling gifts with the 'materials' they kidnapped was... shocking.\nAnd the two Sinners we were searching for were also about to be turned into gifts themselves.
   PL:
857. [Rozdziały, etapy i zdolności Dantego [910511] — tytuł] 선물을 배달하는 거인
   źródło: StageNode91-5.json :: dataList[id=910511].title
   limit: do 40 znaków
   EN: The Gift-giving Giant
   PL:
858. [Rozdziały, etapy i zdolności Dantego [910511] — miejsce] 선물 제작소
   źródło: StageNode91-5.json :: dataList[id=910511].place
   (powtórzenie elementu 855 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
859. [Rozdziały, etapy i zdolności Dantego [910511] — opis] 수염 거인, 산타타와의 협상 여지는 없었던 것 같다. 여기서 쓰러트려야만 한다.
   źródło: StageNode91-5.json :: dataList[id=910511].desc
   limit: do 160 znaków
   EN: Our negotiation attempt with the beard giant Santata predictably fell through. We have no choice but to defeat him here.
   PL:
860. [Rozdziały, etapy i zdolności Dantego [910512] — tytuł] 여정의 끝
   źródło: StageNode91-5.json :: dataList[id=910512].title
   limit: do 40 znaków
   EN: A Journey's End
   PL:
861. [Rozdziały, etapy i zdolności Dantego [910512] — miejsce] 선물 제작소
   źródło: StageNode91-5.json :: dataList[id=910512].place
   (powtórzenie elementu 855 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
862. [Rozdziały, etapy i zdolności Dantego [910512] — opis] 산타타가 쓰러졌지만, 자폭 공격이라도 하려는 것처럼 몸이 부풀기 시작한다. 그 때, 어디선가 낯선 목소리가 들려오는데…
   źródło: StageNode91-5.json :: dataList[id=910512].desc
   limit: do 190 znaków
   EN: We defeated Santata, but his body begins to expand as though it's about to explode. That's when we hear a sudden, unfamiliar voice from somewhere...
   PL:
863. [Rozdziały, etapy i zdolności Dantego [910513] — tytuł] 산타타
   źródło: StageNode91-5.json :: dataList[id=910513].title
   limit: do 40 znaków
   EN: Santata
   PL:
864. [Rozdziały, etapy i zdolności Dantego [910513] — miejsce] 선물 제작소
   źródło: StageNode91-5.json :: dataList[id=910513].place
   (powtórzenie elementu 855 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
865. [Rozdziały, etapy i zdolności Dantego [910513] — opis] 수염 거인, 산타타와의 협상 여지는 없었던 것 같다. 직접 처리하는 수 밖에.
   źródło: StageNode91-5.json :: dataList[id=910513].desc
   limit: do 160 znaków
   EN: Our negotiation attempt with the beard giant Santata predictably fell through. We have no choice but to defeat him here.
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode91-6
- plik gry: `StageNode91-6.json`

866. [Rozdziały, etapy i zdolności Dantego [910601] — tytuł] 제2회 발푸르기스의 밤
   źródło: StageNode91-6.json :: dataList[id=910601].title
   limit: do 40 znaków
   EN: The 2nd Walpurgis Night
   PL:
867. [Rozdziały, etapy i zdolności Dantego [910603] — tytuł] 제2회 발푸르기스의 밤
   źródło: StageNode91-6.json :: dataList[id=910603].title
   (powtórzenie elementu 866 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: StageNode91-7
- plik gry: `StageNode91-7.json`

868. [Rozdziały, etapy i zdolności Dantego [910701] — tytuł] 20구의 뒷골목
   źródło: StageNode91-7.json :: dataList[id=910701].title
   limit: do 40 znaków
   EN: District 20 Backstreets
   PL:
869. [Rozdziały, etapy i zdolności Dantego [910701] — miejsce] 메피스토펠레스 내부
   źródło: StageNode91-7.json :: dataList[id=910701].place
   (powtórzenie elementu 792 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
870. [Rozdziały, etapy i zdolności Dantego [910701] — opis] T사의 뒷골목 초입을 지나온 지 얼마나 되었을까.\n이미 차창 밖은 이전보다도 더욱 색채가 사라져, 흐릿한 회색의 공간이 된 것만 같다.\n함께 창 밖을 내다보던 히스클리프의 미간이 찌푸러진다.
   źródło: StageNode91-7.json :: dataList[id=910701].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It's been a while since we entered the T Corp. Backstreets...\nThe deeper we go into the Backstreets, the world outside the bus becomes increasingly colorless.\nHeathcliff, who's been looking out the window for a while, suddenly furrows his brow.
   PL:
871. [Rozdziały, etapy i zdolności Dantego [910702] — tytuł] 항쟁
   źródło: StageNode91-7.json :: dataList[id=910702].title
   limit: do 40 znaków
   EN: Strife
   PL:
872. [Rozdziały, etapy i zdolności Dantego [910702] — miejsce] T사 뒷골목 어딘가
   źródło: StageNode91-7.json :: dataList[id=910702].place
   limit: do 40 znaków
   EN: Backstreets of T Corp.
   PL:
873. [Rozdziały, etapy i zdolności Dantego [910702] — opis] 버스에서 내리자마자 눈에 들어온 것은, 검은 옷을 나풀대며 칼자루를 쥐고 싸우는 무리들이었다.\n한쪽은 조금 시끄럽게, 또 한쪽은 열세에 놓여서 인지는 모르겠지만 무겁고 탁한 모습이었다.\n대체 이들에게서 우리가 무얼 얻어야 하는 걸까.
   źródło: StageNode91-7.json :: dataList[id=910702].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The first thing we noticed the moment we disembarked the bus was a crowd of swordsmen, all garbed in black cloaks, engaged in a fierce battle.\nOne side was loud and bustling, while the other side was quiet and somber. Perhaps the latter side was losing...\nWhat could we possibly have to gain from this?
   PL:
874. [Rozdziały, etapy i zdolności Dantego [910703] — tytuł] 검을 다루는 계
   źródło: StageNode91-7.json :: dataList[id=910703].title
   limit: do 40 znaków
   EN: Lineage of Blades
   PL:
875. [Rozdziały, etapy i zdolności Dantego [910703] — miejsce] 메피스토펠레스 내부
   źródło: StageNode91-7.json :: dataList[id=910703].place
   (powtórzenie elementu 792 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
876. [Rozdziały, etapy i zdolności Dantego [910703] — opis] 상처를 입고 정신을 잃은 자를 버스에 태웠다.\n베르길리우스에게 한 소리 듣긴 했지만… 이 방식이 맞을 것 같다는 생각이 들었으니까, 끝까지 가보려고 한다.\n…마침, 그자가 정신을 차린 것 같다.
   źródło: StageNode91-7.json :: dataList[id=910703].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We brought the wounded woman aboard the bus.\nVergilius was none to happy about it, but... I'm pretty confident in my decision. I will see this through to the end.\n... Looks like she's waking up.
   PL:
877. [Rozdziały, etapy i zdolności Dantego [910704] — tytuł] 초대하진 않았던 자
   źródło: StageNode91-7.json :: dataList[id=910704].title
   limit: do 40 znaków
   EN: The Uninvited
   PL:
878. [Rozdziały, etapy i zdolności Dantego [910704] — miejsce] 메피스토펠레스 내부
   źródło: StageNode91-7.json :: dataList[id=910704].place
   (powtórzenie elementu 792 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
879. [Rozdziały, etapy i zdolności Dantego [910704] — opis] 돌아온 버스에는 본 적도 없지만, 어딘가 눈에 밟히는 구석이 있는 사람이 앉아 있었다.\n옷의 색이 파랗고, 조금 다른 조끼를 입고 있었다면… 떠오를 법한 인물들이 몇몇 있을 것만도 같다.\n베르길리우스는 이 자를 왜 버스에 탑승시켰을까?
   źródło: StageNode91-7.json :: dataList[id=910704].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When we returned to the bus, an oddly familiar yet previously unacquainted person was waiting for us.\nIf she was wearing a blue uniform, a slightly different looking vest... she would have reminded me of some people we've met before.\nWhy did Vergilius let her board the bus?
   PL:
880. [Rozdziały, etapy i zdolności Dantego [910705] — tytuł] 용진 빌딩을 향해
   źródło: StageNode91-7.json :: dataList[id=910705].title
   limit: do 40 znaków
   EN: To Yong-jin Building
   PL:
881. [Rozdziały, etapy i zdolności Dantego [910705] — miejsce] T사 뒷골목 어딘가
   źródło: StageNode91-7.json :: dataList[id=910705].place
   (powtórzenie elementu 872 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
882. [Rozdziały, etapy i zdolności Dantego [910705] — opis] 상부, 림버스 컴퍼니의 요구는 ‘용진 빌딩’이라는 곳에서 뒤틀림에 관련된 것을 회수하는 것이었다.\n황금가지를 되찾는 일과의 관련성은 찾을 수 없지만, 회사에서 시키는 일에 어느 정도의 강제성이 있음을 어렴풋이 알 것만도 같다.\n그런데…\n베르길리우스는 목표가 애초에 그곳이었다는 걸 알고 있었던 것 같다. 왜 굳이 이렇게 돌아가게 만들었지?
   źródło: StageNode91-7.json :: dataList[id=910705].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Orders came from the higher-ups of Limbus Company that we are to retrieve a Distortion-related artifact from this 'Yong-jin Building'.\nI'm not sure how this is related to retrieving the Golden Boughs, but I'm starting to feel that none of us really have much say in the matter anyway.\nIt seemed to me that Vergilius already knew where we were headed. What was the point in not telling us and letting us go through a roundabout route?
   PL:
883. [Rozdziały, etapy i zdolności Dantego [910706] — tytuł] 용진 빌딩을 향해 2
   źródło: StageNode91-7.json :: dataList[id=910706].title
   limit: do 40 znaków
   EN: To Yong-jin Building 2
   PL:
884. [Rozdziały, etapy i zdolności Dantego [910706] — miejsce] T사 뒷골목 어딘가
   źródło: StageNode91-7.json :: dataList[id=910706].place
   (powtórzenie elementu 872 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
885. [Rozdziały, etapy i zdolności Dantego [910706] — opis] 상부, 림버스 컴퍼니의 요구는 ‘용진 빌딩’이라는 곳에서 뒤틀림에 관련된 것을 회수하는 것이었다.\n황금가지를 되찾는 일과의 관련성은 찾을 수 없지만, 회사에서 시키는 일에 어느 정도의 강제성이 있음을 어렴풋이 알 것만도 같다.\n그런데…\n베르길리우스는 목표가 애초에 그곳이었다는 걸 알고 있었던 것 같다. 왜 굳이 이렇게 돌아가게 만들었지?
   źródło: StageNode91-7.json :: dataList[id=910706].desc
   (powtórzenie elementu 882 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
886. [Rozdziały, etapy i zdolności Dantego [910707] — tytuł] 김삿갓과 친우들
   źródło: StageNode91-7.json :: dataList[id=910707].title
   limit: do 40 znaków
   EN: Mentor and Fellows
   PL:
887. [Rozdziały, etapy i zdolności Dantego [910707] — miejsce] 용진 빌딩
   źródło: StageNode91-7.json :: dataList[id=910707].place
   limit: do 40 znaków
   EN: Yong-jin Building
   PL:
888. [Rozdziały, etapy i zdolności Dantego [910707] — opis] 앵두는 여전히 우두머리… 김삿갓이라는 인물을 찾기 위해 허겁지겁 빌딩의 적들을 제거해나가고 있다.\n아직 다친 곳이 완전히 회복 되지도 않았을 텐데… 저건 분명 집념이라는 것이겠지.\n대체 김삿갓이라는 사람은 어떤 자였을까.
   źródło: StageNode91-7.json :: dataList[id=910707].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Aeng-du is cutting enemies down left and right in her desperate search for the mentor... this Bamboo-hatted Kim.\nI'm pretty sure her wounds are far from healed... I suppose she's just that determined.\nIt makes me wonder, though. What was Bamboo-hatted Kim like?
   PL:
889. [Rozdziały, etapy i zdolności Dantego [910708] — tytuł] 김삿갓과 친우들 2
   źródło: StageNode91-7.json :: dataList[id=910708].title
   limit: do 40 znaków
   EN: Mentor and Fellows 2
   PL:
890. [Rozdziały, etapy i zdolności Dantego [910708] — miejsce] 용진 빌딩
   źródło: StageNode91-7.json :: dataList[id=910708].place
   (powtórzenie elementu 887 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
891. [Rozdziały, etapy i zdolności Dantego [910708] — opis] 앵두는 여전히 우두머리… 김삿갓이라는 인물을 찾기 위해 허겁지겁 빌딩의 적들을 제거해나가고 있다.\n아직 다친 곳이 완전히 회복 되지도 않았을 텐데… 저건 분명 집념이라는 것이겠지.\n대체 김삿갓이라는 사람은 어떤 자였을까.
   źródło: StageNode91-7.json :: dataList[id=910708].desc
   (powtórzenie elementu 888 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
892. [Rozdziały, etapy i zdolności Dantego [910709] — tytuł] 죄의 근원
   źródło: StageNode91-7.json :: dataList[id=910709].title
   limit: do 40 znaków
   EN: Origin of Sin
   PL:
893. [Rozdziały, etapy i zdolności Dantego [910709] — miejsce] 용진 빌딩
   źródło: StageNode91-7.json :: dataList[id=910709].place
   (powtórzenie elementu 887 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
894. [Rozdziały, etapy i zdolności Dantego [910709] — opis] 끈적거리는 우울한 감각과 불타오르는 것만 같은 분노의 감각이 머리통을 아찔하게 만든다.\n왜 이런 곳에서 죄종의 반응이 나타나는 거지…?\n게다가…\n항상 느껴왔던 수준의 반응과는… 달라.
   źródło: StageNode91-7.json :: dataList[id=910709].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Thick, hazy gloom. Burning wrath. My head spins from the sheer intensity of these overwhelming sensations.\nWhy am I sensing the Peccatula here...?\nAnd...\nThese sensations are far stronger than what I usually feel from these Peccatula...!
   PL:
895. [Rozdziały, etapy i zdolności Dantego [910710] — tytuł] 검은 구름
   źródło: StageNode91-7.json :: dataList[id=910710].title
   limit: do 40 znaków
   EN: Dark Cloud
   PL:
896. [Rozdziały, etapy i zdolności Dantego [910710] — miejsce] 용진 빌딩
   źródło: StageNode91-7.json :: dataList[id=910710].place
   (powtórzenie elementu 887 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
897. [Rozdziały, etapy i zdolności Dantego [910710] — opis] 빌딩의 끝, 6층에 도착하니 누군가가 초조하게 회중시계를 내려다보고 있었다.\n커다란 검에 팔을 걸친 채, 인상을 잔뜩 쓴 모습.\n굳이 묻지 않더라도, 우리가 쓰러트리고 올라온 흑운회의 책임자 정도는 될 것이다.
   źródło: StageNode91-7.json :: dataList[id=910710].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We finally arrived at the top floor of the building, the 6th floor. There, a nervous-looking man was checking his pocket watch.\nHe carries a large sword and wears a nasty scowl...\nThis guy has to be the leader of the gang of Kurokumo Clan henchmen we've defeated along the way.
   PL:
898. [Rozdziały, etapy i zdolności Dantego [910711] — tytuł] 김삿갓
   źródło: StageNode91-7.json :: dataList[id=910711].title
   limit: do 40 znaków
   EN: Bamboo-hatted Kim
   PL:
899. [Rozdziały, etapy i zdolności Dantego [910711] — miejsce] 용진 빌딩
   źródło: StageNode91-7.json :: dataList[id=910711].place
   (powtórzenie elementu 887 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
900. [Rozdziały, etapy i zdolności Dantego [910711] — opis] 마침내 우리는 앵두가 우두머리라고 부르던 자를 마주했다.\n비스듬히 쓴 삿갓의 부서진 틈새 사이로, 푸른 빛의 시린 안광이 스멀스멀 흘러 나오고 있다.\n…싸움을 피하기는 어려워 보인다.
   źródło: StageNode91-7.json :: dataList[id=910711].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We finally came face-to-face with Aeng-du's mentor.\nCold blue light from his eye seeps past the crack of a slanted bamboo hat.\n... He won't go down without a fight.
   PL:
901. [Rozdziały, etapy i zdolności Dantego [910712] — tytuł] 검귀의 심상
   źródło: StageNode91-7.json :: dataList[id=910712].title
   limit: do 40 znaków
   EN: A Blade Fiend's Fathoms
   PL:
902. [Rozdziały, etapy i zdolności Dantego [910712] — miejsce] 심상 거울 던전
   źródło: StageNode91-7.json :: dataList[id=910712].place
   limit: do 50 znaków
   EN: Mirror Dungeon of the Fathoms
   PL:

## Rozdziały, etapy i zdolności Dantego: StageNode91-8
- plik gry: `StageNode91-8.json`

903. [Rozdziały, etapy i zdolności Dantego [910801] — tytuł] 제3회 발푸르기스의 밤
   źródło: StageNode91-8.json :: dataList[id=910801].title
   limit: do 40 znaków
   EN: The 3rd Walpurgis Night
   PL:
904. [Rozdziały, etapy i zdolności Dantego [910803] — tytuł] 제3회 발푸르기스의 밤
   źródło: StageNode91-8.json :: dataList[id=910803].title
   (powtórzenie elementu 903 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: StageNode91-9
- plik gry: `StageNode91-9.json`

905. [Rozdziały, etapy i zdolności Dantego [910901] — tytuł] 시간세 스캔들
   źródło: StageNode91-9.json :: dataList[id=910901].title
   limit: do 40 znaków
   EN: A Scandal in Time
   PL:
906. [Rozdziały, etapy i zdolności Dantego [910901] — miejsce] T사 골목 어딘가
   źródło: StageNode91-9.json :: dataList[id=910901].place
   limit: do 40 znaków
   EN: Alleyways of T Corp.
   PL:
907. [Rozdziały, etapy i zdolności Dantego [910902] — tytuł] 시간 관리국의 직원
   źródło: StageNode91-9.json :: dataList[id=910902].title
   limit: do 40 znaków
   EN: The Visit from T Corp.
   PL:
908. [Rozdziały, etapy i zdolności Dantego [910902] — miejsce] T사 골목 어딘가
   źródło: StageNode91-9.json :: dataList[id=910902].place
   (powtórzenie elementu 906 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
909. [Rozdziały, etapy i zdolności Dantego [910903] — tytuł] 교수대의 정체
   źródło: StageNode91-9.json :: dataList[id=910903].title
   limit: do 40 znaków
   EN: A Case of the Gallows
   PL:
910. [Rozdziały, etapy i zdolności Dantego [910903] — miejsce] T사 시간 관리국 사무실
   źródło: StageNode91-9.json :: dataList[id=910903].place
   limit: do 50 znaków
   EN: T Corp. Bureau of Time Admin. Office
   PL:
911. [Rozdziały, etapy i zdolności Dantego [910904] — tytuł] 세 명의 탐정
   źródło: StageNode91-9.json :: dataList[id=910904].title
   limit: do 60 znaków
   EN: The Adventure of the Three Detectives
   PL:
912. [Rozdziały, etapy i zdolności Dantego [910904] — miejsce] T사 시간 관리국 사무실
   źródło: StageNode91-9.json :: dataList[id=910904].place
   (powtórzenie elementu 910 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
913. [Rozdziały, etapy i zdolności Dantego [910905] — tytuł] 시간살인의 수수께끼
   źródło: StageNode91-9.json :: dataList[id=910905].title
   limit: do 40 znaków
   EN: Timekilling Puzzle
   PL:
914. [Rozdziały, etapy i zdolności Dantego [910905] — miejsce] T사 시계 공장
   źródło: StageNode91-9.json :: dataList[id=910905].place
   limit: do 40 znaków
   EN: T Corp. Watch Factory
   PL:
915. [Rozdziały, etapy i zdolności Dantego [910906] — tytuł] 하얀 스카프 연맹
   źródło: StageNode91-9.json :: dataList[id=910906].title
   limit: do 40 znaków
   EN: The White-scarved League
   PL:
916. [Rozdziały, etapy i zdolności Dantego [910906] — miejsce] T사 시계 공장
   źródło: StageNode91-9.json :: dataList[id=910906].place
   (powtórzenie elementu 914 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
917. [Rozdziały, etapy i zdolności Dantego [910907] — tytuł] 되감기 시계
   źródło: StageNode91-9.json :: dataList[id=910907].title
   limit: do 40 znaków
   EN: The Rewinding Clock
   PL:
918. [Rozdziały, etapy i zdolności Dantego [910907] — miejsce] T사 골목 어딘가
   źródło: StageNode91-9.json :: dataList[id=910907].place
   (powtórzenie elementu 906 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
919. [Rozdziały, etapy i zdolności Dantego [910908] — tytuł] 실종된 흔적
   źródło: StageNode91-9.json :: dataList[id=910908].title
   limit: do 40 znaków
   EN: A Trail Gone Cold
   PL:
920. [Rozdziały, etapy i zdolności Dantego [910908] — miejsce] 음습한 T사 골목
   źródło: StageNode91-9.json :: dataList[id=910908].place
   limit: do 40 znaków
   EN: Dark Alleyways of T Corp.
   PL:
921. [Rozdziały, etapy i zdolności Dantego [910909] — tytuł] 빈사의 탐정
   źródło: StageNode91-9.json :: dataList[id=910909].title
   limit: do 40 znaków
   EN: The Dying Detective
   PL:
922. [Rozdziały, etapy i zdolności Dantego [910909] — miejsce] 유로지비 비밀 아지트
   źródło: StageNode91-9.json :: dataList[id=910909].place
   limit: do 40 znaków
   EN: Yurodiviye Hideout
   PL:
923. [Rozdziały, etapy i zdolności Dantego [910910] — tytuł] 유로지비의 비밀
   źródło: StageNode91-9.json :: dataList[id=910910].title
   limit: do 40 znaków
   EN: The Yurodiviye Mystery
   PL:
924. [Rozdziały, etapy i zdolności Dantego [910910] — miejsce] 유로지비 비밀 아지트
   źródło: StageNode91-9.json :: dataList[id=910910].place
   (powtórzenie elementu 922 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
925. [Rozdziały, etapy i zdolności Dantego [910911] — tytuł] 묘한 감상평
   źródło: StageNode91-9.json :: dataList[id=910911].title
   limit: do 40 znaków
   EN: An Odd Impression
   PL:
926. [Rozdziały, etapy i zdolności Dantego [910911] — miejsce] 음습한 T사 골목
   źródło: StageNode91-9.json :: dataList[id=910911].place
   (powtórzenie elementu 920 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
927. [Rozdziały, etapy i zdolności Dantego [910912] — tytuł] 시간 살인마
   źródło: StageNode91-9.json :: dataList[id=910912].title
   limit: do 40 znaków
   EN: The Time Ripper
   PL:
928. [Rozdziały, etapy i zdolności Dantego [910912] — miejsce] 음습한 T사 골목
   źródło: StageNode91-9.json :: dataList[id=910912].place
   (powtórzenie elementu 920 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
929. [Rozdziały, etapy i zdolności Dantego [910913] — tytuł] 삐뚤어진 시간
   źródło: StageNode91-9.json :: dataList[id=910913].title
   limit: do 40 znaków
   EN: Twisted Time
   PL:
930. [Rozdziały, etapy i zdolności Dantego [910913] — miejsce] T사 골목 어딘가
   źródło: StageNode91-9.json :: dataList[id=910913].place
   (powtórzenie elementu 906 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
931. [Rozdziały, etapy i zdolności Dantego [910914] — tytuł] 공포의 시계탑
   źródło: StageNode91-9.json :: dataList[id=910914].title
   limit: do 40 znaków
   EN: The Clock Tower of Fear
   PL:
932. [Rozdziały, etapy i zdolności Dantego [910914] — miejsce] 시계탑
   źródło: StageNode91-9.json :: dataList[id=910914].place
   limit: do 40 znaków
   EN: Clock Tower
   PL:
933. [Rozdziały, etapy i zdolności Dantego [910915] — tytuł] 마지막 사건
   źródło: StageNode91-9.json :: dataList[id=910915].title
   limit: do 40 znaków
   EN: The Final Problem
   PL:
934. [Rozdziały, etapy i zdolności Dantego [910915] — miejsce] 심상 거울 던전
   źródło: StageNode91-9.json :: dataList[id=910915].place
   (powtórzenie elementu 902 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: StagePartText
- plik gry: `StagePartText.json`

935. [Rozdziały, etapy i zdolności Dantego [part_1] — tytuł części] 지옥
   źródło: StagePartText.json :: dataList[id=part_1].parttitle
   limit: do 40 znaków
   EN: Inferno
   PL:
936. [Rozdziały, etapy i zdolności Dantego [part_2] — tytuł części] 천국
   źródło: StagePartText.json :: dataList[id=part_2].parttitle
   limit: do 40 znaków
   EN: Paradiso
   PL:
937. [Rozdziały, etapy i zdolności Dantego [part_91] — tytuł części] 외전
   źródło: StagePartText.json :: dataList[id=part_91].parttitle
   limit: do 40 znaków
   EN: Deviazione
   PL:

## Rozdziały, etapy i zdolności Dantego: StageStatisticUIText
- plik gry: `StageStatisticUIText.json`

938. [Rozdziały, etapy i zdolności Dantego [stage_statistic_title] — tekst] 클리어 통계
   źródło: StageStatisticUIText.json :: dataList[id=stage_statistic_title].content
   limit: do 120 znaków
   EN: Clear Statistics
   PL:
939. [Rozdziały, etapy i zdolności Dantego [stage_statistic_popup_no_data] — tekst] 클리어 정보가 없습니다.
   źródło: StageStatisticUIText.json :: dataList[id=stage_statistic_popup_no_data].content
   limit: do 120 znaków
   EN: No clear info found.
   PL:
940. [Rozdziały, etapy i zdolności Dantego [formation_code_popup_copy_only_desc] — tekst] 편성 코드를 복사하여 불러올 수 있습니다.
   źródło: StageStatisticUIText.json :: dataList[id=formation_code_popup_copy_only_desc].content
   limit: do 120 znaków
   EN: Team Codes can be copied and pasted to load the Team loadouts.
   PL:
