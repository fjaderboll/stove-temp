import utime
#import micropython, gc

#print(micropython.mem_info())
from uQR import QRCode  # 94 kB RAM

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
    #print(micropython.mem_info())

    create_matrix('hello')
    create_matrix('Hello World!')
    create_matrix('A_quick_brown_fox_jumps_over_the_lazy_dog')
    #create_matrix('A ') # broken???

    #print(micropython.mem_info())
    #del QRCode  # get ~60 kB back
    #gc.collect()
    #print(micropython.mem_info())
