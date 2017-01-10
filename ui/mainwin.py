# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\TempScripts\LOCAL\psdhandling\ui\mainwin.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(180, 315)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Input_DropFile = QtWidgets.QLabel(self.centralwidget)
        self.Input_DropFile.setAcceptDrops(True)
        self.Input_DropFile.setText("")
        self.Input_DropFile.setPixmap(QtGui.QPixmap(":/root/res/dropfield.png"))
        self.Input_DropFile.setAlignment(QtCore.Qt.AlignCenter)
        self.Input_DropFile.setObjectName("Input_DropFile")
        self.verticalLayout.addWidget(self.Input_DropFile)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tool"))
        self.pushButton.setText(_translate("MainWindow", "Unpack"))

import mainwin_rc
