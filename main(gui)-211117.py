import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pickle
import random
import datetime


# 리소스 변환(터미널 실행) pyrcc5 resource.qrc -o resource_rc.py
form_class = uic.loadUiType("bartender.ui")[0]

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
재료 = {'보드카': 1, '진': 1, '자몽주스': 1, '베르무트': 1, '토닉워터': 1, '오렌지주스': 1, '크렌베리주스': 1, '깔루아': 1,
          '우유': 1}  # 재료수량 추가시 수정하고 19,20번째 로드 부분 (#)처리
메뉴가능 = {'솔티독': 1, '그레이하운드': 1, '시브리즈': 1, '스크루드라이버': 1, '블랙러시안': 1, '화이트러시안': 1, '마티니': 1, '진토닉': 1, '오렌지블로섬': 1}
메뉴수량 = {'솔티독': 0, '그레이하운드': 0, '시브리즈': 0, '스크루드라이버': 0, '블랙러시안': 0, '화이트러시안': 0, '마티니': 0, '진토닉': 0, '오렌지블로섬': 0}

한영변환_칵테일 = {'솔티독': 'saltidog', '그레이하운드': 'greyhound', '시브리즈': 'seabreeze', '스크루드라이버': 'screwdriver', '블랙러시안': 'blackrussian', '화이트러시안': 'whiterussian', '마티니': 'martini', '진토닉': 'gintonic', '오렌지블로섬': 'orangeblossom'}
한영변환_재료 = {'보드카': 'vodka', '진': 'gin', '자몽주스': 'grapefruit_juice', '베르무트': 'vermouth', '토닉워터': 'tonicwater', '오렌지주스': 'orange_juice', '크렌베리주스': 'cranberry_juice', '깔루아': 'kahlua', '우유': 'milk'}

기록 = {}
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# 재료 처음 세팅

        fx = open('재료.txt', 'rb')  # 재료 코드 수정시 로드X
        재료 = pickle.load(fx)  # 재료 코드 수정시 로드X
        if 재료['보드카'] == 1: #메니저모드 재료 라디오버튼 세팅
            self.rb_vodka_t.setChecked(True)
        else :
            self.rb_vodka_f.setChecked(True)
        if 재료['진'] == 1:
            self.rb_gin_t.setChecked(True)
        else :
            self.rb_gin_f.setChecked(True)
        if 재료['자몽주스'] == 1:
            self.rb_grapefruit_juice_t.setChecked(True)
        else :
            self.rb_grapefruit_juice_f.setChecked(True)
        if 재료['베르무트'] == 1:
            self.rb_vermouth_t.setChecked(True)
        else :
            self.rb_vermouth_f.setChecked(True) 
        if 재료['토닉워터'] == 1:
            self.rb_tonicwater_t.setChecked(True)
        else :
            self.rb_tonicwater_f.setChecked(True)
        if 재료['오렌지주스'] == 1:
            self.rb_orange_juice_t.setChecked(True)
        else :
            self.rb_orange_juice_f.setChecked(True)
        if 재료['크렌베리주스'] == 1:
            self.rb_cranberry_juice_t.setChecked(True)
        else :
            self.rb_cranberry_juice_f.setChecked(True)
        if 재료['깔루아'] == 1:
            self.rb_kahlua_t.setChecked(True)
        else :
            self.rb_kahlua_f.setChecked(True)
        if 재료['우유'] == 1:
            self.rb_milk_t.setChecked(True)
        else :
            self.rb_milk_f.setChecked(True)

# 주문기록 불러오기
#        fy = open('기록.txt', 'rb')  # 기록 수정시 로드X
#        기록 = pickle.load(fy)  # 기록 수정시 로드X

# 주문가능 여부 확인 및 버튼활성화(추후 삭제?)
        self.source_reset()


# 개별 메뉴선택 버튼 클릭시 함수 연결
        self.bt_saltidog.clicked.connect(lambda: self.menuclick('솔티독'))
        self.bt_greyhound.clicked.connect(lambda: self.menuclick('그레이하운드'))
        self.bt_seabreeze.clicked.connect(lambda: self.menuclick('시브리즈'))
        self.bt_screwdriver.clicked.connect(lambda: self.menuclick('스크루드라이버'))
        self.bt_blackrussian.clicked.connect(lambda: self.menuclick('블랙러시안'))
        self.bt_whiterussian.clicked.connect(lambda: self.menuclick('화이트러시안'))
        self.bt_martini.clicked.connect(lambda: self.menuclick('마티니'))
        self.bt_gintonic.clicked.connect(lambda: self.menuclick('진토닉'))
        self.bt_orangeblossom.clicked.connect(lambda: self.menuclick('오렌지블로섬'))
        self.bt_allrandom.clicked.connect(lambda: self.menuclick_random('all'))
        self.bt_vodkarandom.clicked.connect(lambda: self.menuclick_random('vodkarandom'))
        self.bt_ginrandom.clicked.connect(lambda: self.menuclick_random('ginrandom'))

