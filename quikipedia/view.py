import wikipedia
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

request = ''
title = ''
page = ''
wikipedia.set_lang("ru")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(458, 528)
        self.qukipedia = QtWidgets.QWidget(MainWindow)
        self.qukipedia.setObjectName("qukipedia")
        self.lineEdit = QtWidgets.QLineEdit(self.qukipedia)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 341, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(32766)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.btnSearch = QtWidgets.QPushButton(self.qukipedia)
        self.btnSearch.setGeometry(QtCore.QRect(350, 10, 101, 31))
        self.btnSearch.setDefault(True)
        self.btnSearch.setFlat(False)
        self.btnSearch.setObjectName("btnSearch")
        self.btnSearch.clicked.connect(self.SearchFor)
        
        self.textField = QtWidgets.QPlainTextEdit(self.qukipedia)
        self.textField.setGeometry(QtCore.QRect(10, 50, 441, 461))
        self.textField.setReadOnly(True)
        self.textField.setObjectName("textField")
        MainWindow.setCentralWidget(self.qukipedia)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def SearchFor(self):
        global request, title, page
        self.textField.clear()
        request = self.lineEdit.text()
        ls = wikipedia.search(request, results=3)
        title = ls[0]
        page = wikipedia.page(title)
        page = page.content
        self.textField.insertPlainText(page)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quikipedia"))
        self.btnSearch.setText(_translate("MainWindow", "Search"))

