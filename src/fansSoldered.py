import machine
import utime

onboard_led = machine.Pin(25, machine.Pin.OUT)

button_0 = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
button_1 = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_UP)

fan0 = machine.Pin(2, machine.Pin.OUT)
fan1 = machine.Pin(3, machine.Pin.OUT)

while True:

    if button_0.value() == 0:
        onboard_led.toggle()
        fan0.toggle()
        utime.sleep(0.5)

    if button_1.value() == 0:
        onboard_led.toggle()
        fan1.toggle()
        utime.sleep(0.5)