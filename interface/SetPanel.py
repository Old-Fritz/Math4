#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from diffmath.Controller import Controller


class SetPanel(QWidget):

    def __init__(self, functionNames):
        super().__init__()
        self.initUI(functionNames)

    def initUI(self, functionNames):
        layout = QGridLayout()
        self.setLayout(layout)

        # view:
        # "Выберите функцию"     "X0"      "Y0"    "конец отрезка"   "точнсть"      button
        #    combobox         textField  textField   textField       textField

        # first row
        labels = ["Выберите функцию", "X0", "Y0", "Конец отрезка", "точность"]
        for i in range(0,5):
            el = QLabel(labels[i], self)
            layout.addWidget(el, 0, i, Qt.AlignCenter)

        # second row
        self.comboBox = self.createComboBox(functionNames)
        layout.addWidget(self.comboBox, 1, 0, Qt.AlignCenter)

        self.x0TextField = QLineEdit()
        self.x0TextField.setValidator(QDoubleValidator())
        layout.addWidget(self.x0TextField, 1, 1, Qt.AlignCenter)

        self.y0TextField = QLineEdit()
        self.y0TextField.setValidator(QDoubleValidator())
        layout.addWidget(self.y0TextField, 1, 2, Qt.AlignCenter)

        self.endTextField = QLineEdit()
        self.endTextField.setValidator(QDoubleValidator())
        layout.addWidget(self.endTextField, 1, 3, Qt.AlignCenter)

        self.precisionTextField = QLineEdit()
        self.precisionTextField.setValidator(QDoubleValidator())
        layout.addWidget(self.precisionTextField, 1, 4, Qt.AlignCenter)

        #button
        button = QPushButton("Вычислить")
        button.clicked.connect(self.clickCalculate)
        layout.addWidget(button, 0, 5, 2, 1, Qt.AlignCenter)


    def createComboBox(self, names):
        comboBox = QComboBox()
        comboBox.addItems(names)
        return comboBox

    def clickCalculate(self):
        try:
            # parse params
            index = int(self.comboBox.currentIndex())
            x0 = float(self.x0TextField.text().replace(',', '.'))
            y0 = float(self.y0TextField.text().replace(',', '.'))
            end = float(self.endTextField.text().replace(',', '.'))
            precision = float(self.precisionTextField.text().replace(',', '.'))
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Введите корректные значения", QMessageBox.Ok)
        try:
            Controller.calculate(index,x0,y0,end,precision)
        except:
            QMessageBox.warning(self, "Ошибка", "Ошибка вычисления", QMessageBox.Ok)






