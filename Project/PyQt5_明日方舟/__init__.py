
'''
QLineEdit(校验器)
如限制器只能输入整数、浮点数或者满足一定条件的字符串
'''

import sys,os,time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
state=0
run_time=0
game_num=0
name="夏活副本"
def TIME_IT():
    global run_time
    global name
    global game_num
    global state
    print(f'次数：{game_num}'+f'   name；{name}' + f'   time:{run_time}')
    if state == 1:
        if game_num in range(1, 100):
            if name == "主线副本":
                if run_time ==0:
                    os.system(r'G:\MuMu\emulator\nemu\vmonitor\bin\adb_server.exe connect 127.0.0.1:7555')
                    os.system(r'G:\MuMu\emulator\nemu\vmonitor\bin\adb_server.exe shell input tap 1425 826')
                if run_time == 2:
                    os.system(r'G:\MuMu\emulator\nemu\vmonitor\bin\adb_server.exe shell input tap 1375 785')
                if run_time == 100:
                    os.system(r'G:\MuMu\emulator\nemu\vmonitor\bin\adb_server.exe shell input tap 725 262')
                if run_time == 104:
                    run_time = 0
                    game_num=game_num - 1
            elif name == "剿灭副本":
                if run_time == 0:
                    os.system(r'G:\MuMu\emulator\nemu\vmonitor\bin\adb_server.exe connect 127.0.0.1:7555')
                    os.system(r'G:\MuMu\emulator\nemu\vmonitor\bin\adb_server.exe shell input tap 1425 826')
                if run_time == 2:
                    os.system(r'G:\MuMu\emulator\nemu\vmonitor\bin\adb_server.exe shell input tap 1375 785')
                if run_time == 902:
                    os.system(r'G:\MuMu\emulator\nemu\vmonitor\bin\adb_server.exe shell input tap 725 262')
                if run_time == 907:
                    run_time = 0
                    game_num=game_num - 1
            elif name == "夏活副本":
                if run_time == 0:
                    os.system(r'G:\MuMu\emulator\nemu\vmonitor\bin\adb_server.exe connect 127.0.0.1:7555')
                    os.system(r'G:\MuMu\emulator\nemu\vmonitor\bin\adb_server.exe shell input tap 1425 826')
                if run_time == 1:
                    os.system(r'G:\MuMu\emulator\nemu\vmonitor\bin\adb_server.exe shell input tap 1375 785')
                if run_time == 130:
                    os.system(r'G:\MuMu\emulator\nemu\vmonitor\bin\adb_server.exe shell input tap 725 262')
                if run_time == 134:
                    run_time = 0
                    game_num=game_num - 1
        run_time = run_time + 1
    t = threading.Timer(1,TIME_IT)
    t.start()

t = threading.Timer(1, TIME_IT)
t.start()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("明日方舟_Breeezer_X")
        MainWindow.resize(728, 1029)
        MainWindow.setMaximumSize(QtCore.QSize(728, 1029))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 30, 171, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.currentIndexChanged.connect(self.AK_CB)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 920, 131, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.AK_OK)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 90, 99, 30))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 90, 113, 28))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(self.AK_edit)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 920, 131, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.AK_Stop)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(390, 40, 155, 25))
        self.radioButton.setObjectName("radioButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(510, 90, 113, 28))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setReadOnly(True)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 90, 99, 21))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 728, 34))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "明日方舟_Breeezer_X"))
        self.comboBox.setItemText(0, _translate("MainWindow", "夏活副本"))
        self.comboBox.setItemText(1, _translate("MainWindow", "剿灭副本"))
        self.comboBox.setItemText(2, _translate("MainWindow", "主线副本"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.label.setText(_translate("MainWindow", "次数:"))
        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.lineEdit_2.setText(_translate("MainWindow", "0"))
        self.pushButton_2.setText(_translate("MainWindow", "取消战斗"))
        self.radioButton.setText(_translate("MainWindow", "战斗中"))
        self.label_2.setText(_translate("MainWindow", "剩余次数:"))

    def AK_OK(self):
        global state
        global game_num
        if self.radioButton.isChecked() == False:
            self.radioButton.setChecked(True)
            state=1
            self.lineEdit_2.setText(f'{game_num}')
        else:
            print('None')
    def AK_Stop(self):
        self.radioButton.setChecked(False)
        self.lineEdit_2.setText("0")
        game_num=0
        state=0
        print('stop')
    def AK_edit(self,text):
        print('输入的内容:' + text)
        global game_num
        game_num=int(text)
    def AK_CB(self,i):
        global name
        #标签用来显示选中的文本
        print(self.comboBox.currentText())
        name=self.comboBox.currentText()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mianWindow = QMainWindow()
    #初始化类
    ui = Ui_MainWindow()
    # 每过3秒切换一次账号
    #向主窗口添加控件
    ui.setupUi(mianWindow)
    palette = QPalette()
    palette.setBrush(QPalette.Background, QBrush(QPixmap("./images/斯卡蒂_PS.png")))
    mianWindow.setPalette(palette)
    #主窗口显示
    mianWindow.show()
    #进入程序的主循环、并通过exit函数确保主函数安全结束
    sys.exit(app.exec_())