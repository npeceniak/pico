# This file will run automatically when the Pi is powered up.

# Import modules from the src directory here
import src.RGB_Blink as RGB_Blink
import src.Switches as Switches
print("Running Main.py")

# Call any functions from the imported modules above here
# RGB_Blink.run()
Switches.run()