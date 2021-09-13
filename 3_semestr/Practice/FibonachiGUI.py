# -*- coding: utf-8 -*-

from agrigator_func import input_form
import os
from sys import argv, executable

import math,matplotlib.pyplot as plt,numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

if os.path.isfile('agrigator_func.py'):
    from agrigator_func import matfunc
else:
    with open("agrigator_func.py","w") as fl:
        print(f'''import math

def matfunc(x):
    print("(x-2)*math.cos(x)")
    return((x-2)*math.cos(x))
def input_form():
    return("")
''',file=fl)
    from agrigator_func import matfunc

# корректировка файла для собственного модуля
def intoequa(text = str()):
    
    if text.find("arccos") != -1:
        text = text.replace("cos","math.acos")
    if text.find("arcsin") != -1:
        text = text.replace("sin","math.asin")
    if text.find("cos") != -1:
        text = text.replace("cos","math.cos")
    if text.find("sin") != -1:
        text = text.replace("sin","math.sin")
    if text.find("tg") != -1:
        text = text.replace("tg","math.tan")
    if text.find("arctg") != -1:
        text = text.replace("arctg","math.atan")
    if text.find("ctg") != -1:
        text = text.replace("ctg","(-1)/math.sin")
    if text.find("exp") != -1:
        text = text.replace("exp","math.exp")
    if text.find("^") != -1:
        text = text.replace("^","**")
    if text.find("sqrt") != -1:
        text = text.replace("sqrt","math.sqrt") 
    
    return(text)
# для расчета функций
def f(x):
    return -matfunc(x)
def func(x):
    return matfunc(x)

#График функции
def create_graph(a,b):
    ox = np.linspace(a,b,100)
    oy = []
    for value in ox:
        oy.append(func(value))
    fig = plt.figure()
    plt.plot(ox,oy)
    plt.grid(True)
    ax = fig.add_subplot(111)
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_smart_bounds(True) # 3.8 
    ax.spines['bottom'].set_smart_bounds(True) # 3.8
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    fig.savefig('figure.png',dpi = 100)


# создание отдельного файла для вычислений
def create_mod(text):
    with open("agrigator_func.py","w") as fl:
        print(f'''import math

def matfunc(x):
    print("{text}")
    return({text})

def input_form():
    text1 = "{text}"
    text1 = text1.replace("math.","")
    return(text1)
''',file=fl)
    print("Модуль записан")


