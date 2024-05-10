# Camera Module on Bullseye and Bookworm
With bullseye and bookworm, the camera module is enabled by default. You can use the camera module without having to enable it in the raspi-config tool.

>Note:
Keep in mind that the camera is not supported on bullseye if you disable the camera interface in the raspi-config tool.
If you disable the camera interface, you will need to re-enable it to use the camera scripts and files in this directory

## List of scripts:
- `record.py`: This script records videos using the camera module. The script starts recording videos when it is run and saves the video files in the `videos` directory. The script runs until you stop it by pressing `Ctrl+C`.
- `record.service`: This script is a systemd service that starts the `record.py` script on boot. The service is configured to start the `record.py` script when the Raspberry Pi Zero boots up, so you can start recording videos automatically when the Raspberry Pi Zero starts up.
- `take_picture.py`: This script takes a picture using the camera module. The script takes a picture when it is run and saves the picture file in the `pictures` directory.
- `take_picture.service`: This script is a systemd service that starts the `take_picture.py` script on boot. The service is configured to start the `take_picture.py` script when the Raspberry Pi Zero boots up, so you can take pictures automatically when the Raspberry Pi Zero starts up.
- `timelapse.py`: This script takes a picture every 10 seconds using the camera module. The script takes a picture every 10 seconds when it is run and saves the picture files in the `timelapse` directory.
- `timelapse.service`: This script is a systemd service that starts the `timelapse.py` script on boot. The service is configured to start the `timelapse.py` script when the Raspberry Pi Zero boots up, so you can take pictures automatically every 10 seconds when the Raspberry Pi Zero starts up.
- `stream.py`: This script streams video using the camera module. The script streams video when it is run and displays the video feed on the screen. The script runs until you stop it by pressing `Ctrl+C`.
- `stream.service`: This script is a systemd service that starts the `stream.py` script on boot. The service is configured to start the `stream.py` script when the Raspberry Pi Zero boots up, so you can stream video automatically when the Raspberry Pi Zero starts up.

 The script uses the `picamera2` library to interface with the camera module.
For more information on the picamera2 library, check out the [GitHub](https://github.com/raspberrypi/picamera2) or see the [picamera2 documentation](https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf) for more information.