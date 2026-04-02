from picamera2 import Picamera2, Preview
from time import sleep

picam2 = Picamera2()
picam2.preview_configuration.size=(2592, 1944)
picam2.start(show_preview=True)
sleep(2)

picam2.capture_file('../Desktop/max.jpg')
picam2.close()
