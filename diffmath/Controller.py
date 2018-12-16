#!/usr/bin/python3
# -*- coding: utf-8 -*-
from diffmath.DiffMethods import MilnMethod
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
        calculatedPoints = MilnMethod.calculate(function.getDiff(), y0, x0, end, precision)
        originalPoints = function.toPointsOriginal(x0, end, precision)
        Controller.window.drawResult(calculatedPoints, originalPoints)

