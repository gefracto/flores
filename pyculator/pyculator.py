# Pyculator v.1.0
# Created by Flores
# 11-01-2016


import sys
from PyQt5.QtWidgets import *

total = 0.0
number = 0.0
number2 = 0.0
operator = ''
op = False
forPoint = 10
dot = False


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tablo = QLCDNumber(self)
        self.tablo.setGeometry(0, 0, 161, 21)
        self.tablo.setSmallDecimalPoint(True)
        self.tablo.setDigitCount(13)
        self.tablo.setDecMode()
        self.tablo.setProperty("value", 0.0)
        self.tablo.setProperty("intValue", 0)
        self.tablo.setStyleSheet('color:blue;\nbackground-color:white;')
        self.tablo.setSegmentStyle(QLCDNumber.Flat)

        self.b0 = QPushButton('0', self)
        self.b0.setGeometry(0, 180, 81, 41)

        self.b1 = QPushButton('1', self)
        self.b1.setGeometry(0, 140, 41, 41)

        self.b2 = QPushButton('2', self)
        self.b2.setGeometry(40, 140, 41, 41)

        self.b3 = QPushButton('3', self)
        self.b3.setGeometry(80, 140, 41, 41)

        self.b4 = QPushButton('4', self)
        self.b4.setGeometry(0, 100, 41, 41)

        self.b5 = QPushButton('5', self)
        self.b5.setGeometry(40, 100, 41, 41)

        self.b6 = QPushButton('6', self)
        self.b6.setGeometry(80, 100, 41, 41)

        self.b7 = QPushButton('7', self)
        self.b7.setGeometry(0, 60, 41, 41)

        self.b8 = QPushButton('8', self)
        self.b8.setGeometry(40, 60, 41, 41)

        self.b9 = QPushButton('9', self)
        self.b9.setGeometry(80, 60, 41, 41)

        self.bPoint = QPushButton('.', self)
        self.bPoint.setGeometry(80, 180, 41, 41)
        self.bPoint.clicked.connect(self.Point)

        self.bEquals = QPushButton('=', self)
        self.bEquals.setGeometry(120, 140, 41, 81)
        self.bEquals.clicked.connect(self.Equals)

        self.bPlus = QPushButton('+', self)
        self.bPlus.setGeometry(120, 100, 41, 41)

        self.bMinus = QPushButton('-', self)
        self.bMinus.setGeometry(120, 60, 41, 41)

        self.bMul = QPushButton('*', self)
        self.bMul.setGeometry(120, 20, 41, 41)

        self.bDiv = QPushButton('/', self)
        self.bDiv.setGeometry(80, 20, 41, 41)

        self.bClear = QPushButton('C', self)
        self.bClear.setGeometry(0, 20, 41, 41)
        self.bClear.clicked.connect(self.Clear)

        self.bSign = QPushButton('+/-', self)
        self.bSign.setGeometry(40, 20, 41, 41)
        self.bSign.clicked.connect(self.Sign)

        self.setWindowTitle('Pyculator')
        self.setGeometry(0, 0, 161, 220)
        self.setFixedSize(161, 220)
        self.move(161, 220)
        self.show()



        self.nums = [self.b0, self.b1, self.b2, self.b3, self.b4,
                self.b5, self.b6, self.b7, self.b8, self.b9]

        self.oper = [self.bDiv, self.bMinus, self.bMul,
                self.bPlus, self.bSign]

        self.other = [self.bPoint, self.bEquals, self.bClear]



        for i in self.nums:
            i.setStyleSheet("color:blue;")
            i.clicked.connect(self.numClicked)

        for i in self.oper:
            i.setStyleSheet("color:red;")
            i.setStyleSheet('background-color: rgb(212, 212, 212);')
            i.clicked.connect(self.Oper)

        for i in self.other[1:]:
            i.setStyleSheet('background-color: rgb(212, 212, 212);')


    def Point(self):
        global dot, forPoint
        forPoint = 10
        dot = True


    def Sign(self):
        global op, number, number2

        if op is False:
            number = number * (-1)
        else:
            number2 = number2 * (-1)
        self.render()

    def Clear(self):
        global number2, number, total, operator, op, dot, forPoint

        forPoint = 10
        total = 0.0
        dot = False
        number = 0.0
        number2 = 0.0
        operator = ''
        op = False
        self.render()


    def Equals(self):
        global number, number2, total, op, operator, forPoint, dot

        if operator == '+':
            total = float(number) + float(number2)
        elif operator == '-':
            total = float(number) - float(number2)
        elif operator == '*':
            total = float(number) * float(number2)
        elif operator == '/':
            total = float(number) / float(number2)

        op = False
        number2 = 0.0
        number = total
        forPoint = 10
        dot = False
        self.render()




    def numClicked(self):
        global number, number2, forPoint, dot
        digit = self.sender()
        if op is False:
            if dot is False:
                number = number * 10 + int(digit.text())
                self.render()
            else:
                number = number + int(digit.text())/forPoint
                forPoint *= 10
                self.render()
        else:
            if dot is False:
                number2 = number2 * 10 + int(digit.text())
                self.render()
            else:
                number2 = number2 + int(digit.text())/forPoint
                forPoint *= 10
                self.render()


    def render(self):
        if op is False:
            self.tablo.display(number)
        elif op is True:
            self.tablo.display(number2)

    def Oper(self):
        global dot, operator, op
        sender = self.sender()
        operator = sender.text()
        op = True
        dot = False
        forPoint = 10

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())