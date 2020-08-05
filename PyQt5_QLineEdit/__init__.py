'''
QLineEdit控件与回显

基本功能：输入单行的文本

EchoMode(回显模式)
总共有4种
1.Normal
2.NoEcho
3.Password
4.PasswordEchoOnEdit
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QFont,QPalette,QPixmap
from PyQt5.QtCore import Qt

class QLineEditEchomode(QWidget):
    def __init__(self):
        super(QLineEditEchomode,self).__init__()
        self.initUI()

    def initUI(self):
        #设置窗口标题
        self.setWindowTitle('文本输入框的回显模式')
        #
        formLayout = QFormLayout()

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnLineEdit = QLineEdit()

        formLayout.addRow('Normal',normalLineEdit)
        formLayout.addRow('NoEcho', noEchoLineEdit)
        formLayout.addRow('Password', passwordLineEdit)
        formLayout.addRow('passwordEcho', passwordEchoOnLineEdit)
        #设置文本
        normalLineEdit.setPlaceholderText('normal')
        noEchoLineEdit.setPlaceholderText('NoEcho')
        passwordLineEdit.setPlaceholderText('Password')
        passwordEchoOnLineEdit.setPlaceholderText('PasswordEcho')
        #设置模式
        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)
        #设置应用图标
        self.setWindowIcon(QIcon('./images/初音.ico'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #创建一个窗口
    main = QLineEditEchomode()
    #显示窗口 
    main.show()
    #进入程序的主循环、并通过exit函数确保主函数安全结束
    sys.exit(app.exec_())