import string
from serial import Serial


class Thermometer:
    def __init__(self, port, baudrate=115200):
        self._serial = Serial(port, baudrate)

    def trigger(self) -> string:
        self._serial.write(b'Y\r\n')
        self._serial.readline()
        data = self._serial.read_until().strip().decode('utf8')
        try:
            temperature, humidity = (
                data.split(':')
            )
        except ValueError:
            return
        response = "temperature: {}°C, humidité: {}%".format(temperature, humidity)
        print(response)
