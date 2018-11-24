
import nidaqmx
from DigitalSignal import *
from AnalogSignal import *

class channel:

    def __init__(self, number, task, signal_type):
        self.task = task
        type_select = {"ai": AI,
                       "ao": AO,
                       "di": DI,
                       "do": DO}
        self.signal = type_select[signal_type](number)

    def _read(self):
        pass

