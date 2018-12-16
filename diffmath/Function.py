#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Function:
    def __init__(self, name, differential, original):
        self.name = name
        self.differential = differential
        self.original = original

    def getName(self):
        return self.name

    def getDiff(self):
        return self.differential

    def getOriginal(self):
        return self.original

    def toPointsOriginal(self, start, end, step):
        points = []
        count = int(abs((end-start)/step))
        x = start
        for i in range(0,count):
            points.append([x, self.original(x)])
            x += step
        return points
