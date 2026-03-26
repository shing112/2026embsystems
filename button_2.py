from gpiozero import Button
from gpiozero import LED
from time import sleep

button = Button(2) #pull_up=True
led = LED(17)
try:
    while True:
        if button.is_pressed:
            print("button is pressed")
            led.on()
            sleep(0.1)
        else :
            print("Buton is not pressed")
            led.off()
            sleep(0.1)
except KeyboardInterrupt:
    pass
