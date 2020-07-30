import sys

from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #创建一个窗口
    w = QWidget()
    #设置窗口的尺寸
    w.resize(300,150)
    #移动窗口s
    w.move(300,300)
    #设置窗口的标题
    w.setWindowTitle('第一个基于PyQT5的桌面程序')
    #显示窗口
    w.show()
    #进入程序的主循环、并通过exit函数确保主函数安全结束
    sys.exit(app.exec_())