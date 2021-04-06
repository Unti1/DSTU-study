# алгоритм Хаффмана.
from collections import Counter
import pickle
# Узлы для построения древа
# Переменные left и right отображают сторону в которую пойдет ветвление узла (Право или Лево)
class Node: 
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

# Создание древа
def get_tree(text):
    text_count = Counter(text) # подсчет частоты повторений

    if len(text_count) <= 1:
        node = Node(None) # Задаем изначальный узел с пустым(None) значением

    
        if len(text_count) == 1:
            node.left = Node([key for key in text_count][0])
            node.right = Node(None)
            
        text_count = {node: 1}
    

    while len(text_count) != 1:
        node = Node(None)
        spam = text_count.most_common()[:-3:-1] # наиболее часто встречаемые символы в  порядке убывания 
        # Выборка в spam идет с конца по 2  элемента 
        # print(spam)
        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])
        else:
            node.left = spam[0][0]

        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])
        else:
            node.right = spam[1][0]

        del text_count[spam[0][0]]
        del text_count[spam[1][0]]
        text_count[node] = spam[0][1] + spam[1][1]

    return [arg for arg in text_count][0]

# Получения шифровки каждого символа
def get_code(root, codes=dict(), code=''):

    if root is None:
        return

    if isinstance(root.value, str):
        codes[root.value] = code
        return codes

    get_code(root.left, codes, code + '0')
    get_code(root.right, codes, code + '1')

    return codes


# Кодирование
def coding(text, codes):
    res = ''
    # кодирование
    for symbol in text:
        res += codes[symbol]
        
    # добавление вероятности
    text_count = Counter(text)
    pwr = len(text)
    dic_ver = []
    for i in text_count.keys():
        dic_ver.append([i,text_count.get(i)/pwr])
    res += "\n"+str(dic_ver)
    
    return res

# Декодирование
def decoding(text, codes):
    res = ''
    i = 0

    while i < len(text):

        for code in codes:

            if text[i:].find(codes[code]) == 0:
                res += code
                i += len(codes[code])
    return res

# (coding и decoding) function стояли раньше здесь

'''
# Проверка на точность перевода
with open("testout/file1.txt",'r',encoding='utf-8') as f:
    with open ("testout/file2.txt",'r',encoding='utf-8') as f1:
        text1 = f.read()
        text2 = f1.read()
        if text1 == text2:
            print("Успех")
        else:
            pass
            # print("Неудача")
'''

# Меню 
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(674, 584)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Кнопка "Кодировать"
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 80, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.coding_function)

        # Кнопка "Декодировать"
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 80, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.decoding_function)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 430, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 470, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(370, 430, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(370, 470, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 160, 291, 251))
        self.textEdit.setObjectName("textEdit")
        
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(330, 160, 301, 251))
        self.textEdit_2.setObjectName("textEdit_2")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 674, 26))
        self.menubar.setObjectName("menubar")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Алгоритм Хаффмана"))
        self.pushButton.setText(_translate("MainWindow", "Кодировать"))
        self.pushButton_2.setText(_translate("MainWindow", "Декодировать"))
        self.label.setText(_translate("MainWindow", "Файл : file1.txt"))
        self.label_2.setText(_translate("MainWindow", "Файл : file2.txt"))
        self.label_3.setText(_translate("MainWindow", "Конечный вес файла : "))
        self.label_4.setText(_translate("MainWindow", "Новое навзание файла : file2.txt"))
        self.label_5.setText(_translate("MainWindow", "Конечный вес файла : "))
        self.label_6.setText(_translate("MainWindow", "Новое навзание файла : file3.txt"))
        
    def coding_function(self):
        
        filename1 = 'testout/file1.txt'
        filename2 = 'testout/file2.txt'

        with open(filename1,"r",encoding="utf-8") as f:
            file_text = f.read()
        # создаем дерево по данным файла 
        tree = get_tree(file_text)
        # создаем шифр под символ
        codes = get_code(tree)
        # print(f'Шифр: {codes}')
        # сжимаем данные файла1 в файл2 
        coding_text = coding(file_text, codes)
        # print('Сжатая строка: \n', coding_text)
        with open(filename2,"w") as f:
            f.write(coding_text)

        import os
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("MainWindow", f"Конечный вес файла : {os.path.getsize(filename2)} байт"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
        f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{coding_text}</p>\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


    def decoding_function(self):

        filename3 = 'testout/file3.txt'
        with open('testout/file1.txt',"r",encoding="utf-8") as f:
            file_text = f.read() 
        tree = get_tree(file_text)
        codes = get_code(tree)
        with open('testout/file2.txt',"r") as f:
            text = f.read()
            textlist = text.split('\n')
            textlist.remove(textlist[-1])
            text = ''
            for i in textlist:
                text += i
        
        decoding_text = decoding(text, codes)
        # print('Исходная строка: ', decoding_text)
        with open(filename3,"w") as f:
            f.write(decoding_text)

        import os
        _translate = QtCore.QCoreApplication.translate
        self.label_5.setText(_translate("MainWindow", f"Конечный вес файла : {os.path.getsize(filename3)} байт"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
        f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{decoding_text}</p>\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



# ! Создать меню 
# ! Информацию о 0 и 1 в битовую
# ! В конец второго файла дописать вероятности
# В декодировании считывать вероятности и строить шифр заного , по таблице 