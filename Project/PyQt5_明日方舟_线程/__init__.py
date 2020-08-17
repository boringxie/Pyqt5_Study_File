
'''
QLineEdit(校验器)
如限制器只能输入整数、浮点数或者满足一定条件的字符串
'''

import sys,os,time,明日方舟
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt


if __name__ == '__main__':

    app = QApplication(sys.argv)

    mianWindow = QMainWindow()
    #初始化类
    ui = 明日方舟.Ui_MainWindow()
    #向主窗口添加控件
    ui.setupUi(mianWindow)
    palette = QPalette()
    palette.setBrush(QPalette.Background, QBrush(QPixmap("./images/斯卡蒂_PS.png")))
    mianWindow.setPalette(palette)
    #主窗口显示
    mianWindow.show()
    #进入程序的主循环、并通过exit函数确保主函数安全结束
    sys.exit(app.exec_())