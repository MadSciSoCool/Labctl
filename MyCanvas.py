from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


class MyCanvas(FigureCanvas):
    def __init__(self, width=10, height=8, dpi=100, unit=0.01, steps=300):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(MyCanvas, self).__init__(self.fig)

        # generate two subplots
        self.time_domain = self.fig.add_subplot(211)
        self.freq_domain = self.fig.add_subplot(212)

        # set data axis
        self.time_axis = np.arange(0, unit * steps, unit)
        self.freq_axis = np.fft.rfftfreq(n=steps)

        # initialize data and plot
        self.data = np.zeros(steps)
        self.fft_data = np.fft.rfft(self.data)
        self._plot()

    def _plot(self):
        self.time_domain.cla()
        self.time_domain.set_ylim(-1, 1)
        self.time_domain.plot(self.time_axis, self.data)

        self.freq_domain.cla()
        self.freq_domain.set_ylim(-200, 200)
        self.freq_domain.plot(self.freq_axis, self.fft_data.real)
        self.freq_domain.plot(self.freq_axis, self.fft_data.imag)

        self.draw()

    def refresh_data(self, source):
        self.data = self.data[1:len(self.data)]
        self.data = np.append(self.data, source)
        self.fft_data = np.fft.rfft(self.data)
        self._plot()
