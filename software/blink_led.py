#The blink medthod is used to make the LED blink, here is how it is used with the PWMLED:

from gpiozero import PWMLED
from signal import pause

blue_led = PWMLED(18)


blue_led.blink(on_time=1, off_time=1, n=5) #LED blinks 5 times

#pause() #The pause function is used to keep the program running and to keep the LED on