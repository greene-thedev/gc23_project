from gpiozero import LED, Button
from signal import pause
from time import sleep
# from Adafruit_ADS1x15 import ADS1x15

button = Button(2)
flame_detector = ADS1x15()

red = LED(15)
yellow = LED(24)
green = LED(18)

while True:
    green.on()
    if flame_detector:
        green.off()
        yellow.on()
        sleep(2)
        yellow.off()
        while True:
            red.on()
            sleep(0.1)
            red.off()
            sleep(0.1)
            if button.is_held:
                break







pause()