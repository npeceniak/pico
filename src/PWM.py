import machine
import utime

led_red = machine.PWM(machine.Pin(10))
potentiometer = machine.ADC(26)

led_red.freq(1000)

while True:
    potVal = potentiometer.read_u16()
    # This allows the led to go completly off.
    potVal = 0 if potVal < 1000 else potVal
    print(f"Value: {potVal}")
    led_red.duty_u16(potVal)