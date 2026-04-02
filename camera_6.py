from picamera2 import Picamera2, Preview
from time import sleep

picam2 = Picamera2()
picam2.preview_configuration.size=(320, 240)
picam2.configure('preview')
picam2.start(show_preview=True)
sleep(2)

picam2.capture_file('../Desktop/min.jpg')
picam2.close()