# Интерфейс

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1051, 755)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 520, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(750, 20, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 100, 640, 480))
        self.label_2.setMinimumSize(QtCore.QSize(640, 480))
        self.label_2.setMaximumSize(QtCore.QSize(640, 480))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("figure.png"))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 600, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 560, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 630, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 430, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 130, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 180, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 90, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 220, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 320, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(90, 130, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(90, 180, 100, 40))
        self.plainTextEdit_2.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(20, 260, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit_3.setFont(font)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(20, 360, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit_4.setFont(font)
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(110, 20, 631, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit_5.setFont(font)
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(40, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1051, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        from agrigator_func import input_form
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Метод Фибоначчи для функции одной переменной"))
        self.label.setText(_translate("MainWindow", "Xmin = "))
        self.label_3.setText(_translate("MainWindow", "Xmax = "))
        self.label_4.setText(_translate("MainWindow", "F(Xmin) = "))
        self.label_5.setText(_translate("MainWindow", "F(Xmax) = "))
        self.pushButton.setText(_translate("MainWindow", "ВЫЧИСЛИТЬ"))
        self.pushButton.clicked.connect(self.main_func)
        self.pushButton_2.clicked.connect(self.create_module)
        self.label_6.setText(_translate("MainWindow", "a = "))
        self.label_7.setText(_translate("MainWindow", "b = "))
        self.label_8.setText(_translate("MainWindow", "Интервал [а,b]"))
        self.label_9.setText(_translate("MainWindow", "Количество итераций(n)"))
        self.label_10.setText(_translate("MainWindow", "Приближение (Epsilone)"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", ""))
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", ""))
        self.plainTextEdit_3.setPlainText(_translate("MainWindow", ""))
        self.plainTextEdit_4.setPlainText(_translate("MainWindow", "0.0001"))
        self.plainTextEdit_5.setPlainText(_translate("MainWindow", f"{input_form()}"))
        self.label_11.setText(_translate("MainWindow", "f(x) = "))
        self.pushButton_2.setText(_translate("MainWindow", "ДОБАВИТЬ"))
    
    def create_module(self):
        from sys import argv, executable
        import os
        equa = self.plainTextEdit_5.toPlainText()
        equa = intoequa(equa)
        equa = create_mod(equa)
        os.execl(executable, os.path.abspath(__file__), *argv)

    def main_func(self):
        
        equa = self.plainTextEdit_5.toPlainText()
        from  agrigator_func import matfunc

        # Интервал
        a = int(self.plainTextEdit.toPlainText())
        a1 = a
        b = int(self.plainTextEdit_2.toPlainText())
        b1 = b
        # Количество вычислений
        N = int(self.plainTextEdit_3.toPlainText())
        N1 = N
        Epsilone =  float(self.plainTextEdit_4.toPlainText())
        
        # Создание графика

        create_graph(a,b)
        self.label_2.setPixmap(QtGui.QPixmap("figure.png"))


        # Входные данные
        Fib = [1,1]

        for i in range(2,N+1):
            Fib.append(Fib[i-1]+Fib[i-2])

        if N % 2 == 0:
            sign = 1
        else:
            sign = -1

        x1 = a + ((Fib[N-2] * (b-a) - sign*Epsilone)/Fib[N])
        x2 = a + ((Fib[N-1]*(b-a) + sign*Epsilone)/Fib[N])

        f1 = f(x1)
        f2 = f(x2)

        j = 1

        # Нахождение максимума
        while (j <= (N-1)):

            if ((N - j + 1)% 2 == 0):
                sign = 1
            else:
                sign = -1
            
            if (f1 <= f2):
                b = x2 
                x2 = x1
                f2 = f1
                x1 = a + ((Fib[N - j - 1]*(b-a)-sign * Epsilone)/Fib[N-j+1])
                f1 = f(x1)
                x = x2
            else:
                a = x1 
                x1 = x2
                f1 = f2
                x2 = a + ((Fib[N - j] * (b-a) + sign * Epsilone)/Fib[N-j+1])
                f2 = f(x2)
                x = x1
            j += 1



        # Перезапись(дублирование) входных данных

        Fib1 = [1,1]
        for i in range(2,N+1):
            Fib1.append(Fib1[i-1]+Fib1[i-2])

        if N1 % 2 == 0:
            sign1 = 1
        else:
            sign1 = -1

        x3 = a1 + ((Fib1[N1-2]* (b1-a1) - sign1*Epsilone) / Fib1[N1])
        x4 = a1 + ((Fib1[N1-1]* (b1-a1) + sign1*Epsilone) / Fib1[N1])

        f3 = func(x3)
        f4 = func(x4)
        j1 = 1

        # Нахождение максимума
        while (j1 <= (N1-1)):
            if ((N1 - j1 + 1)% 2 == 0):
                sign1 = 1
            else:
                sign1 = -1
            
            if (f3 <= f4):
                b1 = x4
                x4 = x3
                f4 = f3
                x3 = a1 + ((Fib1[N1 - j1 - 1] * (b1-a1) - sign1 * Epsilone)/Fib1[N1-j1+1])
                f3 = func(x3)
                max = x4
            else:
                a1 = x3 
                x3 = x4
                f3 = f4
                x4 = a1 + ((Fib1[N1 - j1] * (b1-a1) + sign1 * Epsilone)/Fib1[N1-j1+1])
                f4 = func(x4)
                max = x3
            j1 += 1
            
            
            rou_num = len(str(Epsilone))-2

            _translate = QtCore.QCoreApplication.translate
            self.label.setText(_translate("MainWindow", f"Xmin = {round(max,rou_num)}"))
            self.label_3.setText(_translate("MainWindow", f"Xmax = {round(x,rou_num)}"))
            self.label_4.setText(_translate("MainWindow", f"F(Xmin) = {round(func(max),rou_num)}"))
            self.label_5.setText(_translate("MainWindow", f"F(Xmax) = {round(-f(x),rou_num)}"))



if __name__ == "__main__":
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())