from Adafruit_DHT import DHT11 as SENSOR, read
from time import time


class DHT11:
    def __init__(self):
        # The DHT11 sensor must be up for a least 2 seconds before it can be read
        self.last_read = time()
        self.humidity = 0
        self.fahrenheit = 0
        self.celsius = 0

    def _set_fahrenheit(self):
        self.fahrenheit = self.celsius * 9.0 / 5.0 + 32

    def _set_hum_temp(self, hum, temp):
        # Ignore large jumps in humidity
        if hum - self.humidity <= 50 or self.humidity == 0:
            self.celsius = temp
            self.humidity = hum
            self._set_fahrenheit()

    def read(self):
        if time() - self.last_read >= 3.0:
            self.last_read = time()
            humidity, celsius = read(SENSOR, 4)

            # Only update if valid data was received
            if humidity and celsius:
                self._set_hum_temp(humidity, celsius)

        return self.humidity, self.celsius, self.fahrenheit
