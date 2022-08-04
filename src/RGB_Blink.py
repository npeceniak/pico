import machine
import utime
import random

def run():
    print("Run function RGB_Blink")
    blink_loop()

def blink_loop():
    led_red = machine.Pin(10, machine.Pin.OUT)
    led_green = machine.Pin(11, machine.Pin.OUT)
    led_blue = machine.Pin(14, machine.Pin.OUT)
    onboard_led = machine.Pin(25, machine.Pin.OUT)
    counter = 0

    while True:
        counter+=1
        onboard_led.value(gen_random())
        led_red.value(gen_random())
        led_green.value(gen_random())
        led_blue.value(gen_random())
        utime.sleep(1)

        print(f'End of loop {counter}')
        

def gen_random():
    retval = random.choice([0, 1])
    print(f'Random {retval}')
    return retval

