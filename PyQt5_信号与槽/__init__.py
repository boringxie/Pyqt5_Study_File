import  sys

import PyQt5_信号与槽

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':

    app = QApplication(sys.argv)

    mianWindow = QMainWindow()
    #初始化类
    ui = PyQt5_信号与槽.Ui_MainWindow()
    #向主窗口添加控件
    ui.setupUi(mianWindow)
    #主窗口显示
    mianWindow.show()
    #进入程序的主循环、并通过exit函数确保主函数安全结束
    sys.exit(app.exec_())