from machine import Pin
import ds18x20
import onewire
import time

class DsSensors:
	def __init__(self, gpio):
		self.pin = Pin(gpio)
		self.ds = ds18x20.DS18X20(onewire.OneWire(self.pin))
		self.roms = self.ds.scan()
	
	def get_sensor_count(self):
		return len(self.roms)
	
	def read_temperatures(self):
		temperatures = []
		if self.get_sensor_count() > 0:
			self.ds.convert_temp()
			time.sleep_ms(750)
			for rom in self.roms:
				temperatures.append(self.ds.read_temp(rom))
		return temperatures
