#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Function:
    def __init__(self, name, differential, result):
        self.name = name
        self.differential = differential
        self.result = result

    def getName(self):
        return self.name

    def getDiff(self):
        return self.differential

    def getResult(self):
        return self.result

    def toPointsResult(self, start, end, step):
        points = []
        while start <= end:
            points.append([start, self.result(start)])
            start += step
        return points
