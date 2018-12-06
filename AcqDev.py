import nidaqmx
from nidaqmx.constants import TerminalConfiguration
from nidaqmx.stream_readers import AnalogSingleChannelReader

class AcqDev:

    def __init__(self, device_name="Dev1"):
        self.name = device_name
        self.ai_chan = []
        self.task = nidaqmx.Task()

    def add_test_ai_chan(self, channel):
        if channel not in self.ai_chan:
            test_task = nidaqmx.Task()
            channel_name = self.name + '/ai' + str(channel)
            test_task.ai_channels.add_ai_voltage_chan(channel_name, terminal_config=TerminalConfiguration.RSE)
            reader = AnalogSingleChannelReader(test_task.in_stream)
            return reader

    def add_ttl_chan(self, num_of_chan, sample_rate, maximum_sample):
        if num_of_chan < 32:
            self.task


