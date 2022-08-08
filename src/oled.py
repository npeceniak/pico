import machine
from deps.ssd1306 import SSD1306_I2C
import src.Potentiometer as POT
import time

def run():
    WIDTH = 128
    HEIGHT = 64

    i2c = machine.I2C(0, scl=machine.Pin(17), sda=machine.Pin(16), freq=400000)

    oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

    while True:
        convertedBarValue = int(POT.readPotValue() / 512)
        print(f"Bar size: {convertedBarValue}")
        oled.fill(0)
        oled.fill_rect(0, 0, convertedBarValue, HEIGHT, 1)
        oled.show()
        time.sleep_ms(100)