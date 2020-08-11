
'''
QTextEdit控件
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QRegExp


class QTextEditDemo(QWidget):
    def __init__(self):
        super(QTextEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5_QLineEdit_综合案例')
        self.resize(300,280)
        self.textEdit = QTextEdit()
        self.buttonText = QPushButton('显示文本')
        self.buttonToText = QPushButton('获取文本')
        self.buttonHTML = QPushButton('显示HTML')
        self.buttonToHTML = QPushButton('获取HTML')
        # 设置应用图标
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonHTML)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonToText)
        layout.addWidget(self.buttonToHTML)

        self.setLayout(layout)

        self.buttonText.clicked.connect(self.onClick_buttonText)
        self.buttonHTML.clicked.connect(self.onCLick_ButtonHTML)
        self.buttonToText.clicked.connect(self.onClick_buttonToText)
        self.buttonToHTML.clicked.connect(self.onCLick_ButtonToHTML)
    def onClick_buttonText(self):
        self.textEdit.setPlainText('Hello World, 世界你好吗 ')
    def onClick_buttonToText(self):
        print(self.textEdit.toPlainText())
    def onCLick_ButtonHTML(self):
        self.textEdit.setHtml('<font color="blue" size="5">Hello World</font>')
    def onCLick_ButtonToHTML(self):
        print(self.textEdit.toHtml())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建一个窗口
    main = QTextEditDemo()
    # 显示窗口
    main.show()
    # 进入程序的主循环、并通过exit函数确保主函数安全结束
    sys.exit(app.exec_())