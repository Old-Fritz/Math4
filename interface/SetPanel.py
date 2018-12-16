#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


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
        for i in range(0,4):
            el = QLabel(labels[i], self)
            layout.addWidget(el, 0, i, Qt.AlignCenter)

        # second row
        comboBox = self.createComboBox(functionNames)
        layout.addWidget(comboBox, 1, 0, Qt.AlignCenter)

        for i in range(1,4):
            el = QLineEdit()
            el.setValidator(QDoubleValidator())
            layout.addWidget(el, 1, i, Qt.AlignCenter)

        #button
        button = QPushButton("Вычислить")
        layout.addWidget(button, 0, 4, 2, 1, Qt.AlignCenter)


    def createComboBox(self, names):
        comboBox = QComboBox()
        comboBox.addItems(names)
        return comboBox


