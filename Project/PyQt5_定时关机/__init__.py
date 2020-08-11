
'''
QLineEdit(校验器)
如限制器只能输入整数、浮点数或者满足一定条件的字符串
'''

import sys,os,time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

hour= 0
min = 0

class PyQt5_Shutdown_DEMO(QWidget):
    def __init__(self):
        super(PyQt5_Shutdown_DEMO, self).__init__()
        self.initUI()

    def initUI(self):
        #创建两个按钮
        pushButton1 = QPushButton('确定')
        pushButton2 = QPushButton('取消定时关机')
        pushButton1.clicked.connect(self.buttonChanged)
        pushButton2.clicked.connect(self.buttonNO)
        #创建目标时间标签
        nameLabel1 = QLabel('&目标时间:')
        timeLabel = QLabel(' : ')
        edit_time1 = QLineEdit()
        edit_time2 = QLineEdit()
        #设置校验器
        intvalidator = QIntValidator(self)
        intvalidator.setRange(1,24)
        #添加目标时间Edit
        edit_time1.setValidator(intvalidator)
        edit_time2.setValidator(intvalidator)
        nameLabel1.setBuddy(edit_time1)
        #添加edit槽
        edit_time1.textChanged.connect(self.textChanged1)
        edit_time2.textChanged.connect(self.textChanged2)

        nameLabel2 = QLabel('时间:')
        timeEdit = QDateTimeEdit(QTime.currentTime(), self)
        timeEdit.setDisplayFormat("HH:mm:ss")

        #创建图片标签
        label = QLabel(self)
        #label3居中对齐
        label.setAlignment(Qt.AlignCenter)
        #设置提示文本
        label.setToolTip('这是一个图片标签')
        #设置标签3为图片
        label.setPixmap(QPixmap("./images/!face.png"))
        #创建栅格布局
        gridLayout = QGridLayout(self)
        #将控件添加到gridLayout
        gridLayout.addWidget(label, 0,0,10,10)
        gridLayout.addWidget(nameLabel2, 0, 10, 1, 1)
        gridLayout.addWidget(timeEdit, 0, 11, 1, 1)
        gridLayout.addWidget(nameLabel1,1,10,1,1)
        gridLayout.addWidget(edit_time1,2,10,1,1)
        gridLayout.addWidget(timeLabel, 2,11,1,1)
        gridLayout.addWidget(edit_time2, 2,11,1,1)

        gridLayout.addWidget(pushButton2, 3,10,1,1)
        gridLayout.addWidget(pushButton1,3,11,1,1)

        self.setLayout(gridLayout)
        self.setWindowTitle('定时关机程序')
        self.resize(930, 691)
        # 设置应用图标
        self.setWindowIcon(QIcon('./images/初音.ico'))
    
    def textChanged1(self,text):
        print('输入的内容'+ text)
        global hour
        hour = text
    def textChanged2(self,text):
        print('输入的内容'+ text)
        global min
        min = text
    def buttonChanged(self):
        if int(hour)<=24 and int(min)<=60:
            qtimeObj = QTime.currentTime()
            strTime1 = qtimeObj.toString("h")
            strTime2 = qtimeObj.toString("m")
            SET_hour = int(hour) - int(strTime1)
            SET_min = int(min) - int(strTime2)
            print(f'hour:{hour} + min:{min}')
            print(f'{strTime1}:{strTime2}')
            print(f'Set_hour:{SET_hour} + Set_min:{SET_min}')
            settime = SET_hour*3600+SET_min*60
            os.system(f'shutdown -s -t {settime}')
    def buttonNO(self):
        os.system('shutdown /a')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建一个窗口
    main = PyQt5_Shutdown_DEMO()
    # 显示窗口
    main.show()
    # 进入程序的主循环、并通过exit函数确保主函数安全结束
    sys.exit(app.exec_())