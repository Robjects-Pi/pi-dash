
### Electronics

The electronics for the pi dash are designed to be as flexible and hackable as possible. It is based around a single through-hole prototyping board which can be assembled easily by hand. This board connects to the GPIO or via micro usb to a charger that outputs steady voltage/current to ensure your rpi doesn't break or slow down in recording while driving. The board is designed to be easy to modify, so that you can add or remove components as needed. The electronics are designed to be easy to assemble and disassemble, so that you can easily access the components inside.


### Software

The Pi-dash software application is written in Python and bash (via scripts). It receives input from the Raspberry Pi camera module, prepares it for for storage organized via date/time. 


For more advanced developers looking into long-term storage for whatever data science application, I have put some code that is good starter for those looking to send files to their personal cloud or storage device once they are in proximity to wireless connection.



### Casing

The casing for the pi dash is designed to be easy to 3D print and assemble. It is made up of 3 parts: the top, the bottom, and the middle. The top and bottom are designed to be printed in a flexible material, while the middle is designed to be printed in a rigid material. The top and bottom are held together by screws, while the middle is held in place by the top and bottom. The casing is designed to be easy to assemble and disassemble, so that you can easily access the electronics inside.

### [Remixing Pi-Dash for your projects](remixing-pi-dash.md)
### Hacking the [Hardware]()
Here are some options for hacking the hardware of the project:
- Adding LED lights to create Pi-Dash heartbeats for is testing and debugging
- Adding a battery to make the device temporary portable in your car
- Adding a button to start and stop recording
- Adding a screen to display the current recording time
- Adding a GPS module to record the location of the videos


### Hacking the [software]()
Here are some options for hacking the software of the project:
- Adding a storage mechanism to send files to a personal cloud or storage device (see code for sending files to a server or external usb)
- Adding a button or external to start and stop recording based on electronic signal
- Adding a screen and creating software to turn it on or off based on recording status
- Adding a button to start and stop recording

### Hacking the [casing]()
The casing for Alto can easily be changed to fit whatever application you might have in mind. Whether that’s simple aesthetic changes to modify Pi-Dash look, or changes to the design to make it more robust or portable, the casing is designed to be easy to modify.

Here are some options for hacking the casing of the project:
- Changing the material of the casing to make it more robust
- Changing the case for high heat environments for long term recording and hotter climates

- Creating a custom design for the casing of a raspberry pi 4 or 3
- Adding a mount to the casing to attach it to a tripod or other device




### Other Operating Systems for Pi-Dash recording

In order to utilize motioneye for enabling recording when detection of motion, you can utilize raspian BullsEye OS as it has compabitibility with USB and cable camera using the legacy camera stack. 
For instructions, please follow this [guide](https://github.com/motioneye-project/motioneye/wiki/Install-on-Raspbian-Bullseye)