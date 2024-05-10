import os
import picamera
import datetime
import configparser

class Camera:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.resolution = tuple(map(int, config['camera']['resolution'].split(',')))
        self.location = config['camera']['location']
        self.framerate = int(config['camera']['framerate'])
        self.camera = picamera.PiCamera()

    def start_recording(self):
        if not os.path.exists(self.location):
            os.makedirs(self.location)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
        filepath = os.path.join(self.location, f"{timestamp}.h264")
        self.camera.resolution = self.resolution
        self.camera.framerate = self.framerate
        self.camera.start_recording(filepath)

    def stop_recording(self):
        self.camera.stop_recording()