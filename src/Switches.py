# Two buttons and three LEDs
# Button 1 = Red LED
# Button 2 = Green LED
# Both = Blue LED

import machine
import utime

def run():
    print("Running Switches")
    led_red = machine.Pin(10, machine.Pin.OUT)
    led_green = machine.Pin(11, machine.Pin.OUT)
    led_blue = machine.Pin(14, machine.Pin.OUT)
    onboard_led = machine.Pin(25, machine.Pin.OUT)
    button_1 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
    button_2 = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)

    while True:
        led_red.value(0)
        led_green.value(0)
        led_blue.value(0)

        if button_1.value() == 1 and button_2.value() == 0:
            led_red.value(0)
            led_green.value(0)
            led_blue.value(1)
        else:
            if button_1.value() == 1:
                print("Button 1")
                led_green.value(1)

            if button_2.value() == 0:
                print("Button 2")
                led_red.value(1)

        utime.sleep(0.1)
        onboard_led.toggle()

    