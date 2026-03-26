from gpiozero import Button
from gpiozero import LED
from time import sleep

button1 = Button(2) #pull_up=True
button2 = Button(3) #pull_up=True
led1 = LED(17)
led2 = LED(27)
led3 = LED(22)

try :
    while True:
        if button1.is_pressed:
            print("button1 is pressed")
            led1.on()
            led2.off()
            led3.off()
            sleep(0.5)
            led1.off()
            led2.on()
            led3.off()
            sleep(0.5)
            led1.off()
            led2.off()
            led3.on()
            sleep(0.5)
            led1.off()
            led2.off()
            led3.off()
            sleep(0.5)
        elif button2.is_pressed:
            print("Button2 is pressed")
            led1.off()
            led2.off()
            led3.on()
            sleep(0.5)
            led1.off()
            led2.on()
            led3.off()
            sleep(0.5)
            led1.on()
            led2.off()
            led3.off()
            sleep(0.5)
            led1.off()
            led2.off()
            led3.off()
            sleep(0.5)
except KeyboardInterrupt:
    pass
