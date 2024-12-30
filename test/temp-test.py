import time
import ds_sensors

sensors = ds_sensors.DsSensors(22)
print(f'Found {sensors.get_sensor_count()} sensor(s)')

if sensors.get_sensor_count() > 0:
	while True:
		print(sensors.read_temperatures())
		time.sleep(3)
