from picamera2 import Picamera2, Preview
from time import sleep

picam2 = Picamera2()

picam2.start_and_capture_file('first.jpg') #이미지 파일로 저장

picam2.close()
