from Signal import Signal


class AnalogSignal(Signal):

    def __init__(self):
        super().__init__()

    @staticmethod
    def from_dev(value):
        return value

    @staticmethod
    def to_dev(value):
        return value


class AI(AnalogSignal):
    def __init__(self, number):
        super().__init__(chan_type="ai")
        self.number = number

    def _set(self, obj):
        pass

    def _get(self, obj):
        return obj._read(self.number, self.chan_type)


class AO(AnalogSignal):
    def __init__(self, number):
        super().__init__(chan_type="ao")
        self.number = number

    def _set(self, obj, value):
        obj._write(self.number, self.chan_type, value)

    def _get(self, obj):
        pass
