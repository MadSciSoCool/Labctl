import sys
from PyQt5.QtCore import QTimer
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi
from MyCanvas import *
from SinGen import *


class UiOsci(QWidget):

    def __init__(self):
        super().__init__()
        loadUi('osci.ui', self)

        # self.pushButton.clicked.connect()

        self.sin_gen = SinGen()
        self.sinTimer = QTimer()
        self.sinTimer.timeout.connect(self.sin_gen.add_count)
        self.sinTimer.start(100)

        self.Canvas = MyCanvas()
        self.timer = QTimer()
        self.timer.timeout.connect(self._update_plot)
        self.timer.start(100)

        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addWidget(self.Canvas)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.show()
        self.show()

    def _update_plot(self):
        self.Canvas.refresh_data(self.sin_gen.get_value())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = UiOsci()
    sys.exit(app.exec())
