import machine
import utime

fanA = machine.Pin(6, machine.Pin.OUT)
fanB = machine.Pin(7, machine.Pin.OUT)

button_A = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_B = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)

while True:

    if button_A.value() == 1:
        print("Button 1")
        fanA.toggle()
        utime.sleep(0.5)

    if button_B.value() == 0:
        print("Button 2")
        fanB.toggle()
        utime.sleep(0.5)