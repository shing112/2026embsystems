from picamera2 import Picamera2, Preview
from time import sleep
import cv2 

picam2 = Picamera2()
picam2.preview_configuration.size=(800, 600)
picam2.start(show_preview=True)
sleep(2)

picam2.capture_file('../Desktop/toProcess.jpg')
picam2.close()

img = cv2.imread('../Desktop/toProcess.jpg')
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('../Desktop/grayscaleImage.jpg', grayscale)
