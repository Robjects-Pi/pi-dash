#Set up of 3 Gpios for the setting of the color of 3 different LED via PWM (Pulse Width Modulation) in case I want to use the flicker effect as notifcation.
#The flicker effect is not used in the current version of the software

'''

# Set up of the GPIOs for the PWM of the LEDs:
blue_led = 18
red_led = 13
green_led = 12

gpiozero is a library that allows to control the GPIOs of the Raspberry Pi. It is a high level library that allows to control the GPIOs without having to worry about the low level details of the GPIOs.
To install the library, run the following command in the terminal:'
'python3 -m pip gpiozero'

'''
from gpiozero import PWMLED
from time import sleep # Import of the sleep function from the time library

# Set up of the PWMLED objects for the 3 LEDs
blue_led = PWMLED(18)
red_led = PWMLED(13)
green_led = PWMLED(12)


# The following code is used to test the PWMLED blue_led

blue_led.value = 1   #LED fully on
sleep(1)
blue_led.value = 0.5  #LED half-brightness
sleep(1)
blue_led.value = 0    #LED fully off
sleep(1)

# The following code is used to test the PWMLED fade effect
#The range function is used to generate a sequence of numbers from 0 to 100 with a step of 1 (start, stop, step)

#fade
#fade in
for duty_cycle in range(0, 100, 1):
    blue_led.value = duty_cycle/100.0
    sleep(0.05)

#fade out
for duty_cycle in range(100, 0, -1):
    blue_led.value = duty_cycle/100.0
    sleep(0.05)

# You can use the following code to test the PWMLED using the pulse function
     

#from signal import pause # Import of the pause function from the signal library


blue_led.pulse(fade_in_time=1,fade_out_time=1, n=5,background=True) #LED fades in and out
#pause() #The pause function is used to keep the program run`ning and to keep the LED on
