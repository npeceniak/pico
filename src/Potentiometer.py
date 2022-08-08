import re
import machine
import utime

potentiometer = machine.ADC(26)
lowValue = 0


def readPotValue():
    # Theoretical value 0-65535
    # Actual value ~1000-65535
    return potentiometer.read_u16()

# while True:
#     print(f"From Potentiometer {readPotValue()}")
#     utime.sleep(1)


def readPotConstrained(constraint = 65535):
    potVal = potentiometer.read_u16()
    # This allows the led to go completly off.
    potVal = 0 if potVal < 1000 else potVal
    return potVal % constraint