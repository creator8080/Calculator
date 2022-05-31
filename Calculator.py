from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from math import sqrt

app = QApplication([])
main = QWidget()
main.setGeometry(400,300,400,300)
main.setWindowTitle('Calculator')
app.setWindowIcon(QIcon('calc.png'))

line = QLabel('Result')
delete_last = QPushButton('<=')
delete_left = QPushButton('=>')
delete_all = QPushButton('C')
sqrtes = QPushButton('√')
num_seven = QPushButton('7')
num_eight = QPushButton('8')
num_nine = QPushButton('9')
divide = QPushButton('÷')
num_four = QPushButton('4')
num_five = QPushButton('5')
num_six = QPushButton('6')
multiplate = QPushButton('×')
num_one = QPushButton('1')
num_two = QPushButton('2')
num_three = QPushButton('3')
minus = QPushButton('−')
num_zero = QPushButton('0')
points = QPushButton('.')
summa = QPushButton('=')
plus = QPushButton('+')

row = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()
row4 = QHBoxLayout()
row5 = QHBoxLayout()
row6 = QHBoxLayout()

def check():
    global line
    if line.text() == 'Result':
        line.setText('')

def clck_one():
    global line
    check()
    line.setText(line.text() + '1')
def clck_two():
    global line
    check()
    line.setText(line.text() + '2')
def clck_three():
    global line
    check()
    line.setText(line.text() + '3')
def clck_four():
    global line
    check()
    line.setText(line.text() + '4')
def clck_five():
    global line
    check()
    line.setText(line.text() + '5')
def clck_six():
    global line
    check()
    line.setText(line.text() + '6')
def clck_seven():
    global line
    check()
    line.setText(line.text() + '7')
def clck_eight():
    global line
    check()
    line.setText(line.text() + '8')
def clck_nine():
    global line
    check()
    line.setText(line.text() + '9')
def clck_zero():
    global line
    check()
    line.setText(line.text() + '0')


def clck_minus():
    global line
    check()
    line.setText(line.text() + '-')
def clck_plus():
    global line
    check()
    line.setText(line.text() + '+')
def clck_multiplate():
    global line
    check()
    line.setText(line.text() + '*')
def clck_divide():
    global line
    check()
    line.setText(line.text() + '/')

def delete():
    global line
    line.setText('Result')

def delete_right():
    global line
    if len(line.text()) == 1 or line.text() == 'Result':
        line.setText('Result')
    else:
        line.setText(line.text()[:-1])

def delete_lef():
    global line
    if len(line.text()) == 1 or line.text() == 'Result':
        line.setText('Result')
    else:
        line.setText(line.text()[1::])

def total():
    global line
    try:
        line.setText(str(eval(line.text())))
    except:
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Проверьте свой пример")
        msg.exec_()

def koren():
    global line
    try:
        line.setText(str(sqrt(float(line.text()))))
    except:
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Проверьте свой пример")
        msg.exec_()

def point():
    global line
    line.setText(line.text() + '.')

row1.addWidget(line)
row2.addWidget(sqrtes)
row2.addWidget(delete_all)
row2.addWidget(delete_left)
row2.addWidget(delete_last)
row3.addWidget(num_seven)
row3.addWidget(num_eight)
row3.addWidget(num_nine)
row3.addWidget(divide)
row4.addWidget(num_four)
row4.addWidget(num_five)
row4.addWidget(num_six)
row4.addWidget(multiplate)
row5.addWidget(num_one)
row5.addWidget(num_two)
row5.addWidget(num_three)
row5.addWidget(minus)
row6.addWidget(points)
row6.addWidget(num_zero)
row6.addWidget(summa)
row6.addWidget(plus)

num_one.clicked.connect(clck_one)
num_two.clicked.connect(clck_two)
num_three.clicked.connect(clck_three)
num_four.clicked.connect(clck_four)
num_five.clicked.connect(clck_five)
num_six.clicked.connect(clck_six)
num_seven.clicked.connect(clck_seven)
num_eight.clicked.connect(clck_eight)
num_nine.clicked.connect(clck_nine)
num_zero.clicked.connect(clck_zero)

multiplate.clicked.connect(clck_multiplate)
divide.clicked.connect(clck_divide)
plus.clicked.connect(clck_plus)
minus.clicked.connect(clck_minus)

summa.clicked.connect(total)
delete_all.clicked.connect(delete)
delete_last.clicked.connect(delete_right)
delete_left.clicked.connect(delete_lef)
sqrtes.clicked.connect(koren)
points.clicked.connect(point)

row.addLayout(row1)
row.addLayout(row2)
row.addLayout(row3)
row.addLayout(row4)
row.addLayout(row5)
row.addLayout(row6)
main.setLayout(row)

main.show()
app.exec()