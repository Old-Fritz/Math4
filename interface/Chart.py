#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import *
from PyQt5.QtChart import *


class Chart(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        #create Qchart
        chart = QChart()
        chartView = QChartView(chart)
        layout.addWidget(chartView)



