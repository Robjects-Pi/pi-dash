

# Pi-Dash
___________________
![](/images/overview-pi-dash.NEF)

A DIY Dashcam using Raspberry Pi<br>
<br>


Say hello to the world of DIY recording, and introduce yourself to your own DIY dashcam built and ported to a raspberry pi.  


<br>
<br>

***Table of Contents***
- [Pi-Dash](#pi-dash)
- [Overview](#overview)
  - [What you’ll find in this document](#what-youll-find-in-this-document)
    - [4.0: Printing out the electronics casing (OPTIONAL)](#40-printing-out-the-electronics-casing-optional)
  - [Remixing Pi-Dash for your projects](#remixing-pi-dash-for-your-projects)
    - [Hacking the software](#hacking-the-software)
    - [Hacking the Hardware](#hacking-the-hardware)
    - [Hacking the casing](#hacking-the-casing)
    - [OS \& compute](#os--compute)
    - [Software](#software)
    - [Electronics](#electronics)

# Overview
The pi dash was designed to simplify data collection, and teach you how to not only code your own recording device but build up the entire enclosure, mount, and set up of an automatic recording device from the endless capabilities of a raspberry Pi!  

With this, you will be able to go past the basic functionalities and limits of pre-built dashcams
and integrate your own solutions and features that extensive data collection and recording can provide.

With the tutorial, you will be able to build your own dashcam that records and stores video files in a location of your preference. The project is designed to be a simple, easy-to-follow guide to building a DIY dashcam using a Raspberry Pi Zero. The project is aimed at beginners and hobbyists who are interested in learning relevant implementations of DIY applications.

Also, by following this tutorial, you will learn about the basics of machine learning and computer vision, and how to apply these concepts to a real-world project. The project is designed to be a fun and engaging way to learn about these topics, and to inspire you to explore them further.


comes from variety of automatically record when utilizing your vehicle. This way, you manually store your data and recordings on a drive you can take out whenever you need it. The code is layed out so you can manipulate it as you please in case you want to add your own personal code with it.

<br>
<br>
## What you’ll find in this document

-  **[1. Setting up the rpi image](#User-guide)** -
Explaining functionality through prototype build through easy-to-follow tutorial aimed at how the project is working

-  **[2. Assembling and gathering components](#User-guide)** -
Explaining functionality through prototype build through easy-to-follow tutorial aimed at how the project is working

-  **[3. Setting up and testing pi dashcam for automatic recordings of preferred length](#Software-for-rpi)** -
An easy-to-follow software overview of services set on rpi to make automatic recording of camera whenever you turn on the device.
- **[4.  printing out the case for all your components(OPTIONAL) ](#)** -
A set of simple experiments to help understand how Alto works, and how you can use Alto to introduce some of the basic concepts of machine learning to others.

- **[5. Putting together the device with the car mounting equipment.Setting up your device in your car for aesthetic build](#)** -
A brief introduction to how you can hack your Alto to look and behave differently to fit your own application.


### 4.0: [Printing out the electronics casing (OPTIONAL)]()

You should now have a completed pi Dash unit – the next stage is to test it with the scripts included.


## [Remixing Pi-Dash for your projects](5.0-remixing-pi-dash.md)

All the hardware and software for Pi-Dash was created with hacking and remixing in mind: the case design can be made from different materials, or refactored entirely; the electronics can be adapted to use whatever components you have available;and the software is written in a high level language (Python) with optional bash scripts that are easy to modify. 

Here are just some of the ways you can hack your own pi-dash:

### Hacking the [software]()
Here are some options for hacking the software of the project:
- Adding a storage mechanism to send files to a personal cloud or storage device (see code for sending files to a server or external usb)
- Adding a button or external to start and stop recording based on electronic signal
- Adding a screen and creating software to turn it on or off

### Hacking the [Hardware]()
Here are some options for hacking the hardware of the project:
- Adding LED lights to create Pi-Dash heartbeats for is testing and debugging
- Adding a battery to make the device temporary portable in your car
- Adding a button to start and stop recording
- Adding a screen to display the current recording time

### Hacking the [casing]()
The casing for Alto can easily be changed to fit whatever application you might have in mind. Whether that’s simple aesthetic changes to modify Pi-Dash look, or changes to the design to make it more robust or portable, the casing is designed to be easy to modify.

Here are some options for hacking the casing of the project:
- Changing the material of the casing to make it more robust
- Changing the case for high heat environments for long term recording and hotter climates

- Creating a custom design for the casing of a raspberry pi 4 or 3
- Adding a mount to the casing to attach it to a tripod or other device


### OS & compute

The Raspberry Pi Zero runs Raspberry Pi OS. It is responsible for interfacing with the user’s connected hardware (connected via GPIO, USB or ribben cable).

### Software

The Alto software application is written in Python and bash (via scripts). It receives input from the Raspberry Pi camera module, prepares it for for storage organized via date/time. 


For more advanced developers looking into long-term storage for whatever data science application, I have put some code that is good starter for those looking to send files to their personal cloud or storage device once they are in proximity to wireless connection.



### Electronics

The electronics for the pi dash are designed to be as flexible and hackable as possible. It is based around a single through-hole prototyping board which can be assembled easily by hand. This board connects to the GPIO or via micro usb to a charger that outputs steady voltage/current to ensure your rpi doesn't break or slow down in recording while driving.
