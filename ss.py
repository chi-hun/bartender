기록 = {'ㄴㅇㄹㄷㄷㄹ' : 'ㅁㅁㅁ : 1, ㄴㄴㄴ : 2', 'dfwef' : 'ㅁㅁㅁ : 3, ㄴㄴㄴ : 4'}
메뉴 = {'ㅁㅁㅁ' : 'ㅁㄴㅇ', 'ㄴㄴㄴ':'ㅇㅇㅇ'}
기록_co_2 = list(기록.values())
기록_co_3 = []
기록_co_f = {}  # 메뉴키, 값(0)이 들어가 있는 딕셔너리 자동 만들기
for i in list(메뉴.keys()):
    기록_co_f[i] = 0
for i in range(len(기록_co_2)):
    기록_co_2_split = str(기록_co_2[i]).split(',')
    for j in range(len(기록_co_2_split)):
        기록_co_2_split2 = str(기록_co_2_split[j]).split(',')
        if 기록_co_2_split2[0][0] == ' ':
            기록_co_2_split3 = 기록_co_2_split2[0].replace(' ', '', 1)
        else:
            기록_co_2_split3 = 기록_co_2_split2[0]
        기록_co_3.append(기록_co_2_split3)
for i in 기록_co_3:
    기록_co_3_split = str(i).split(' : ')
    print(기록_co_3_split[0])
    기록_co_f[기록_co_3_split[0]] += int(기록_co_3_split[1])
print(기록_co_f)