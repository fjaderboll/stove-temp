# Stove Temperature
A modified version of an ordinary stove fan, where the thermoelectric generator
is also powering a display and a microcontroller showing the temperature of the
stove.

Historical values can be extracted via a QR-code on the display.

## Setup

### Hardware
* Microcontroller + display: [RP2040-LCD-1.28](https://www.waveshare.com/wiki/RP2040-LCD-1.28)
* Temperature sensor(s): DS18B20 (-55°C till 125°C)

### Software
Install MicroPython on the microcontroller. Display didn't work using official `1.24.1`, had to
use the bundled `rp2-pico-20220117-v1.18.uf2`.

## Historical data
1. Do action X to bring up the QR-code and scan
2. Input string to script Y to format it into a csv-file
