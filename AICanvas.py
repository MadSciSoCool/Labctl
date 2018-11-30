from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

SAMPLE_PERIOD = 0.000002


class AICanvas(FigureCanvas):
    def __init__(self, width=9, height=5, dpi=100, samples_per_screen=300, refresh_rate=1):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super().__init__(self.fig)
        self.refresh_rate = refresh_rate
        self.length = samples_per_screen

        # generate two subplots
        self.time_domain = self.fig.add_subplot(211)
        self.freq_domain = self.fig.add_subplot(212)

        # set data axis
        self.time_axis = np.arange(0, SAMPLE_PERIOD * samples_per_screen, SAMPLE_PERIOD)
        self.freq_axis = np.fft.rfftfreq(n=samples_per_screen)

        # initialize data and plot
        self.data = np.zeros(samples_per_screen)
        self.fft_data = np.fft.rfft(self.data)
        self._plot()

    def _plot(self):
        self.time_domain.cla()
        self.time_domain.plot(self.time_axis, self.data)

        self.freq_domain.cla()
        self.freq_domain.plot(self.freq_axis, self.fft_data.real)
        self.freq_domain.plot(self.freq_axis, self.fft_data.imag)

        self.draw()

    def refresh_data(self, source):
        self.data = self.data[self.refresh_rate:self.length]
        self.data = np.hstack([self.data, source])
        self.fft_data = np.fft.rfft(self.data)
        self._plot()