# 매니저 모드 재료 변경시 함수 연결
        self.rb_vodka_t.clicked.connect(lambda: self.rb_tc('보드카'))
        self.rb_vodka_f.clicked.connect(lambda: self.rb_fc('보드카'))
        self.rb_gin_t.clicked.connect(lambda: self.rb_tc('진'))
        self.rb_gin_f.clicked.connect(lambda: self.rb_fc('진'))
        self.rb_grapefruit_juice_t.clicked.connect(lambda: self.rb_tc('자몽주스'))
        self.rb_grapefruit_juice_f.clicked.connect(lambda: self.rb_fc('자몽주스'))
        self.rb_vermouth_t.clicked.connect(lambda: self.rb_tc('베르무트'))
        self.rb_vermouth_f.clicked.connect(lambda: self.rb_fc('베르무트'))
        self.rb_tonicwater_t.clicked.connect(lambda: self.rb_tc('토닉워터'))
        self.rb_tonicwater_f.clicked.connect(lambda: self.rb_fc('토닉워터'))
        self.rb_orange_juice_t.clicked.connect(lambda: self.rb_tc('오렌지주스'))
        self.rb_orange_juice_f.clicked.connect(lambda: self.rb_fc('오렌지주스'))
        self.rb_cranberry_juice_t.clicked.connect(lambda: self.rb_tc('크렌베리주스'))
        self.rb_cranberry_juice_f.clicked.connect(lambda: self.rb_fc('크렌베리주스'))
        self.rb_kahlua_t.clicked.connect(lambda: self.rb_tc('깔루아'))
        self.rb_kahlua_f.clicked.connect(lambda: self.rb_fc('깔루아'))
        self.rb_milk_t.clicked.connect(lambda: self.rb_tc('우유'))
        self.rb_milk_f.clicked.connect(lambda: self.rb_fc('우유'))
        self.bt_source_reset.clicked.connect(self.source_reset)

# 개별 메뉴선택 버튼 클릭시 함수
    def menuclick(self, bt_w) :
        메뉴수량[bt_w] += 1
        if bt_w == '솔티독' :
            self.bt_saltidog.setText(bt_w + ' : ' + str(메뉴수량[bt_w])) # 버튼에 수량 표시
        elif bt_w == '그레이하운드' :
            self.bt_greyhound.setText(bt_w + ' : ' + str(메뉴수량[bt_w]))
        elif bt_w == '시브리즈' :
            self.bt_seabreeze.setText(bt_w + ' : ' + str(메뉴수량[bt_w]))
        elif bt_w == '시브리즈' :
            self.bt_seabreeze.setText(bt_w + ' : ' + str(메뉴수량[bt_w]))
        elif bt_w == '스크루드라이버' :
            self.bt_screwdriver.setText(bt_w + ' : ' + str(메뉴수량[bt_w]))
        elif bt_w == '블랙러시안' :
            self.bt_blackrussian.setText(bt_w + ' : ' + str(메뉴수량[bt_w]))
        elif bt_w == '화이트러시안' :
            self.bt_whiterussian.setText(bt_w + ' : ' + str(메뉴수량[bt_w]))
        elif bt_w == '마티니' :
            self.bt_martini.setText(bt_w + ' : ' + str(메뉴수량[bt_w]))
        elif bt_w == '진토닉' :
            self.bt_gintonic.setText(bt_w + ' : ' + str(메뉴수량[bt_w]))
        elif bt_w == '오렌지블로섬' :
            self.bt_orangeblossom.setText(bt_w + ' : ' + str(메뉴수량[bt_w]))
        self.tb_order.setText('') # 주문 tb_order에 보여줌
        for k in 메뉴:
            if 메뉴수량[k] != 0:
                self.tb_order.append(str(k) + ' : ' + str(메뉴수량[k]))
     
    # 랜덤버튼 클릭           
    def menuclick_random(self, soul) :
        if soul == 'all' : #올랜덤
            랜덤가능=[] 
            for i in 메뉴가능:
                if 메뉴가능[i] == 1:
                    랜덤가능.append(i)
            랜덤선택=random.choice(랜덤가능)
            self.menuclick(랜덤선택)
        elif soul == 'vodkarandom' : #보드카랜덤
            보드카가능=[]
            보드카칵테일=[]
            랜덤가능=[]
            for i in 메뉴 :
                if 메뉴[i][0] == '보드카':
                    보드카칵테일.append(i)
            랜덤가능=[] 
            for i in 메뉴가능:
                if 메뉴가능[i] == 1:
                    랜덤가능.append(i)
            보드카가능 = list(set(보드카칵테일) & set(랜덤가능))
            보드카선택=random.choice(보드카가능)
            self.menuclick(보드카선택)
        elif soul == 'ginrandom' : #진랜덤
            진가능=[]
            진칵테일=[]
            랜덤가능=[]
            for i in 메뉴 :
                if 메뉴[i][0] == '진':
                    진칵테일.append(i)
            랜덤가능=[] 
            for i in 메뉴가능:
                if 메뉴가능[i] == 1:
                    랜덤가능.append(i)
            진가능 = list(set(진칵테일) & set(랜덤가능))
            진선택=random.choice(진가능)
            self.menuclick(진선택)

