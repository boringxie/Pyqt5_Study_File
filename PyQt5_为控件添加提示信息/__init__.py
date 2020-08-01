import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QHBoxLayout,QToolTip,QPushButton
from PyQt5.QtGui import QIcon,QFont

class TooltipForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        QToolTip.setFont(QFont('Sanserif',12))
        self.setToolTip('控件提示信息完成')
        self.setGeometry(300,300,500,300)
        self.setWindowTitle('设置控件提示信息')
        self.setWindowIcon(QIcon('./images/!face.png'))

        #添加button
        self.button1 = QPushButton('我的按钮')
        self.button1.setToolTip('这是一个按钮，Are you ok?')
        #设置布局
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        #添加窗口
        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #创建一个窗口
    main = TooltipForm()
    #显示窗口 
    main.show()
    #进入程序的主循环、并通过exit函数确保主函数安全结束
    sys.exit(app.exec_())