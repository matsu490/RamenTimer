# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainDialog.ui'
#
# Created: Sat Apr 15 01:37:40 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(228, 169)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 211, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lcdNumber = QtGui.QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout.addWidget(self.lcdNumber)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.StopButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.StopButton.setObjectName("StopButton")
        self.gridLayout.addWidget(self.StopButton, 0, 1, 1, 1)
        self.StartButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.StartButton.setObjectName("StartButton")
        self.gridLayout.addWidget(self.StartButton, 0, 0, 1, 1)
        self.ResetButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.ResetButton.setObjectName("ResetButton")
        self.gridLayout.addWidget(self.ResetButton, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.StopButton.setText(QtGui.QApplication.translate("Dialog", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.StartButton.setText(QtGui.QApplication.translate("Dialog", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.ResetButton.setText(QtGui.QApplication.translate("Dialog", "Reset", None, QtGui.QApplication.UnicodeUTF8))

