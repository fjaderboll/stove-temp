import time
import math
import rp2040_lcd_128
import ds_sensors

TEMP_REFRESH_INTERVAL = 5 # seconds
BATT_REFRESH_INTERVAL = 15 # seconds

if __name__=='__main__':
    display = rp2040_lcd_128.LCD_1inch28()
    qmi8658 = rp2040_lcd_128.QMI8658()
    battery = rp2040_lcd_128.Battery()
    sensors = ds_sensors.DsSensors(22)
    
    print("RP2040-LCD-1.28 initiated")
    
    last_temp_time = 0
    last_batt_time = 0
    temps = []
    Vbat = 0.0
    while(True):
        xyz = qmi8658.Read_XYZ()
        if time.time() - last_temp_time > TEMP_REFRESH_INTERVAL:
            temps = sensors.read_temperatures()
            last_temp_time = time.time()
        
        if time.time() - last_batt_time > BATT_REFRESH_INTERVAL:
            Vbat = battery.read_voltage()
            last_batt_time = time.time()

        # Calculate roll angle from accelerometer data (in degrees)
        # Roll is the tilt left-right when display is flat on wall
        # Positive = leaning right, Negative = leaning left, 0 = level
        # Using X and Y axes for roll calculation
        roll_rad = math.atan2(xyz[0], xyz[1])
        roll_deg = math.degrees(roll_rad)
        roll_deg += 90
        
        #display.fill(display.white)
        
        display.fill_rect(0,0,240,40,display.red)        
        # Draw horizon line showing the inverted roll angle (compensating for tilt)
        center_x = 120
        center_y = 20
        line_length = 100
        line_rad = math.radians(-roll_deg)
        x1 = int(center_x - line_length * math.cos(line_rad))
        y1 = int(center_y - line_length * math.sin(line_rad))
        x2 = int(center_x + line_length * math.cos(line_rad))
        y2 = int(center_y + line_length * math.sin(line_rad))
        display.line(x1, y1, x2, y2, display.white)
        display.write_text("Roll",90,5,2,display.green)
        display.write_text("{:+.0f} *C".format(roll_deg),90,25,2,display.green)
        
        display.fill_rect(0,40,240,40,display.blue)
        display.write_text("temp",60,43,1,display.white)
        if len(temps) > 0:
            display.write_text(str(temps[0]),60,57,2,display.white)
        
        display.fill_rect(0,80,120,120,0x1805)
        display.write_text("ACC_X",30,82,1,display.white)
        display.write_text("{:+.2f}".format(xyz[0]),30,95,2,display.white)
        display.write_text("ACC_Y",30,122,1,display.white)
        display.write_text("{:+.2f}".format(xyz[1]),30,135,2,display.white)
        display.write_text("ACC_Z",30,162,1,display.white)
        display.write_text("{:+.2f}".format(xyz[2]),30,175,2,display.white)

        display.fill_rect(120,80,120,120,0xF073)
        display.write_text("GYR_X",130,82,1,display.white)
        display.write_text("{:+.2f}".format(xyz[3]),130,95,2,display.white)
        display.write_text("GYR_Y",130,122,1,display.white)
        display.write_text("{:+.2f}".format(xyz[4]),130,135,2,display.white)
        display.write_text("GYR_Z",130,162,1,display.white)
        display.write_text("{:+.2f}".format(xyz[5]),130,175,2,display.white)
        
        display.fill_rect(0,200,240,40,0x180f)
        display.write_text("Vbat",80,205,1,display.white)
        display.write_text("{:+.2f}".format(Vbat),80,215,2,display.white)

        display.show()
        time.sleep(0.1)


