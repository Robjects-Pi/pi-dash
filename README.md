# Pi-Dash - DIY Dashcam using Raspberry Pi<br>
<br>


Say Goodbye to personal injury scams, and introduce yourself to your own DIY dashcam built and ported to a raspberry pi. d The pi dash was designed to simplify data collection, and teach you how to automatically record when utilizing your vehicle. This way, you manually store your data and recordings on a drive you can take out whenever you need it. The code is layed out so you can manipulate it as you please in case you want to add your own personal code with it.

Using a computer like a raspberry pi zero, the project takes advantage of small form factor  to create a working, standalone device built from scratch that you combine or mix with unlimited capabilities. 

This repository contains instructions, files to run scripts and services required to record ongoing video with the option of running code automatically when the device turns on. Recordings are stored on an SD card (or USB drive) that you can remove any time you want a chance to review the footage. 

Many customizations are available, as I implemented a battery on my personal device to enable offline transfer of videos for extra security. Please feel free to fork, export the project, and utilize the project however you please.

\

 ![pidash image here](images/pidash.jpg)
<br>
<br>
 ![pidash installed image here](images/pidash-installed.jpg)
<br>
<br>
## What you’ll find in this document

This document has five chapters:

-  **[1. Setting up the rpi image](#User-guide)** -
Explaining functionality through prototype build through easy-to-follow tutorial aimed at how the project is working

-  **[2. Assembling and gathering components](#User-guide)** -
Explaining functionality through prototype build through easy-to-follow tutorial aimed at how the project is working

-  **[3. Setting up and testing pi dashcam for automatic recordings of preferred length](#Software-for-rpi)** -
An easy-to-follow software overview of services set on rpi to make automatic recording of camera whenever you turn on the device.
- **[4.  printing out the case for all your components(OPTIONAL) ](#Experiment-with-Alto)** -
A set of simple experiments to help understand how Alto works, and how you can use Alto to introduce some of the basic concepts of machine learning to others.

- **[5. Putting together the device with the car mounting equipment.Setting up your device in your car for aesthetic build](#Remixing-Alto-for-your-projects)** -
A brief introduction to how you can hack your Alto to look and behave differently to fit your own application.

~~- **[Technical overview](#Technical-Overview)** -
A more detailed overview of Alto’s software and electronics and how they function.<br>~~
<br>

> ## Instructional guide (prototype build)
> Here are the instructions for starting the basic prototype set to ensure that your pi is effectively recording using the camera you are working with and storing it in the location you write. I recommend you start with a raspberry pi zero to ensure compatibility and minimal form factor for the device intended for a specific purpose.
> 
> First, boot up your pi. You will need a way to easily utilize the header pins which can be done with ease using a spread out breadboard connected to the rpi zero using a breakout + cable. Keep in mind that this can be done instead with standard  breadboard pins but might not as resilient to tinkereres with vibrating and careless fingers. and your pi. 
> 
> Some additional (optional) hardware that will simplify and speed your development are:
> - - LED lights: used as hardware debugging measurements to track progress of running code/services the pi will run
> - resisters: in conjuction with LED  
> 
> ### Machine learning at its simplest
> 
> Alto has a camera on its front, and an arm and button on each side. Alto uses the camera to observe the world around it. The buttons are used to start learning, and Alto will point with its arm when it sees something it has learned to recognise. 
> 
> ![about alto animated gif](images/alto-readme-2.gif)<br>
> <br>
> 
> Alto can learn two classes of things. When Alto recognises one of them, it will point with its corresponding arm. Alto demonstrates machine learning at its most basic level: what you teach it to recognise is up to you!
> 
> ![alto points at fruit](images/alto-readme-3.gif)<br>
> <br>
> 
> ### Teaching Alto
> 
> To teach Alto to recognise an object, place the object in front of it, and press one of the buttons on the side. As Alto takes images to learn about the object, its arm will slowly raise. When Alto’s arm is stretched out horizontally, the learning process has finished. Now, when the same object is placed in front of it, Alto will point at the object.
> 
> The more you teach Alto about the same object, the better it will become at recognising that thing. You can teach Alto as many times as you like! Try teaching Alto more about an object by rotating the object to show different angles and place it at various distances, pressing the same button each time.
> 
> It's important to try and balance the amount of learning that Alto does on each side. If it learns about one object 5 times, but only once about another, then it is likely to be much better at recognising the one that it has seen more often.
> 
> 
> ![alto points at red apples](images/alto-readme-4.gif)
> <br>
> <br>
> ### Recognising objects
> 
> Start by teaching Alto to recognise a different object for each arm, for example, to teach Alto the difference between types of fruit, teach it about a red apple on one side, and a banana on the other. 
> 
> ![alto points at a red apple](images/alto-readme-5.gif)
> <br>
> <br>
> ### Recognising classes
> 
> Beyond recognising individual objects, you can teach Alto to recognise classes of objects. Building on what it has learned about red apples, could you teach it to recognise red objects in general, rather than just apples? Once Alto has learned to recognise two classes, can it correctly recognise a new red object that it hasn’t seen before?
> 
> ![alto points at red objects](images/alto-readme-6.gif)
> <br>
> <br>
> ### Forgetting
> 
> If you want to teach Alto something new, you can clear its memory by holding down both buttons simultaneously for 3 seconds. This will erase everything Alto was taught on both sides, and can’t be undone.
> 
> To learn about any of these processes in more detail, take a look at the [Experiment with Alto](#experiment-with-Alto) section below.
> 
> ![alto forgets](images/alto-readme-7.gif)
> <br>
> <br>
## Make your own Pi Dashcam
The following steps will guide you through the process of assembling your own Pi Dash: setting up the Raspberry Pi, soldering the electronics, and assembling a case to house all the components. To read a more detailed explanation of each step, click on the links in each section to go to the individual instruction pages. 

![soldering overhead](images/alto-readme-8.png)
<br>
<br>
### 1.0: [Set up the software](1.0-Set-up-the-software.md)

The first step is to setup the software environment for the dashcam, and then load the Python code that makes the code function. The Software & OS section outlines the process in full, starting with setting up the Raspberry Pi Zero, flashing the SD card and installing the depedencies and updates to your machine.

![terminal output installing software](images/alto-readme-9.gif)
<br>
<br>
### 2.0: [Build the electronics](2.0-Build-the-electronics.md)

The electronics for dashcam have been designed to be as simple and hackable as possible. You only need a few common components and basic soldering skills (OPTIONAL) to assemble everything. ~~A full step-by-step guide, with schematics and a bill of materials, is included in the Electronics directory in this repository.~~

![overhead shot of some electronics](images/alto-readme-10.png)
<br>
<br>
### 3.0: [ Setting up and testing pi dashcam for automatic recordings of preferred length ](3.0-Making-the-electronics-casing.md)



~~To begin, you will need to print out the [PDF template](casing/alto-paper-templates.pdf) and stick it to your materials. This will be your guide for cutting the cardboard into the correct shape. All the labels are printed on the template itself.~~


For more detailed instructions on this stage of constructing your Alto, refer to the [electronics casing](3.1-Making-the-electronics-casing.md) instructions.

![cutting out and assembling paper parts](images/alto-readme-11.gif)
<br>
<br>



![assembling alto's casing](images/alto-readme-12.gif)
<br>
<br>
### 4.0: [Printing out the electronics casing (OPTIONAL)](4.0-experiments-with-alto.md)

You should now have a completed pi Dash unit – the next stage is to test it with the scripts included.

~~Grab some objects, plug Alto into a power source, and start exploring what you can teach Alto to recognise. If you need a bit of inspiration to get going, take a look at the Experimenting with Alto section below.~~

![dashcam standing flat](images/alto-readme-13.png)
<br>
<br>
## [Experiment with Alto](4.0-experiments-with-alto.md)

Alto is a great way to understand the basics of machine learning. This section contains a number of experiments to help understand how Alto works, and introduce the basics of machine learning to others.

Covering aspects from simple object recognition, to introducing k-nearest neighbor (kNN) algorithms, these experiments give practical ways to bring the concepts behind Alto to life. Head to the [Experiments with Alto](4.0-experiments-with-alto.md) page to read on.

![alto pointed at a red apple](images/alto-readme-14.png)
<br>
<br>
## [Remixing Alto for your projects](5.0-remixing-alto.md)

All the hardware and software for Alto was created with hacking and remixing in mind: the case design can be made from different materials, or refactored entirely; the electronics can be adapted to use whatever components you have available; the servos can be substituted for any type of actuator; and the software is written in a high level language (Python) that is easy to modify. 

Here are just some of the ways you can hack your own Alto:

![different alto form factors](images/alto-readme-15.gif)
<br>
<br>
### Hacking the [software](5.0-remixing-alto.md#hacking-altos-software)
~~Small tweaks to the existing code can be made to change Alto’s confidence level or behaviours.~~

![changing alto's code](images/alto-readme-16.gif)
<br>
<br>
### Hacking the [hardware](5.0-remixing-alto.md#hacking-altos-hardware)

~~Go beyond servos, to explore new ways for Alto to show its recognised something.~~

![alto with LED confidence meter](images/alto-readme-17.gif)
<br>
<br>
### Hacking the [casing](5.0-remixing-alto.md#hacking-altos-casing)

~~The casing for Alto can easily be changed to fit whatever application you might have in mind. Whether that’s simple aesthetic changes to modify Alto’s look, or changes to the design of the arms or body that might let Alto do new things.~~ 





### OS & compute

The Raspberry Pi Zero runs Raspberry Pi OS. It is responsible for interfacing with the user’s connected hardware (connected via GPIO, USB or ribben cable).

### Software

~~The Alto software application is written in Python and bash (via scripts). It receives input from the Raspberry Pi camera module, prepares it for for storage organized via date/time. For the more technical part, I have put some code that is good starter for those looking to send files to their personal cloud or storage device once they are in proximity to wireless connection.
When Alto is learning, it calculates the embedding of the incoming data from the image sensor in its model and assigns it a label - in the case of Alto, this label is either its left or right arm. When Alto is in recognition mode, the embeddings of data frames from the image sensor are determined and their proximity to other known embeddings is calculated; if these are within a certain distance of a labelled embedding, then Alto has recognised something, and will point at it with its corresponding arm.~~
<br>
<br>

### Electronics

The electronics for the pi dash are designed to be as flexible and hackable as possible. It is based around a single through-hole prototyping board which can be assembled easily by hand. This board connects to the GPIO or via micro usb to a charger that outputs steady voltage/current to ensure your rpi doesn't break or slow down in recording.

~~You can find more information about the electronics in the [electronics](2.0-Build-the-electronics.md) directory, and the bill of materials is available [here](electronics/alto-bom.xlsx) as a downloadable spreadsheet.<br>~~
<br>


