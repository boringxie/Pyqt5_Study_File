# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQt5_工具栏和菜单栏.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1458, 1090)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 120, 131, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 260, 131, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 390, 191, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(240, 460, 155, 25))
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(230, 500, 311, 171))
        self.textEdit.setObjectName("textEdit")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(240, 340, 122, 25))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1458, 34))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNEW = QtWidgets.QAction(MainWindow)
        self.actionNEW.setCheckable(True)
        self.actionNEW.setObjectName("actionNEW")
        self.actionOPEN = QtWidgets.QAction(MainWindow)
        self.actionOPEN.setObjectName("actionOPEN")
        self.actionVIEW = QtWidgets.QAction(MainWindow)
        self.actionVIEW.setObjectName("actionVIEW")
        self.menufile.addAction(self.actionNEW)
        self.menufile.addAction(self.actionOPEN)
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionVIEW)
        self.menubar.addAction(self.menufile.menuAction())
        self.toolBar.addAction(self.actionNEW)
        self.toolBar.addAction(self.actionOPEN)
        self.toolBar.addAction(self.actionVIEW)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        self.radioButton_2.toggled['bool'].connect(self.textEdit.setEnabled)
        self.checkBox.toggled['bool'].connect(self.lineEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "关闭窗口"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.radioButton_2.setText(_translate("MainWindow", "可用/不可用"))
        self.checkBox.setText(_translate("MainWindow", "显示/隐藏"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNEW.setText(_translate("MainWindow", "NEW"))
        self.actionNEW.setToolTip(_translate("MainWindow", "创建文本"))
        self.actionNEW.setShortcut(_translate("MainWindow", "Shift+A"))
        self.actionOPEN.setText(_translate("MainWindow", "OPEN"))
        self.actionOPEN.setToolTip(_translate("MainWindow", "打开"))
        self.actionVIEW.setText(_translate("MainWindow", "VIEW"))
        self.actionVIEW.setToolTip(_translate("MainWindow", "视图"))
