'''
按钮控件
4种按钮
QPushButton
AToolButton
QRadioButton
QCheckBox
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo,self).__init__()
        self.initUI()

    def initUI(self):
        #设置窗口标题
        self.setWindowTitle('QPushButtonDemo Demo')
        layout = QVBoxLayout()

        #给按钮添加两个槽
        self.button1 = QPushButton('第1个按钮')
        self.button1.setText('First Button1')
        self.button1.setCheckable(True)
        self.button1.toggle()
        self.button1.clicked.connect(self.buttonState)
        self.button1.clicked.connect(lambda:self.button_click(self.button1))
        
        #图像按钮
        self.button2 = QPushButton('图像按钮')

        #设置图标
        self.button2.setIcon(QIcon(QPixmap('./images/!face.png')))
        self.button2.clicked.connect(lambda: self.button_click(self.button2))

        #不可用按钮
        self.button3 = QPushButton('不可用按钮')
        self.button3.setEnabled(False)

        #热键按钮 alt+M 默认按钮
        self.button4  = QPushButton('&MyButton')
        self.button4.setDefault(True)
        self.button4.setToolTip('这是一个默认案件 热键alt+M')
        self.button4.clicked.connect(lambda: self.button_click(self.button4))

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)

        self.setLayout(layout)

        #设置应用图标
        self.setWindowIcon(QIcon('./images/初音.ico'))

    def button_click(self,btn):
        print('被单击的按钮是<'+btn.text()+'>')

    def buttonState(self):
        if self.button1.isChecked():
            print('按钮1已经被选中')
            self.button1.setText('按钮1已经被选中')
        else:
            print('按钮1未被选中')
            self.button1.setText('按钮1未被选中')

if __name__ == '__main__':

    app = QApplication(sys.argv)

    #创建一个窗口
    main = QPushButtonDemo()

    #显示窗口 
    main.show()

    #进入程序的主循环、并通过exit函数确保主函数安全结束
    sys.exit(app.exec_())