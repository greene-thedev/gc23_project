from gpiozero import LED, Button
from signal import pause
from time import sleep
# from Adafruit_ADS1x15 import ADS1x15



red = LED(15)
yellow = LED(24)
green = LED(18)

green.on()
yellow.on()
red.on()



pause()