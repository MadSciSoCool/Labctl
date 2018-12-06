import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QApplication, QGraphicsScene
from AICanvas import AICanvas
from AnalogInputWidget import Ui_Form
from AcqDev import AcqDev


class AIWidget(QWidget):

    def __init__(self, reader):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.reader = reader

        self.canvas = AICanvas()

        # create a timer to control reading and refreshing
        self.timer = QTimer()
        self.timer.timeout.connect(self._update_plot)
        self.timer.start(1)

        # link the canvas to the graphical view
        self.scene = QGraphicsScene()
        self.scene.addWidget(self.canvas)
        self.ui.graphicsView.setScene(self.scene)
        self.ui.graphicsView.show()

        self.show()

    def _update_plot(self):
        self.canvas.refresh_data(self.reader.read_one_sample())


if __name__ == "__main__":
    dev = AcqDev()
    reader = dev.add_test_ai_chan(channel=0)
    app = QApplication(sys.argv)
    ui = AIWidget(reader=reader)
    sys.exit(app.exec())
