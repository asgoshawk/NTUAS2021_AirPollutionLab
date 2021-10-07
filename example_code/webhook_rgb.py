from flask import Flask, request, jsonify

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

@app.route("/webhook", methods=['POST'])
def control_led():
    case = request.get_json(silent=True)

    if case['queryResult']['queryText'] == 'blue':
        my_led.setColor(0, 0, 255)      # Blue
        reply = {
            "fulfillmentText": "Ok. The led is turn to blue.",
        }
        return jsonify(reply)

    elif case['queryResult']['queryText'] == 'red':
        my_led.setColor(255, 0, 0)      # Red
        reply = {
            "fulfillmentText": "Ok. The led is turn to red.",
        }
        return jsonify(reply)

    elif case['queryResult']['queryText'] == 'green':
        my_led.setColor(0, 255, 0)      # Green
        reply = {
            "fulfillmentText": "Ok. The led is turn to green.",
        }
        return jsonify(reply)

    elif case['queryResult']['queryText'] == 'off':
        my_led.setColor(0, 0, 0)      # close
        reply = {
            "fulfillmentText": "Ok. The led is close now.",
        }
        return jsonify(reply)

    elif case['queryResult']['queryText'] == 'party':
        color   =   0
        count   =   0
        while(True and count < 1):
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
        reply = {
            "fulfillmentText": "The party just done.",
        }
        return jsonify(reply)

    else:
        reply = {
            "fulfillmentText": "Please try again.",
        }
        return jsonify(reply)

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("Quit.")
    finally:
        my_led.close()
