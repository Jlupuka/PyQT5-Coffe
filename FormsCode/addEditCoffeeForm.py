# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateInformation(object):
    def setupUi(self, CreateInformation):
        CreateInformation.setObjectName("CreateInformation")
        CreateInformation.resize(870, 336)
        self.gridLayout = QtWidgets.QGridLayout(CreateInformation)
        self.gridLayout.setObjectName("gridLayout")
        self.AddPushButton = QtWidgets.QPushButton(CreateInformation)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AddPushButton.setFont(font)
        self.AddPushButton.setObjectName("AddPushButton")
        self.gridLayout.addWidget(self.AddPushButton, 6, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(CreateInformation)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(CreateInformation)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(CreateInformation)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(CreateInformation)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(CreateInformation)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(CreateInformation)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.DegreeLineEdit = QtWidgets.QLineEdit(CreateInformation)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DegreeLineEdit.setFont(font)
        self.DegreeLineEdit.setObjectName("DegreeLineEdit")
        self.gridLayout.addWidget(self.DegreeLineEdit, 1, 2, 1, 1)
        self.ExitPushButton = QtWidgets.QPushButton(CreateInformation)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ExitPushButton.setFont(font)
        self.ExitPushButton.setObjectName("ExitPushButton")
        self.gridLayout.addWidget(self.ExitPushButton, 6, 1, 1, 1)
        self.GWLineEdit = QtWidgets.QLineEdit(CreateInformation)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.GWLineEdit.setFont(font)
        self.GWLineEdit.setObjectName("GWLineEdit")
        self.gridLayout.addWidget(self.GWLineEdit, 2, 2, 1, 1)
        self.DescrLineEdit = QtWidgets.QLineEdit(CreateInformation)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DescrLineEdit.setFont(font)
        self.DescrLineEdit.setObjectName("DescrLineEdit")
        self.gridLayout.addWidget(self.DescrLineEdit, 3, 2, 1, 1)
        self.PriceSpinBox = QtWidgets.QSpinBox(CreateInformation)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PriceSpinBox.setFont(font)
        self.PriceSpinBox.setMinimum(50)
        self.PriceSpinBox.setMaximum(10000)
        self.PriceSpinBox.setSingleStep(100)
        self.PriceSpinBox.setObjectName("PriceSpinBox")
        self.gridLayout.addWidget(self.PriceSpinBox, 4, 2, 1, 1)
        self.VolumeSpinBox = QtWidgets.QSpinBox(CreateInformation)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.VolumeSpinBox.setFont(font)
        self.VolumeSpinBox.setMinimum(100)
        self.VolumeSpinBox.setMaximum(5000)
        self.VolumeSpinBox.setSingleStep(250)
        self.VolumeSpinBox.setObjectName("VolumeSpinBox")
        self.gridLayout.addWidget(self.VolumeSpinBox, 5, 2, 1, 1)
        self.SortLineEdit = QtWidgets.QLineEdit(CreateInformation)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SortLineEdit.setFont(font)
        self.SortLineEdit.setObjectName("SortLineEdit")
        self.gridLayout.addWidget(self.SortLineEdit, 0, 2, 1, 1)

        self.retranslateUi(CreateInformation)
        QtCore.QMetaObject.connectSlotsByName(CreateInformation)

    def retranslateUi(self, CreateInformation):
        _translate = QtCore.QCoreApplication.translate
        CreateInformation.setWindowTitle(_translate("CreateInformation", "Добавление новой информации"))
        self.AddPushButton.setText(_translate("CreateInformation", "Добавить"))
        self.label_6.setText(_translate("CreateInformation", "Объем упаковки"))
        self.label.setText(_translate("CreateInformation", "Название сорта"))
        self.label_3.setText(_translate("CreateInformation", "Молотый/в зерна"))
        self.label_2.setText(_translate("CreateInformation", "Степень обжарки"))
        self.label_5.setText(_translate("CreateInformation", "Цена"))
        self.label_4.setText(_translate("CreateInformation", "Описание вкуса"))
        self.ExitPushButton.setText(_translate("CreateInformation", "Выйти"))