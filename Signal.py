
class Signal:

    def __init__(self):
        pass

    def __get__(self, obj):
        return self.from_dev(self._get())

    def __set__(self, obj, value):
        self._set(self.to_dev)

    def __delete__(self):
        pass

    @staticmethod
    def from_dev(value):
        return value

    @staticmethod
    def to_dev(value):
        return value