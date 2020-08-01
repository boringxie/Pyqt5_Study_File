import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from PyQt5.QtGui import QIcon

class QIconSet(QMainWindow):
    def __init__(self):
        super(QIconSet,self).__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,500,500)
        self.setWindowTitle('设置窗口图标')
        # 设置窗口图标
        self.setWindowIcon(QIcon("./images/初音.ico"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #创建一个窗口
    main = QIconSet()
    #显示窗口 
    main.show()
    #进入程序的主循环、并通过exit函数确保主函数安全结束
    sys.exit(app.exec_())