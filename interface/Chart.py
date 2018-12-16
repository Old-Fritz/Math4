#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtChart import *


class Chart(QWidget):
    def __init__(self):
        super().__init__()
        self.chart = QChart()
        self.minY = self.minX = sys.float_info.max
        self.maxY = self.maxX = sys.float_info.min
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        # customise axis
        axisX = QValueAxis()
        axisX.setTitleText("X")
        self.chart.setAxisX(axisX)

        axisY = QValueAxis()
        axisY.setTitleText("Y")
        self.chart.setAxisY(axisY)

        # create  view
        chartView = QChartView(self.chart)
        chartView.setRenderHint(QStylePainter.Antialiasing)
        layout.addWidget(chartView)

    def drawPoints(self, points, name):
        self.chart.axisX()
        series = QLineSeries()
        series.setName(name)
        # fill series
        for point in points:
            self.refreashExt(point)
            series.append(QPointF(point[0], point[1]))

        # attach series to chart
        self.chart.addSeries(series)
        series.attachAxis(self.chart.axisX())
        series.attachAxis(self.chart.axisY())
        self.refreashAxes()

    def refreashExt(self, point):
        # refereash extreme points of axes
        if point[1] > self.maxY:
            self.maxY = point[1]
        if point[1] < self.minY:
            self.minY = point[1]
        if point[0] > self.maxX:
            self.maxX = point[0]
        if point[0] < self.minX:
            self.minX = point[0]

    def refreashAxes(self):
        # set new extreme points for axes
        axisY = self.chart.axisY()
        axisY.setRange(self.minY, self.maxY)

        axisX = self.chart.axisX()
        axisX.setRange(self.minX, self.maxX)

    def clearPoints(self):
        self.minY = self.minX = sys.float_info.max
        self.maxY = self.maxX = sys.float_info.min
        self.chart.removeAllSeries()






