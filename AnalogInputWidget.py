# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnalogInputWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(942, 638)
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(11, 11, 921, 541))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(11, 599, 381, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(11, 564, 381, 28))
        self.pushButton.setObjectName("pushButton")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(510, 600, 261, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(560, 570, 151, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "Stop Measurement"))
        self.pushButton.setText(_translate("Form", "Begin Measurement"))
        self.label.setText(_translate("Form", "Data Reading Rates"))

