from flask import Flask, render_template, request, redirect, jsonify
from gpiozero import LED, Button, Buzzer
from signal import pause
from time import sleep
import requests
from alertSystem import sendSMS


app = Flask(__name__)
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
flame_values: int = 0

@app.route("/", methods = ["GET", "POST"])
def index():

        
    return render_template("index.html")

@app.route("/engage", methods = ["POST"])
def eng():
    greenLightOn()
    return render_template("engage.html")


@app.route("/disengage", methods = ["POST"])
def deng():
    return redirect("/")

@app.route('/flame-sensor', methods=['POST'])
def receive_flame_sensor_value():
    data = request.json
    print(f"Received flame sensor value: {data}")
    flame_values = data["flameValue"]
    
    if(float(flame_values) == 1):
        led_state = green.is_active
        if led_state == True:
            alert()
            danger = True
            return redirect("engage.html", danger=danger)
        
    return jsonify({'message': 'Flame sensor value received'}), 200


def get_url():
    url = "https://maker.ifttt.com/trigger/notification/json/with/key/lxi_09_iTWs-6l0Avj5SsFUOk0X7GuK3mHeVKH_9GbT"
    r = requests.get(url)
    print(r)

  
    
def greenLightOn():
    green.on()
    
def greenLightOff():
    green.off()
    
def alert():
            get_url()
            sendSMS()
            for i in range(0,5):
                buzzer.on()
                sleep(1)
                buzzer.off()
                yellow.on()
                sleep(1)
                yellow.off()
        
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
           
    


if __name__ == '__main__':
    app.run(debug=True, host='192.168.4.1', port=5000)
    
