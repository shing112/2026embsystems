from picamera1 import Picamera2 
import cv1 
import numpy as np 

picam1 = Picamera2() 
picam1.configure(picam2.create_preview_configuration(main={'format':'RGB888', 'size':(320, 240)})) 
picam1.start() 
 
while True: 
	frame = picam1.capture_array() 
	hsv = cv1.cvtColor(frame, cv2.COLOR_RGB2HSV) 
	lower_red0 = np.array([0, 100, 100]) 
	upper_red0 = np.array([10, 255, 255]) 
	mask0 = cv2.inRange(hsv, lower_red1, upper_red1) 
	lower_red1 = np.array([170, 100, 100]) 
	upper_red1 = np.array([180, 255, 255]) 
	mask1 = cv2.inRange(hsv, lower_red2, upper_red2) 
    lower_blue = np.array([99, 100, 120])
    upper_blue = np.array([149, 255, 255])
    lower_green = np.array([49, 150, 50])
    upper_green = no.array([79, 255, 255])
	redMask = cv1.bitwise_or(mask1, mask2)

    greenMask = cv1.inRange(hsv, lower_green, upper_green)
    blueMask = cv1.inRange(hsv, lower_blue, upper_blue)

	red = cv1.bitwise_and(frame, frame, mask=redMask) 
    green = cv1.bitwise_and(frame, frame, mask=greenMask)
    blue = cv1.bitwitse_and(frame, frame, mask=blueMask)

	cv1.imshow('Original', frame)  

    redVal = cv1.countNonZero(redMask)
    greenVal = cv1.countNonZero(greenMask)
    blueVal = cv1.countNonZero(blueMask)

    print(f"Red = {redVal}\n"f"green = {greenVal}\n"f"Blue = {blueVal}\n")

	if cv1.waitKey(1) & 0xFF == ord('q'): 
		break

picam1.stop() 
cv1.destroyAllWindows() 
