import RPi.GPIO as GPIO
import time

class RGB:
    '''
        This code is a template for 4-pin RGB LED with common anode.
        Please revised the code if using REB LED with common cathode!
    '''
    def __init__(self, mode, red_pin, green_pin, blue_pin, pwm_freq, debug=False):
        self.mode       =   mode
        self.red_pin    =   red_pin
        self.green_pin  =   green_pin
        self.blue_pin   =   blue_pin
        self.pwm_freq   =   pwm_freq

        try: 
            GPIO.setmode(self.mode)
            GPIO.setup(self.red_pin, GPIO.OUT)
            GPIO.setup(self.green_pin, GPIO.OUT)
            GPIO.setup(self.blue_pin, GPIO.OUT)
            if debug:
                GPIO.setwarnings(True)
            else:
                GPIO.setwarnings(False)

            self.r_pwm = GPIO.PWM(self.red_pin, self.pwm_freq)
            self.g_pwm = GPIO.PWM(self.green_pin, self.pwm_freq)
            self.b_pwm = GPIO.PWM(self.blue_pin, self.pwm_freq)

        except Exception as e:
            print("GPIO initial encounters error: ")
            print(e)

    def setup(self):
        # common cathode set 0, common anode set 100 to turn off the led
        self.r_pwm.start(100)
        self.g_pwm.start(100)
        self.b_pwm.start(100)

    def setColor(self, r, g, b):
        self.r_pwm.ChangeDutyCycle(100-int(r/255*100))
        self.g_pwm.ChangeDutyCycle(100-int(g/255*100))
        self.b_pwm.ChangeDutyCycle(100-int(b/255*100))

    def close(self):
        self.r_pwm.stop()
        self.g_pwm.stop()
        self.b_pwm.stop()
        GPIO.cleanup()

def test_led(rainbow = False):
    R_PIN = 8
    G_PIN = 10
    B_PIN = 12
    PWM_FREQ = 300

    try:
        my_led = RGB(GPIO.BOARD, R_PIN, G_PIN, B_PIN, PWM_FREQ)
        my_led.setup()
        time.sleep(1)

        my_led.setColor(255, 0, 0)      # Red
        time.sleep(1)

        my_led.setColor(0, 255, 0)      # Green
        time.sleep(1)

        my_led.setColor(0, 0, 255)      # Blue
        time.sleep(1)

        my_led.setColor(0, 0, 0)        # Off
        time.sleep(1)

        my_led.setColor(255, 255, 255)  # White
        time.sleep(1)

        # Show rainbow loop
        color   =   0
        while(rainbow):
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

        my_led.close()                  # Turn off the led

    except KeyboardInterrupt:
        print("Quit.")

    finally:
        my_led.close()

if __name__ == '__main__':
    test_led(True)