import machine
import utime
import random

fan0 = machine.Pin(6, machine.Pin.OUT)
fan1 = machine.Pin(7, machine.Pin.OUT)

fan0.value(1)
fan1.value(1)


while True:
    fan0.toggle()
    utime.sleep(5)
