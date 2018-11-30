class AnalogReader:

    def __init__(self, task, dppr):
        self.task = task
        self.dppr = dppr

    def read(self):
        return self.task.read(number_of_samples_per_channel=self.dppr)

    def __del__(self):
        self.task.close()
