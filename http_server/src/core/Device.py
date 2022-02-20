from Identifiable import Identifiable
from Serializable import Serializable


class Device(Identifiable, Serializable):

    def __init__(self, *, uuid=None, serial_number):
        Serializable.__init__(self, ["uuid", "serial_number"])
        Identifiable.__init__(self, uuid)
        self._serial_number = serial_number

    @property
    def serial_number(self):
        return self._serial_number


__all__ = ["Device"]
