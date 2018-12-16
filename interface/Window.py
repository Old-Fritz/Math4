#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout

from interface.Chart import Chart
from interface.SetPanel import SetPanel


class Window(QWidget):

    def __init__(self, width, height):
        super().__init__()
        self.initUI(width, height)

    def initUI(self, width, height):
        self.setGeometry(0, 0, width, height)
        self.setWindowTitle('VMLab4')
        layout = QVBoxLayout()
        self.setLayout(layout)

        # init SetPanel
        setPanel = SetPanel()
        layout.addWidget(setPanel, 1)

        # init chart
        chart = Chart()
        layout.addWidget(chart, 6)
        chart.drawPoints([[0, 2], [1, 3], [2, 2]], "qwe")
        chart.drawPoints([[0, 3], [1, 4], [2, 1], [3, 52]], "rty")

        self.show()
