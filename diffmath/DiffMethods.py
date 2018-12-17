#!/usr/bin/python3
# -*- coding: utf-8 -*-


class OneStepMethod:
    @staticmethod
    def calculate(function, y0, x0, delta, count):
        result = [[x0, y0]]
        x = x0
        for i in range(1, count):
            x += delta
            k0 = function(result[i-1][0], result[i-1][1])
            k1 = function(result[i-1][0] + delta/2, result[i-1][1] + delta*k0/2)
            k2 = function(result[i-1][0] + delta/2, result[i-1][1] + delta*k1/2)
            k3 = function(result[i-1][0] + delta, result[i-1][1] + delta*k2)
            y = result[i-1][1] + delta/6*(k0 + 2*k1 + 2*k2 + k3)
            result.append([x, y])

        return result


class MilnMethod:
    @staticmethod
    def calculate(function, y0, x0, end, precision):
        delta = precision
        count = int(abs((end-x0)/delta))

        result = OneStepMethod.calculate(function, y0, x0, delta, 4)
        x = x0 + delta * 3
        for i in range(4, count):
            x += delta
            predY = result[i - 4][1] + 4 * delta / 3 * (
                    2 * function(result[i - 3][0], result[i - 3][1]) -
                    function(result[i - 2][0], result[i - 2][1]) +
                    2 * function(result[i - 1][0], result[i - 1][1]))

            while True:
                y = result[i - 2][1] + delta / 3 * (
                        function(result[i - 2][0], result[i - 2][1]) +
                        4 * function(result[i - 1][0], result[i - 1][1]) +
                        function(x, predY))
                if abs(predY-y) < precision:
                    break
                else:
                    predY = y

            result.append([x, y])

        return result
