#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication

from diffmath.Controller import Controller
from interface.Window import Window
from diffmath.FunctionArray import FunctionArray

if __name__ == '__main__':

    array = FunctionArray()

    app = QApplication(sys.argv)

    w = Window(800, 600, array.getNames())
    Controller.__init__(w, array)
    sys.exit(app.exec_())