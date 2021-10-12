import time

import Adafruit_ADS1x15
import RPi.GPIO as GPIO
import rgb_pwm

adc = Adafruit_ADS1x15.ADS1115()

print('Reading ADS1x15 values, press Ctrl-C to quit...')

R_PIN = 8
G_PIN = 10
B_PIN = 12
PWM_FREQ = 300
my_led = rgb_pwm.RGB(GPIO.BOARD, R_PIN, G_PIN, B_PIN, PWM_FREQ)
my_led.setup()
my_led.setColor(0, 0, 0)
time.sleep(1)

GAIN = 1
upperlim = 25000
lowerlim = 1000

def rgb_with_vr():
    while True:
        value = adc.read_adc(2, gain=GAIN)

        if value <= lowerlim:
            color = 0
        elif value >= upperlim:
            color = 767
        else:
            color = int((value - lowerlim)/(upperlim - lowerlim)*767)

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
        print("\rThe ADC readout is %5d. The color is rgb(%3d,%3d,%3d)." %(value, R,G,B), end="")
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        rgb_with_vr()
    except KeyboardInterrupt:
        print("\nQuit.")
    finally:
        my_led.close()