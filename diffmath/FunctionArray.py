#!/usr/bin/python3
# -*- coding: utf-8 -*-
from diffmath.Function import Function
from math import *


class FunctionArray:
    def __init__(self):
        self.array = []
        self.createFunctions()

    def createFunctions(self):
        self.array.append(Function("Y'=2(x^2+Y)",
            lambda x, y: 2*(x*x+y),
            lambda x: 1.5*exp(2*x) - x*x - x - 0.5))
        self.array.append(Function("Y'=1+y^2/(4x^2))",
            lambda x, y: 1+(y*y)/(4*x*x),
            lambda x: 2*x-x/(log(pow(abs(x), 1/4)))))

        self.array.append(Function("Y'=1/cosx-ytgx",
            lambda x, y: 1/cos(x)-y*tan(x),
            lambda x: sin(x)+cos(x)))

    def getNames(self):
        names = []
        for function in self.array:
            names.append(function.getName())
        return names

    def getFunction(self, index):
        if len(self.array) > index and index >= 0:
            return self.array[index]