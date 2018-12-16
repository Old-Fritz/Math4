#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout

from interface.Chart import Chart
from interface.SetPanel import SetPanel


class Window(QWidget):

    def __init__(self, width, height, functionNames):
        super().__init__()
        self.initUI(width, height, functionNames)

    def initUI(self, width, height, functionNames):
        self.setGeometry(0, 0, width, height)
        self.setWindowTitle('VMLab4')
        layout = QVBoxLayout()
        self.setLayout(layout)

        # init SetPanel
        setPanel = SetPanel(functionNames)
        layout.addWidget(setPanel, 1)

        # init chart
        self.chart = Chart()
        layout.addWidget(self.chart, 6)

        self.show()

    def drawResult(self, calculatedPoints, resultPoints):
        self.chart.clearPoints()
        self.chart.drawPoints(resultPoints, "original")
        self.chart.drawPoints(calculatedPoints, "calculated")

