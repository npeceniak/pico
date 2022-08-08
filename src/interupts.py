import machine
import utime

led_red = machine.Pin(10, machine.Pin.OUT)
led_green = machine.Pin(11, machine.Pin.OUT)


# Turn LED off
led_red.value(0)

button_1 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

def interuptHandler(pin):
    print(f"Interupt Detected on pin {pin}")
    # Temporatly set handler to none so that the handler is not avaliable while it is running.
    button_1.irq(handler=None, trigger=machine.Pin.IRQ_RISING)  # type: ignore
    led_red.value(1)
    utime.sleep(5)
    led_red.value(0)
    # reset handler so it can be called again. 
    button_1.irq(handler=interuptHandler, trigger=machine.Pin.IRQ_RISING)


button_1.irq(handler=interuptHandler, trigger=machine.Pin.IRQ_RISING)

while True:
    led_green.toggle()
    utime.sleep(1)