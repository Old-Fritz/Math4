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
    def calculate(funcName, start, end, precision):
        function = Controller.functionArray.getFunction(funcName)
        Controller.window.drawResult(function.toPointsResult(start*2, end, precision), function.toPointsResult(start, end, precision))

