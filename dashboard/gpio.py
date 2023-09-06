from gpiozero import LED, Button, Buzzer
from signal import pause
from time import sleep
import requests
# from Adafruit_ADS1x15 import ADS1x15

def disengage():
    engage()


def engage():
    button = Button(2)
    buzzer = Buzzer(3)
    # flame_detector = ADS1x15()
    red = LED(15)
    yellow = LED(24)
    green = LED(18)

    def get_url():
        url = "https://maker.ifttt.com/trigger/notification/json/with/key/lxi_09_iTWs-6l0Avj5SsFUOk0X7GuK3mHeVKH_9GbT"
        r = requests.get(url)
        print(r)

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
        
    get_url()

    while True:
        buzzer.on()
        sleep(0.05)
        buzzer.off()
        red.on()
        sleep(0.1)
        red.off()
        button._hold_time = 5
        if button.is_held:
            break

    pause()
