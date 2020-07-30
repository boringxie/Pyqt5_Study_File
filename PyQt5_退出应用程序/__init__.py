import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QHBoxLayout,QPushButton

class QuitApp(QMainWindow):
    def __init__(self):
        super(QuitApp,self).__init__()
        self.resize(300,120)
        self.setWindowTitle('退出应用程序')
        
        #添加button
        self.button1 = QPushButton('退出应用程序')
        #将信号与槽关联
        self.button1.clicked.connect(self.onClick_Button)
        #设置布局
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        #添加窗口
        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    def onClick_Button(self):
        sender = self.sender()
        print(sender.text()+'按钮被按下')
        app = QApplication.instance()
        #退出应用程序
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #设置窗口图标
    #app.setWindowIcon()
    #创建一个窗口
    main = QuitApp()
    #显示窗口 
    main.show()
    #进入程序的主循环、并通过exit函数确保主函数安全结束
    sys.exit(app.exec_())