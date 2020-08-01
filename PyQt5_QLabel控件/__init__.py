import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QHBoxLayout,QVBoxLayout,QToolTip,QPushButton,QLabel
from PyQt5.QtGui import QIcon,QFont,QPalette,QPixmap
from PyQt5.QtCore import Qt

class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        #设置标签1的文本和字体颜色
        label1.setText("<font color=yellow>这是一个文本标签展示程序.</font>")
        #自动填充背景
        label1.setAutoFillBackground(True)
        #设置窗口填充蓝色
        palette = QPalette()
        palette.setColor(QPalette.Window,Qt.blue)
        #对label使用调色板
        label1.setPalette(palette)
        #文本居中对齐
        label1.setAlignment(Qt.AlignCenter)
        #通过点击标签跳转到网页或链接

        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")

        #label3居中对齐
        label3.setAlignment(Qt.AlignCenter)
        #设置提示文本
        label3.setToolTip('这是一个图片标签')
        #设置标签3为图片
        label3.setPixmap(QPixmap("./images/!face.png"))
        #打开标签跳转链接
        label4.setOpenExternalLinks(True)
        #设置网页跳转链接
        label4.setText("<a href='https://www.baidu.com'>欢迎百度一下</a>")
        #label4靠右对齐
        label4.setAlignment(Qt.AlignRight)
        #设置Label4提示信息
        label4.setToolTip('这是一个超级链接')

        # Label2绑定事件(划过触发)
        label2.linkHovered.connect(self.linkHovered)

        #Label4绑定事件(点击触发)
        label4.linkActivated.connect(self.linkClicked)

        #设置水平布局
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        #设置布局
        self.setLayout(vbox)
        #设置窗口标题
        self.setWindowTitle('Qlabel控件演示')
        #设置窗口大小
        self.setGeometry(300, 300, 500, 300)
        #设置应用图标
        self.setWindowIcon(QIcon('./images/初音.ico'))

    def linkHovered(self):
        print('当鼠标划过label2,触发事件')

    def linkClicked(self):
        print('当鼠标单击时,触发事件')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #创建一个窗口
    main = QLabelDemo()
    #显示窗口 
    main.show()
    #进入程序的主循环、并通过exit函数确保主函数安全结束
    sys.exit(app.exec_())