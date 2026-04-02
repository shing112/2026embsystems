from picamera2 import Picamera2, Preview
from time import sleep

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)
picam2.start()
sleep(2)

picam2.capture_file('/home/pi30307/Desktop/first.jpg') #이미지 파일로 저장

sleep(3)

picam2.close()
