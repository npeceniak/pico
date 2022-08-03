from machine import Pin
import time
import os

os.listdir()

pin = Pin(25, Pin.OUT)

print("Running Main.py")
counter = 0
while True:
    counter+=1
    pin.toggle()
    time.sleep_ms(1000)
    print("Seconds Running: " + str(counter))
