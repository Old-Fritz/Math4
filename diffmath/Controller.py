#!/usr/bin/python3
# -*- coding: utf-8 -*-
from diffmath.FunctionArray import FunctionArray


class Controller:
    window = None
    functionArray = None

    @staticmethod
    def __init__(window, functionArray):
        Controller.window = window
        Controller.functionArray = functionArray

    @staticmethod
    def calculate(funcInd, x0, y0, end, precision):
        function = Controller.functionArray.getFunction(funcInd)
        Controller.window.drawResult(function.toPointsResult(x0*2, end, precision), function.toPointsResult(x0, end, precision))

