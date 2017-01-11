# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '\\apseodesk214\psdhandling\ui\mainwin.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(148, 238)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(148, 0))
        MainWindow.setMaximumSize(QtCore.QSize(148, 16777215))
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        MainWindow.setAnimated(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Input_DropFile = QtWidgets.QLabel(self.centralwidget)
        self.Input_DropFile.setAcceptDrops(True)
        self.Input_DropFile.setText("")
        self.Input_DropFile.setPixmap(QtGui.QPixmap(":/root/res/dropfield.png"))
        self.Input_DropFile.setAlignment(QtCore.Qt.AlignCenter)
        self.Input_DropFile.setObjectName("Input_DropFile")
        self.verticalLayout.addWidget(self.Input_DropFile)
        self.Preview_Layers = QtWidgets.QTreeWidget(self.centralwidget)
        self.Preview_Layers.setIndentation(5)
        self.Preview_Layers.setObjectName("Preview_Layers")
        item_0 = QtWidgets.QTreeWidgetItem(self.Preview_Layers)
        self.verticalLayout.addWidget(self.Preview_Layers)
        self.UnpackButton = QtWidgets.QPushButton(self.centralwidget)
        self.UnpackButton.setObjectName("UnpackButton")
        self.verticalLayout.addWidget(self.UnpackButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PSDUnpack"))
        self.Preview_Layers.headerItem().setText(0, _translate("MainWindow", "Layers"))
        __sortingEnabled = self.Preview_Layers.isSortingEnabled()
        self.Preview_Layers.setSortingEnabled(False)
        self.Preview_Layers.topLevelItem(0).setText(0, _translate("MainWindow", "aaaa"))
        self.Preview_Layers.setSortingEnabled(__sortingEnabled)
        self.UnpackButton.setText(_translate("MainWindow", "Unpack"))

import mainwin_rc
