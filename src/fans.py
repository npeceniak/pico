import machine
import utime
 
potentiometer = machine.ADC(26)

fan0 = machine.PWM(machine.Pin(6))
fan1 = machine.PWM(machine.Pin(7))
 
button_0 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
 

led_green = machine.Pin(11, machine.Pin.OUT)
led_blue = machine.Pin(14, machine.Pin.OUT)
led_red = machine.PWM(machine.Pin(10))

led_green.value(0)
led_blue.value(0)

fan0.freq(100)
fan1.freq(100)
led_red.freq(100)

activeFan = 0
fan0SpeedValue = 65535
fan1SpeedValue = 65535
 
while True:
    potValue = potentiometer.read_u16()
    potValue = 0 if potValue < 5000 else potValue
    led_red.duty_u16(potValue)
    print(f"Fan {activeFan} active")
    print(potValue)

    if button_0.value() == 1:
        activeFan = (activeFan + 1) % 2
        print("Button 1")

    if activeFan == 0:
        fan0SpeedValue = potValue
        led_green.value(0)
        led_blue.value(1)
        fan0.duty_u16(fan0SpeedValue)
    else:
        fan1SpeedValue = potValue
        led_green.value(1)
        led_blue.value(0)
        fan1.duty_u16(fan1SpeedValue)
        
    utime.sleep(0.25) 

