#!/usr/bin/python3
# -*- coding: utf-8 -*-
from diffmath.Function import Function
from math import *


class FunctionArray:
    def __init__(self):
        self.array = []
        self.createFunctions()

    def createFunctions(self):
        self.array.append(Function("1",
            lambda x, y: 2*(x*x+y),
            lambda x: 1.5*exp(2*x) - x*x - x - 0.5))
        self.array.append(Function("2", lambda a, b: a * b*2, lambda a: a * 2))
        self.array.append(Function("3", lambda a, b: a * b*3, lambda a: a * 3))
        self.array.append(Function("4", lambda a, b: a * b*4, lambda a: a * 4))
        self.array.append(Function("5", lambda a, b: a * b*5, lambda a: a * 5))

    def getNames(self):
        names = []
        for function in self.array:
            names.append(function.getName())
        return names

    def getFunction(self, index):
        if len(self.array) > index and index >= 0:
            return self.array[index]