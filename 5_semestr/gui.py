# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(429, 225)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(455, 225))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.InitButton = QtWidgets.QPushButton(self.centralwidget)
        self.InitButton.setGeometry(QtCore.QRect(20, 130, 391, 41))
        self.InitButton.setObjectName("InitButton")
        self.NameInput = QtWidgets.QTextEdit(self.centralwidget)
        self.NameInput.setGeometry(QtCore.QRect(130, 20, 281, 31))
        self.NameInput.setMaximumSize(QtCore.QSize(291, 31))
        self.NameInput.setBaseSize(QtCore.QSize(291, 31))
        self.NameInput.setTabStopDistance(25.0)
        self.NameInput.setObjectName("NameInput")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 101, 21))
        self.label_2.setObjectName("label_2")
        self.FemaleMod = QtWidgets.QCheckBox(self.centralwidget)
        self.FemaleMod.setGeometry(QtCore.QRect(130, 70, 81, 20))
        self.FemaleMod.setObjectName("FemaleMod")
        self.MaleMod = QtWidgets.QCheckBox(self.centralwidget)
        self.MaleMod.setGeometry(QtCore.QRect(250, 70, 171, 20))
        self.MaleMod.setObjectName("MaleMod")
        self.EnLang = QtWidgets.QCheckBox(self.centralwidget)
        self.EnLang.setGeometry(QtCore.QRect(250, 100, 171, 20))
        self.EnLang.setObjectName("EnLang")
        self.RuLang = QtWidgets.QCheckBox(self.centralwidget)
        self.RuLang.setGeometry(QtCore.QRect(130, 100, 81, 20))
        self.RuLang.setObjectName("RuLang")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 101, 21))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 429, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Голосовой ассистент"))
        self.InitButton.setText(_translate("MainWindow", "Запустить"))
        self.label.setText(_translate("MainWindow", "Имя ассистента"))
        self.label_2.setText(_translate("MainWindow", "Пол ассистента"))
        self.FemaleMod.setText(_translate("MainWindow", "Женский"))
        self.MaleMod.setText(_translate("MainWindow", "Мужской(английский)"))
        self.EnLang.setText(_translate("MainWindow", "Английский"))
        self.RuLang.setText(_translate("MainWindow", "Русский"))
        self.label_3.setText(_translate("MainWindow", "Язык ассистента"))
        self.menu.setTitle(_translate("MainWindow", "Список команд"))
        self.action.setText(_translate("MainWindow", "Показать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())