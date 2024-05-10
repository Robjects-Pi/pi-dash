# Compare this snippet from software/Raspbian_picamera/record-10-secs/lib.py:
# with the snippet below. The picamera2 library is more concise and easier to use.
# The picamera2 library is a wrapper around the picamera library. It provides a more
# user-friendly interface to the picamera library. The picamera2 library is a good
# alternative to the picamera library for beginners and experienced users.



from picamera2.encoders import H264Encoder
from picamera2 import Picamera2
import time
from picamera2 import Quality
from time import sleep

picam2=Picamera2()
video_config=picam2.create_video_configuration()
picam2.configure(video_config)
encoder=H264Encoder(bitrate=10000000)

# set the output file name
output="test.h264"
# set the video directory
video_dir="/home/pi/videos"
# set the video file path
video_path=f"{video_dir}/{output}"  # /home/pi/videos/test.h264
# start recording

picam2.start_recording(encoder,'test.h264',quality=Quality.HIGH)
sleep(10)
picam2.stop_recording()


