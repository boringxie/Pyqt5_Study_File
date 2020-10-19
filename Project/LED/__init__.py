# -*- coding: utf-8 -*-
'''
简易无接触温度测量与身份识别装置
'''
#coding:utf-8
import sys,cv2
import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from functools import partial
temp_l=28
temp_h=48
temp = 50
keil_state =0
edit_state =0
class FrameThread(QThread):
    imgLab = None
    device = None
    paizhao = 0

    """摄像头拍照线程，摄像头拍照耗时较长容易卡住UI"""

    def __init__(self, deviceIndex, imgLab):
        QThread.__init__(self)
        self.imgLab = imgLab
        self.deviceIndex = deviceIndex
        self.device = cv2.VideoCapture(self.deviceIndex)  # 从摄像头中取得视频
        self.device.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
        self.device.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

    def run(self):
        if self.device.isOpened():
            try:
                while True:
                    ret, frame = self.device.read()
                    height, width, bytesPerComponent = frame.shape
                    bytesPerLine = bytesPerComponent * width
                    # 变换彩色空间顺序
                    cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)
                    # 转为QImage对象
                    image = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
                    if self.paizhao == 1:
                        image.save(".\\" + str(self.deviceIndex) + ".jpg")
                        self.paizhao = 0
                        print('1')
                    pixmap = QPixmap.fromImage(image)
                    pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)
                    self.imgLab.setPixmap(pixmap)
            finally:
                self.device.release()

class StackedExample(QWidget):
    def __init__(self):
        self.img = np.ndarray(())
        super(StackedExample, self).__init__()
        self.painter = QPainter()
        self.setGeometry(300, 50, 10, 10)
        self.setWindowTitle('简易无接触温度测量与身份识别装置')

        self.list = QListWidget()
        self.list.insertItem(0,'非接触测温')
        self.list.insertItem(1,'身份识别')
        self.list.insertItem(2,'检测口罩')
        self.list.insertItem(3, '身份识别')

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.stack4 = QWidget()

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()

        self.stack = QStackedWidget()
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)
        self.stack.addWidget(self.stack4)

        hbox = QHBoxLayout()
        hbox.addWidget(self.list)
        hbox.addWidget(self.stack)
        self.setLayout(hbox)

        self.list.currentRowChanged.connect(self.display)
    def tab1UI(self):
        hbox = QHBoxLayout(self)
        Vlayout = QVBoxLayout()
        lb1 = QLabel(self)
        btn = QPushButton(self)
        btn2 = QRadioButton(self)
        btn2.setStyleSheet("QRadioButton::indicator {width:22px;height:22px;border-radius:7px}"
                      "QRadioButton::indicator:checked {background-color:green;}"
                      "QRadioButton::indicator:unchecked {background-color:red;}"
                      );
        btn2.setEnabled(False)
        if temp in range(temp_l,temp_h) :
            btn2.setChecked(True)
        else:
            btn2.setChecked(False)
        btn2.setText("高温警报")
        btn.setText("测温")
        btn.clicked.connect(self.paizhao)

        self.frameThread = FrameThread(0, lb1)
        self.frameThread.start()
        Vlayout.addWidget(btn)
        Vlayout.addWidget(btn2)
        hbox.addWidget(lb1)
        hbox.addLayout(Vlayout)
        self.stack1.setLayout(hbox)

    def tab2UI(self):
        Vlayout = QVBoxLayout()
        Hlayout = QHBoxLayout()
        btn = QPushButton(self)
        btn1 = QPushButton(self)
        lb2 = QLabel(self)
        btn.setText("处理")
        btn1.setText("确定")
        btn.clicked.connect(partial(self.keil,lb2))
        btn1.clicked.connect(self.keil_ok)
        Vlayout.addWidget(btn)
        Vlayout.addWidget(btn1)
        Hlayout.addWidget(lb2)
        Hlayout.addLayout(Vlayout)
        self.stack2.setLayout(Hlayout)

    def tab3UI(self):
        Vlayout = QVBoxLayout()
        Hlayout = QHBoxLayout()
        btn2 = QRadioButton(self)
        btn3 = QPushButton(self)
        lb3 = QLabel(self)
        btn2.setText("编辑")
        btn3.setText("确定")
        btn2.clicked.connect(partial(self.edit_read, lb3,btn2))
        btn3.clicked.connect(self.keil_ok)
        Vlayout.addWidget(btn2)
        Vlayout.addWidget(btn3)
        Hlayout.addWidget(lb3)
        Hlayout.addLayout(Vlayout)

        self.stack3.setLayout(Hlayout)

    def tab4UI(self):
        Hlayout = QHBoxLayout()
        lb4=QLabel('等待发送')
        btn4 = QPushButton(self)
        btn4.setText("确定")
        Hlayout.addWidget(lb4)
        Hlayout.addWidget(btn4)
        btn4.clicked.connect(partial(self.send, lb4))
        self.stack4.setLayout(Hlayout)
    def display(self,index):
        self.stack.setCurrentIndex(index)

    def paizhao(self):
        self.frameThread.paizhao = 1
        self.stack.setCurrentIndex(1)

    def showDate(self, date):
        self.lb1.setText(date.toString())
    def keil(self,lb):
        i=0
        global send_np
        global keil_state
        self.img = cv2.imread('./LED.png')
        self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)
        ret, thresh = cv2.threshold(self.img, 240, 255, 0)
        self.img = cv2.bitwise_not(thresh, -1)
        # 边缘检测
        contours, hierarchy = cv2.findContours(self.img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # 获取轮廓的矩
        cnt = contours[1]
        M = cv2.moments(cnt)
        # 计算周长
        epsilon = 0.1 * cv2.arcLength(cnt, True)
        # 框4个角
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        pts1 = np.float32([approx[0], approx[3], approx[1], approx[2]])
        pts2 = np.float32([[0, 0], [400, 0], [0, 400], [400, 400]])
        s = cv2.getPerspectiveTransform(pts1, pts2)
        self.img  = cv2.warpPerspective(self.img, s, (400, 400))
        self.img  = cv2.bitwise_not(self.img, -1)
        rows, columns = self.img.shape
        bytesPerLine = columns
        QImg = QImage(self.img.data, columns, rows, columns, QImage.Format_Indexed8)
        lb.setPixmap(QPixmap.fromImage(QImg))
        keil_state =1
    def keil_ok(self):
        self.stack.setCurrentIndex(2)
    def edit_ok(self):
        self.stack.setCurrentIndex(3)
    def edit_read(self,lb,btn):
        global keil_state
        global edit_state
        if keil_state ==0:
            print('还未处理文件')
            lb.setText('还未处理文件')
            return
        if btn.isChecked()==True:
            print('选中')
            edit_state=1
            cv2.namedWindow('frame', 0);
            cv2.moveWindow("trans:" + 'frame', 2000, 2000)
            cv2.resizeWindow('frame', 400, 400);
            cv2.imshow('frame',self.img)
            # 读取键盘:按下q键结束程序
            if btn.isChecked()==False:
                cv2.destroyAllWindows()
        else:
            print('未选中')
            edit_state=0
        rows, columns = self.img.shape
        bytesPerLine = columns
        QImg = QImage(self.img.data, columns, rows, columns, QImage.Format_Indexed8)
        lb.setPixmap(QPixmap.fromImage(QImg))
    def send(self, lb):
        lb.setText('发送完成')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = StackedExample()
    demo.setFixedSize(480,320)
    demo.show()
    sys.exit(app.exec_())
