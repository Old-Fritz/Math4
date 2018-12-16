#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from interface.Window import Window


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = Window(800, 600)

    sys.exit(app.exec_())