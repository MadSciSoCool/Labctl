from Signal import Signal


class DigitalSignal(Signal):

    def __init__(self):
        super().__init__()

    @staticmethod
    def from_dev(value):
        return value

    @staticmethod
    def to_dev(value):
        if value == 0:
            return False
        else:
            return True


class DI(DigitalSignal):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def _set(self, obj):
        pass

    def _get(self, obj):
        return obj._read(self.number)


class DO(DigitalSignal):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def _set(self, obj, value):
        obj._write(self.number, value)

    def _get(self, obj):
        pass