# 매니저 모드
# 처음 재료 세팅 함수
    def rb_tc(self, rbt_w) :
        재료[rbt_w] = 1
        f = open('재료.txt', 'wb')
        pickle.dump(재료, f)
        f.close()
    def rb_fc(self, rbf_w) :
        재료[rbf_w] = 0
        f = open('재료.txt', 'wb')
        pickle.dump(재료, f)
        f.close()
        
# 재료설정버튼 클릭시 메뉴가능한지 변환 함수 
    def source_reset(self): #menuableset 함수로 이름 변경 할지, 추후 버튼 삭제(재료 라디오버튼변경시 함수 실행), 프로그램실행시 함수로만 실행할지 고민
        가능 = []
        for i in 메뉴['솔티독']:
            가능.append(재료[i])
            if 0 in 가능:
                self.bt_saltidog.setEnabled(False)
                메뉴가능['솔티독'] = 0
            else:
                self.bt_saltidog.setEnabled(True)
                메뉴가능['솔티독'] = 1
        가능 = []        
        for i in 메뉴['그레이하운드']:
            가능.append(재료[i])
            if 0 in 가능:
                self.bt_greyhound.setEnabled(False)
                메뉴가능['그레이하운드'] = 0
            else:
                self.bt_greyhound.setEnabled(True)
                메뉴가능['그레이하운드'] = 1
        가능 = []        
        for i in 메뉴['시브리즈']:
            가능.append(재료[i])
            if 0 in 가능:
                self.bt_seabreeze.setEnabled(False)
                메뉴가능['시브리즈'] = 0
            else:
                self.bt_seabreeze.setEnabled(True)
                메뉴가능['시브리즈'] = 1
        가능 = []        
        for i in 메뉴['스크루드라이버']:
            가능.append(재료[i])
            if 0 in 가능:
                self.bt_screwdriver.setEnabled(False)
                메뉴가능['스크루드라이버'] = 0
            else:
                self.bt_screwdriver.setEnabled(True)
                메뉴가능['스크루드라이버'] = 1
        가능 = []        
        for i in 메뉴['블랙러시안']:
            가능.append(재료[i])
            if 0 in 가능:
                self.bt_blackrussian.setEnabled(False)
                메뉴가능['블랙러시안'] = 0
            else:
                self.bt_blackrussian.setEnabled(True)
                메뉴가능['블랙러시안'] = 1
        가능 = []        
        for i in 메뉴['화이트러시안']:
            가능.append(재료[i])
            if 0 in 가능:
                self.bt_whiterussian.setEnabled(False)
                메뉴가능['화이트러시안'] = 0
            else:
                self.bt_whiterussian.setEnabled(True)
                메뉴가능['화이트러시안'] = 1
        가능 = []        
        for i in 메뉴['마티니']:
            가능.append(재료[i])
            if 0 in 가능:
                self.bt_martini.setEnabled(False)
                메뉴가능['마티니'] = 0
            else:
                self.bt_martini.setEnabled(True)
                메뉴가능['마티니'] = 1
        가능 = []        
        for i in 메뉴['진토닉']:
            가능.append(재료[i])
            if 0 in 가능:
                self.bt_gintonic.setEnabled(False)
                메뉴가능['진토닉'] = 0
            else:
                self.bt_gintonic.setEnabled(True)
                메뉴가능['진토닉'] = 1
        가능 = []        
        for i in 메뉴['오렌지블로섬']:
            가능.append(재료[i])
            if 0 in 가능:
                self.bt_orangeblossom.setEnabled(False)
                메뉴가능['오렌지블로섬'] = 0
            else:
                self.bt_orangeblossom.setEnabled(True)
                메뉴가능['오렌지블로섬'] = 1

#주문완료 버튼시 함수
#주문 통계용 함수(될지 모르겠음)
    def statistics_write(self) :
       order_time = datetime.datetime.now().strftime('%Y년 %m월 %d일 %H시')
       order_menu = self.tb_order.toPlainText()
       기록[order_time] = order_menu
       fa = open('기록.txt', 'wb')
       pickle.dump(기록, fa)
       fa.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()