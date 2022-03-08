import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pickle


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

한영_bt = {'솔티독' : bt_saltidog} #클레스 안에 들어가야하는지 의문

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
# 재료 처음 세팅
        fx = open('재료.txt', 'rb')  # 재료 코드 수정시 로드X
        재료 = pickle.load(fx)  # 재료 코드 수정시 로드X
        if 재료['보드카'] == 1:
            self.rb_bodca_t.setChecked(True)
        else :
            self.rb_bodca_f.setChecked(True)

# 주문가능 여부 확인
        for i in 메뉴['솔티독'] :
            가능 = []
            가능.append(재료[i])
            if 0 in 가능 :
                self.bt_saltidog.setEnabled(False)
            else :
                self.bt_saltidog.setEnabled(True)

# 개별 메뉴선택 버튼 클릭시 함수 연결
        self.bt_saltidog.clicked.connect(self.menuclick('솔티독'))
        self.bt_grayhound.clicked.connect(self.menuclick_grayhound)
#        self.bt_ordersee.clicked.connect(self.menuclick_ordersee)

# 매니저 모드 재료 변경시 함수 연결
        self.rb_bodca_t.clicked.connect(self.rb_tc('보드카'))
        self.rb_bodca_f.clicked.connect(self.rb_fc('보드카'))

# 개별 메뉴선택 버튼 클릭시 함수
    # 보드카
    def menuclick(bt_w) :  #범용으로 수정해봄
        메뉴수량[bt_w] += 1
        self.한영_bt[bt_w].setText(bt_w,' : ' + str(메뉴수량[bt_w])) # 버튼에 수량 표시 #안되면globals()[한영[bt_w]]
        self.tb_order.setText('')
        for k in 메뉴:  # 주문 tb_order에 보여줌
            if 메뉴수량[k] != 0:
                self.tb_order.append(str(k) + ' : ' + str(메뉴수량[k]))

    def menuclick_grayhound(self) :
        메뉴수량['그레이하운드'] += 1
        self.bt_grayhound.setText('그레이하운드 : ' + str(메뉴수량['그레이하운드'])) # 버튼에 수량 표시
        self.tb_order.setText('')
        for k in 메뉴:  # 주문 tb_order에 보여줌
            if 메뉴수량[k] != 0:
                self.tb_order.append(str(k) + ' : ' + str(메뉴수량[k]))
#    def menuclick_ordersee(self) : #주문확인 필요 없음 보류
#       for k in 메뉴:  # 주문출력
#            if 메뉴수량[k] != 0:
#                self.tb_order.append(str(k) + ' : ' + str(메뉴수량[k]))

# 매니저 모드
# 재료 변경시 세팅 함수
    def rb_tc(rbt_w) :
        재료[tbt_w] = 1
        f = open('재료.txt', 'wb')
        pickle.dump(재료, f)
        f.close()
    def rb_fc(rbf_w) :
        재료[rbf_w] = 0
        f = open('재료.txt', 'wb')
        pickle.dump(재료, f)
        f.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()