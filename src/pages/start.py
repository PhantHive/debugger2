from decimal import Decimal

import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QLineEdit, QComboBox, QGraphicsDropShadowEffect

from src.canvas.Canvas import Canvas


class StartWin(object):

    def __init__(self):
        self.screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.width = int(self.screen.width() * 0.50)
        self.height = int(self.screen.height() * 0.55)

        self.onlyInt = QIntValidator()
        self.lang = None

        self.change_eq = None  # change equation

    def setupUI(self, StartWin):

        StartWin.setGeometry((self.screen.width() - self.width) // 2, (self.screen.height() - self.height) // 2, self.width, self.height)
        StartWin.setFixedSize(self.width, self.height)

        StartWin.setWindowTitle(self.lang["app-title"] + " \ " + self.lang["start"])

        self.IPWidgets = QWidget(StartWin)
        self.canvas = Canvas(self.IPWidgets)
        self.canvas.resize(475, 275)
        self.canvas.move(370, 500)

        '''layout = QtWidgets.QVBoxLayout(self.IPWidgets)
        layout.addWidget(self.canvas)
        self.IPWidgets.setLayout(layout)'''

        # self.toolbar = NavigationToolbar(self.canvas, StartWin)

        # test

        self.language = QPushButton(self.IPWidgets)
        self.language.setText(self.lang["language"])

        self.entry_widgets()
        self.result_widgets()
        self.move_widgets()

        StartWin.setCentralWidget(self.IPWidgets)

    def entry_widgets(self):
        # self.calcul.clicked.connect(self.calculate)
        self.change_eq = QPushButton(self.IPWidgets)  # change equation

    def result_widgets(self):
        # Result
        pass

    def move_widgets(self):
        self.language.move(int(self.width * 0.92), int(self.height * 0.015))
        self.change_eq.move(int(self.width * 0.1), int(self.height * 0.1))

    def calculate(self):
        pass
