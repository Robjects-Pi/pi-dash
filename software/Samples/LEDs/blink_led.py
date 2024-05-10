#The blink medthod is used to make the LED blink, here is how it is used with the PWMLED:


from gpiozero import PWMLED
from signal import pause

# Set up of the PWMLED objects for the 3 LEDs
blue_led = PWMLED(18)
red_led = PWMLED(13)
green_led = PWMLED(12)



#The blink method is used to make the LED blink, here is how it is used with the PWMLED:
#The on_time parameter is used to set the time the LED is on
#The off_time parameter is used to set the time the LED is off
#The n parameter is used to set the number of times the LED blinks

blue_led.blink(on_time=1, off_time=1, n=5) #LED blinks 5 times
red_led.blink(on_time=1, off_time=1, n=5) #LED blinks 5 times
green_led.blink(on_time=1, off_time=1, n=5) #LED blinks 5 times


#The pause function is used to keep the program running and to keep the LED on
#pause() 
