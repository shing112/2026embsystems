from picamera2 import Picamera2 
import cv2 
import numpy as np 

picam2 = Picamera2() 
picam2.configure(picam2.create_preview_configuration(main={'format':'RGB888', 'size':(320, 240)})) 
picam2.start() 
 
while True: 
	frame = picam2.capture_array() 
	hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV) 

	lower_purple = np.array([145, 100, 100]) 
	upper_purple = np.array([165, 255, 255]) 
	mask = cv2.inRange(hsv, lower_purple, upper_purple)

	purple_only = cv2.bitwise_and(frame, frame, mask=mask) 

	cv2.imshow('Original', frame) 
	cv2.imshow('Mask', mask) 
	cv2.imshow('Result', purple_only) 

	if cv2.waitKey(1) & 0xFF == ord('q'): 
		break

picam2.stop() 
cv2.destroyAllWindows() 
