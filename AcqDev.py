
import nidaqmx
import numpy as np

class AcqDev:

    def __init__(self, data_points_per_read=300, device_name = "Dev1"):
        self.task = nidaqmx.Task()
        self.dppr = data_points_per_read
        self.ai_chan = []

    def set_dppr(data_points_per_read):
        self.dppr = data_points_per_read

    def add_channel(self, number, chan_type):
        if chan_type == "ai":
            if number not in ai_chan:
                self.ai_chan.append(number)
                self.task.ai_channels.add_ai_voltage_chan(self.name + "/ai" + str(number))

    def close_channel(self, number, chan_type):
        # since no close method for single channel is found now, I will realize this method by shut down and rebuild the whole task object
        if chan_type == "ai":
            if number in ai_chan:
                ai_chan.remove(number)

    def _refresh(self)

    def _read(self, number, chan_type)

    def _write(self, number, chan_type, value)
