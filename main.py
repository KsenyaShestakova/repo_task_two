import random
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor, QPainterPath
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Координаты')
        self.qp = QPainter()
        self.flag = False
        self.coords = []
        self.push

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        self.qp.setBrush(
            QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

        self.qp.drawEllipse(x, y, random_int, random_int)
