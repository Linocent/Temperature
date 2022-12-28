from .thermometer import Thermometer


class TriggerThermometer:

    def trigger(self):
        Thermometer('/dev/ttyUSB0').trigger()

