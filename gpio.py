from gpiozero import LED, Button, Buzzer
from signal import pause
from time import sleep
# from Adafruit_ADS1x15 import ADS1x15

button = Button(2)
buzzer = Buzzer(3)
# flame_detector = ADS1x15()

red = LED(15)
yellow = LED(24)
green = LED(18)

# while True:
#     green.on()
#     if flame_detector:

green.off()
for i in range(0,5):
    buzzer.on()
    sleep(1)
    buzzer.off()
    yellow.on()
    sleep(1)
    yellow.off()
    

while True:
    buzzer.on()
    # buzzer.blink
    sleep(0.05)
    buzzer.off()
    red.on()
    sleep(0.1)
    red.off()
    button._hold_time = 5
    if button.is_held:
        break
  
     
        

pause()