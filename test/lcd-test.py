import time
import rp2040_lcd_128

if __name__=='__main__':
    display = rp2040_lcd_128.LCD_1inch28()
    qmi8658 = rp2040_lcd_128.QMI8658()
    battery = rp2040_lcd_128.Battery()
    
    print("RP2040-LCD-1.28 initiated")
    
    while(True):
        #read QMI8658
        xyz = qmi8658.Read_XYZ()
        
        display.fill(display.white)
        
        display.fill_rect(0,0,240,40,display.red)
        #display.text("Hello!",60,25,display.white)
        display.write_text("size3",60,15,3,display.green)
        
        display.fill_rect(0,40,240,40,display.blue)
        display.write_text("size1",60,43,1,display.white)
        display.write_text("size2",60,57,2,display.white)
        
        display.fill_rect(0,80,120,120,0x1805)
        display.text("ACC_X={:+.2f}".format(xyz[0]),20,100-3,display.white)
        display.text("ACC_Y={:+.2f}".format(xyz[1]),20,140-3,display.white)
        display.text("ACC_Z={:+.2f}".format(xyz[2]),20,180-3,display.white)

        display.fill_rect(120,80,120,120,0xF073)
        display.text("GYR_X={:+3.2f}".format(xyz[3]),125,100-3,display.white)
        display.text("GYR_Y={:+3.2f}".format(xyz[4]),125,140-3,display.white)
        display.text("GYR_Z={:+3.2f}".format(xyz[5]),125,180-3,display.white)
        
        display.fill_rect(0,200,240,40,0x180f)
        Vbat = battery.read_voltage()
        display.text("Vbat={:.2f}".format(Vbat),80,215,display.white)
        
        display.show()
        
        #print("ACC_X={:+.2f} ACC_Y={:+.2f} ACC_Z={:+.2f} GYR_X={:+3.2f} GYR_Y={:+3.2f} GYR_Z={:+3.2f} Vbat={:.2f}".format(xyz[0],xyz[1],xyz[2],xyz[3],xyz[4],xyz[5],reading))
        time.sleep(0.1)
