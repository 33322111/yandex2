from sys import argv, exit
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.mouse)

    def mouse(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawing(qp)
        qp.end()

    def drawing(self, qp):
        qp.setBrush(QColor('Yellow'))
        a = randint(1, 150)
        qp.drawEllipse(randint(151, 760), randint(151, 480), a, a)


if __name__ == '__main__':
    app = QApplication(argv)
    ex = Main()
    ex.show()
    exit(app.exec())
