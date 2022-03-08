# 구현할것들 : 통계(인물, 수량, 시간), 재료수량은 워드로 쓰고 읽게, 메뉴도?

# 기본값(매뉴, 재료 변경시 수정)
메뉴 = {'솔티독': ('보드카', '자몽주스'),
      '그레이하운드': ('보드카', '자몽주스'),
      '시브리즈': ('보드카', '크렌베리주스', '자몽주스'),
      '스크루드라이버': ('보드카', '오렌지주스'),
      '블랙러시안': ('보드카', '깔루아'),
      '화이트러시안': ('보드카', '깔루아', '우유'),
      '마티니': ('진', '베르무트'),
      '진토닉': ('진', '토닉워터'),
      '오렌지블로섬': ('진', '오렌지주스')}  # 칵테일종류 및 들어가는 재료
제조법 = {'솔티독': '보드카(1oz), 자몽주스(3oz), 스노우잔(소금), 빌드',
       '그레이하운드': '보드카(1oz), 자몽주스(가득), 빌드',
       '시브리즈': '보드카(1oz), 크렌베리주스(2oz), 자몽주스(0.5oz), 쉐이크',
       '스크루드라이버': '보드카(1.5oz), 오렌지주스(가득). 빌드',
       '블랙러시안': '보드카(2oz), 깔루아(1oz), 빌드',
       '화이트러시안': '보드카(2oz), 깔루아(1oz), 우유(1oz), 빌드',
       '마티니': '진(2oz), 베르무트(0.5oz), 스터',
       '진토닉': '진(1.5oz), 토닉워터(가득), 빌드',
       '오렌지블로섬': '진(1.5oz), 오렌지주스(1oz), 쉐이크'}
재료 = {'보드카': 1, '진': 1, '자몽주스': 1, '베르무트': 1, '토닉워터': 1, '오렌지주스': 1, '크렌베리주스': 1, '깔루아': 1, '우유': 1}  # 재료수량 추가시 수정하고 19,20번째 로드 부분 (#)처리
메뉴가능 = {'솔티독': 1, '그레이하운드': 1, '시브리즈': 1, '스크루드라이버': 1, '블랙러시안': 1, '화이트러시안': 1, '마티니': 1, '진토닉': 1, '오렌지블로섬': 1}
메뉴수량 = {'솔티독': 0, '그레이하운드': 0, '시브리즈': 0, '스크루드라이버': 0, '블랙러시안': 0, '화이트러시안': 0, '마티니': 0, '진토닉': 0, '오렌지블로섬': 0}

# 모드선택
mode = input('모드를 선택해주세요')

# 마스터 모드
if mode == '0':
    변경재료 = 0
    while 변경재료 != 'n':
        import pickle
       # fx = open('재료.txt', 'rb')  # 재료 코드 수정시 로드X
       # 재료 = pickle.load(fx)  # 재료 코드 수정시 로드X
        print(재료)
        변경재료 = input('변경을 원하는 재료를 입력하세요(취소:n)')
        if 변경재료 == 'n':
            continue
        변경재료수량 = input('상태를 입력하세요')
        변경확인 = input(변경재료 + " : " + 변경재료수량 + "이 맞습니까?(y/n)")
        if 변경확인 == 'y':
            재료[변경재료] = 변경재료수량
            f = open('재료.txt', 'wb')
            pickle.dump(재료, f)
            f.close()

# 메뉴판
for i in 메뉴:
    가능리스트 = []
    for j in 메뉴[i]:
        가능리스트.append(재료[j])
    if 0 in 가능리스트:
        메뉴색 = '\033[31m'
        메뉴가능[i] = 0
    else:
        메뉴색 = '\033[0m'
        메뉴가능[i] = 1
    print(메뉴색 + i + ", " + '\033[0m', end='')
print('')

# 주문
주문 = []
메뉴선택 = 0
while 메뉴선택 != 'fin':
    메뉴선택 = input('주문하세요(종료시:fin)')
    if 메뉴선택 not in 메뉴:
        if 메뉴선택 == 'fin':
            continue
        else:
            print('메뉴에서 골라주세요')
            continue
    if 메뉴가능[메뉴선택] == 0:
        print('재료가 부족합니다')
    else:
        주문.append(메뉴선택)
        메뉴수량[메뉴선택] += 1
for k in 메뉴:  # 주문출력
    if 메뉴수량[k] != 0:
        print(k, ':', 메뉴수량[k])
print('')
for l in 메뉴:  # 제조법출력
    if 메뉴수량[l] != 0:
        print(l, ':', 제조법[k])
