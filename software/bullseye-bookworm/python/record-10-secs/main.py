from lib import Camera
import time
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
duration = config['camera']['duration']

# Record and stop after 10 seconds
camera = Camera()
camera.start_recording()
print("Recording")
time.sleep(duration)
print("Done Recording")
camera.stop_recording()
