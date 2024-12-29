import utime
from uQR import QRCode
import micropython, gc
import rp2040_lcd_128

def create_matrix(data):
    print(f'Generating code for: {data}')
    qr = QRCode(border=0)
    t = utime.ticks_ms()
    qr.add_data(data)
    matrix = qr.get_matrix()
    print(f'Done in {utime.ticks_diff(utime.ticks_ms(), t)} ms')

    rows = len(matrix)
    cols = 0
    for row in matrix:
        cols = max(cols, len(row))
            
    print(f'Matrix size: {rows} x {cols}')
    print()
    return matrix

if __name__=='__main__':
    print('QR Code Test')
    print('============')

    matrix = create_matrix('abc')
    
    gc.collect()
    print(micropython.mem_info())
    utime.sleep(1)

    display = rp2040_lcd_128.LCD_1inch28() # out of memory  :-(
    print("RP2040-LCD-1.28 initiated")
