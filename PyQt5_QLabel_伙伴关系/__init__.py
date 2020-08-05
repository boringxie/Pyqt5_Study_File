import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QFont,QPalette,QPixmap
from PyQt5.QtCore import Qt

class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #设置窗口标题
        self.setWindowTitle('QLabel与伙伴控件')
        #创建nameLabel
        nameLabel = QLabel('&Name')
        nameLineEdit = QLineEdit(self)
        #设置nameLabel与nameLineEdit成为伙伴控件
        nameLabel.setBuddy(nameLineEdit)

        # 创建passLabel
        passwordLabel = QLabel('&Password')
        passwordLineEdit = QLineEdit(self)
        # 设置nameLabel与nameLineEdit成为伙伴控件
        passwordLabel.setBuddy(passwordLineEdit)
        
        #创建按钮 ok & cancel
        btnOK = QPushButton('&OK')
        btncanel  = QPushButton('&Canel')

        #使用栅格布局
        mianLayout = QGridLayout(self)
        #nameLabel占用第一行1列
        mianLayout.addWidget(nameLabel,0,0)
        # nameLineEdit占用第一行2列
        mianLayout.addWidget(nameLineEdit, 0, 1,1,2)
        # passwordLabel占用第2行1列
        mianLayout.addWidget(passwordLabel, 1, 0)
        # passwordLabel占用第2行2列
        mianLayout.addWidget(passwordLineEdit, 1, 1,1,2)
        mianLayout.addWidget(btnOK,2,1)
        mianLayout.addWidget(btncanel,2,2)
        #设置应用图标
        self.setWindowIcon(QIcon('./images/初音.ico'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #创建一个窗口
    main = QLabelBuddy()
    #显示窗口 
    main.show()
    #进入程序的主循环、并通过exit函数确保主函数安全结束
    sys.exit(app.exec_())