from flask import Flask

import time
import RPi.GPIO as GPIO
import rgb_pwm

R_PIN = 8
G_PIN = 10
B_PIN = 12
PWM_FREQ = 300
my_led = rgb_pwm.RGB(GPIO.BOARD, R_PIN, G_PIN, B_PIN, PWM_FREQ)
my_led.setup()
time.sleep(1)

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/Red")
def call_Red():
    my_led.setColor(255, 0, 0)      # Red
    return "It's Red!"

@app.route("/Green")
def call_Green():
    my_led.setColor(0, 255, 0)      # Green
    return "It's Green!"

@app.route("/Blue")
def call_Blue():
    my_led.setColor(0, 0, 255)      # Blue
    return "It's Blue!"

@app.route("/Close")
def close_LED():
    my_led.setColor(0, 0, 0)        # Close
    return "LED is closed!"    

@app.route("/Demo/<int:times>")
def demo_RGB():
    if times < 0:
        times = 0
    color   =   0
    count   =   0
    while(True and count < times):
        if color <= 255:
            R = 255 - color
            G = color
            B = 0
        elif color <= 511:
            R = 0
            G = 255 - (color - 256)
            B = (color - 256)
        else:
            R = color - 512
            G = 0
            B = 255 - (color - 512)

        my_led.setColor(R, G, B)
        time.sleep(0.005)
        color += 1

        if color > 767:
            color = 0
            count += 1
    my_led.setColor(0, 0, 0)
    return "Demo"

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("Quit.")
    finally:
        my_led.close()