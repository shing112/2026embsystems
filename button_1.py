from gpiozero import Button

button = Button(2) #pull_up=True
try:
    while True:
        if button.is_pressed:
            print("Button is pressed")
        else :
            print("Buton is not pressed")
except KeyboardInterrupt:
    pass
