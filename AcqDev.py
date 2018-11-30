import nidaqmx
from nidaqmx.constants import TerminalConfiguration
from AnalogReader import AnalogReader

class AcqDev:

    def __init__(self, device_name="Dev1"):
        self.name = device_name
        self.ai_chan = []

    def add_ai_chan(self, channel, data_points_per_read):
        this_task = nidaqmx.Task()
        channel_name = self.name + '/ai' + str(channel)
        this_task.ai_channels.add_ai_voltage_chan(channel_name, terminal_config=TerminalConfiguration.RSE)
        reader = AnalogReader(this_task, data_points_per_read)
        return reader


