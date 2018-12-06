import numpy as np


class ConfigError(Exception):
    pass


class DigitalWaveForm:

    def __init__(self, sample_rate=10, maximum_samples=10, maximum_channels=32):
        self.sample_rate = sample_rate
        self.maximum_samples = maximum_samples
        self.maximum_channels = maximum_channels
        self.sample_period = 1 / sample_rate
        self.maximum_time = maximum_samples / sample_rate
        self.number_of_channel = 0
        self.config = []

    def add_chan(self, time_cfg):
        if sum(time_cfg) > self.maximum_time:
            raise (ConfigError)
        elif self.number_of_channel == self.maximum_channels:
            raise (ConfigError)
        else:
            self.number_of_channel = self.number_of_channel + 1
            self.config.append(time_cfg)

    def delete_chan(self, number):
        del (self.config[number - 1])
        self.number_of_channel = self.number_of_channel - 1

    def get_one_cfg(self, number):
        return self.config[number - 1]

    def get_np_cfg(self):
        np_config = np.empty([self.maximum_samples, self.number_of_channel], dtype=bool)
        cursor_y = 0
        for config in self.config:
            flag = False
            cursor_x = 0
            for period in config:
                for i in range(int(period / self.sample_period)):
                    np_config[cursor_x, cursor_y] = flag
                    cursor_x = cursor_x + 1
                flag = not flag
                for i in range(cursor_x - 1, self.maximum_samples):
                    np_config[cursor_x, cursor_y] = False
            cursor_y = cursor_y + 1
        return np_config