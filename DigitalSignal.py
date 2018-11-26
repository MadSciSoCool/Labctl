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
        super().__init__(chan_type="di")
        self.number = number

    def _set(self, obj):
        pass

    def _get(self, obj):
        return obj._read(self.number, self.chan_type)


class DO(DigitalSignal):
    def __init__(self, number):
        super().__init__(chan_type="do")
        self.number = number

    def _set(self, obj, value):
        obj._write(self.number, self.chan_type, value)

    def _get(self, obj):
        pass
