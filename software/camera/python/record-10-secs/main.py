from lib import Camera
import time


# Record and stop after 10 seconds
camera = Camera()
camera.start_recording()
print("Recording")
time.sleep(10)
print("Done Recording")
camera.stop_recording()
