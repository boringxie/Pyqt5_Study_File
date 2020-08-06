'''
QLineEdit(校验器)
如限制器只能输入整数、浮点数或者满足一定条件的字符串
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt,QRegExp

class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('校验器')

        #创建表单
        formLayout = QFormLayout()
        #创建文本输入框
        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()
        #添加标题文本输入框
        formLayout.addRow('整数类型',intLineEdit)
        formLayout.addRow('浮点类型',doubleLineEdit)
        formLayout.addRow('数字和字母',validatorLineEdit)
        #设置注释文字
        intLineEdit.setPlaceholderText('整形')
        doubleLineEdit.setPlaceholderText('浮点型')
        validatorLineEdit.setPlaceholderText('数字和字母')
        #整数校验器
        intvalidator = QIntValidator(self)
        intvalidator.setRange(1,24)
        #浮点校验器[-360，360]，精度小数点后两位
        doublelidator = QDoubleValidator(self)
        doublelidator.setRange(-360,360)
        doublelidator.setNotation(QDoubleValidator.StandardNotation)
        #设置精度，小数点后两位
        doublelidator.setDecimals(2)

        #字符和数字（校验器）
        reg = QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

        #设置校验器
        intLineEdit.setValidator(intvalidator)
        doubleLineEdit.setValidator(doublelidator)
        validatorLineEdit.setValidator(validator)

        self.setLayout(formLayout)
        #设置应用图标
        self.setWindowIcon(QIcon('./images/初音.ico'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #创建一个窗口
    main = QLineEditValidator()
    #显示窗口 
    main.show()
    #进入程序的主循环、并通过exit函数确保主函数安全结束
    sys.exit(app.exec_())