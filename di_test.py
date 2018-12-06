import nidaqmx
from nidaqmx.constants import LineGrouping
from nidaqmx.stream_writers import DigitalSingleChannelWriter
import numpy as np

delay = 3*(10**7)
a = np.empty(delay, dtype="uint32")
for i in range(delay):
    a[i] = 0
a[delay-1] = 1
with nidaqmx.Task() as task:
    task.do_channels.add_do_chan("Dev1/port0/line0:0", line_grouping=LineGrouping.CHAN_PER_LINE)
    writer = DigitalSingleChannelWriter(task.out_stream, auto_start=True)
    writer.write_many_sample_port_uint32(a)
