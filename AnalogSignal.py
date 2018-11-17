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
        super().__init__()
        self.number = number

    def _set(self, obj):
        pass

    def _get(self, obj):
        return obj._read(self.number)


class AO(AnalogSignal):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def _set(self, obj, value):
        obj._write(self.number, value)

    def _get(self, obj):
        pass
