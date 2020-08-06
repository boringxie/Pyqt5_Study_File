
'''
QLineEdit(校验器)
如限制器只能输入整数、浮点数或者满足一定条件的字符串
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QRegExp


class QLineEditDemo(QWidget):
    def __init__(self):
        super(QLineEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        edit1 = QLineEdit()
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)  # 不超过9999
        edit1.setAlignment(Qt.AlignRight)
        edit1.setFont(QFont('Arial', 20))

        edit2 = QLineEdit()
        edit2.setValidator(QDoubleValidator(0.99, 99.99, 2))

        edit3 = QLineEdit()
        edit3.setInputMask('99_9999_999999;#')

        edit4 = QLineEdit()
        edit4.textChanged.connect(self.textChanged)

        edit5 = QLineEdit()
        edit5.setEchoMode(QLineEdit.Password)
        edit5.textChanged.connect(self.enterPress)

        edit6 = QLineEdit('Hello PyQT5')
        #只读模式
        edit6.setReadOnly(True)

        FormLayout = QFormLayout()
        FormLayout.addRow('整数校验', edit1)
        FormLayout.addRow('浮点数校验', edit2)
        FormLayout.addRow('Input Mask', edit3)
        FormLayout.addRow('文本变化',edit4)
        FormLayout.addRow('密码', edit5)
        FormLayout.addRow('只读', edit6)
        self.setLayout(FormLayout)
        self.setWindowTitle('PyQt5_QLineEdit_综合案例')
        # 设置应用图标
        self.setWindowIcon(QIcon('./images/初音.ico'))
    
    def textChanged(self,text):
        print('输入的内容'+ text)
    def enterPress(self,text):
        print('已输入值:'+text)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建一个窗口
    main = QLineEditDemo()
    # 显示窗口
    main.show()
    # 进入程序的主循环、并通过exit函数确保主函数安全结束
    sys.exit(app.exec_())