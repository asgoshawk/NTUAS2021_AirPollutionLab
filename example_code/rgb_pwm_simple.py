import RPi.GPIO as GPIO
import time

R_PIN = 8
G_PIN = 10
B_PIN = 12
PWM_FREQ = 300

GPIO.setmode(GPIO.BOARD)
GPIO.setup(R_PIN, GPIO.OUT)
GPIO.setup(G_PIN, GPIO.OUT)
GPIO.setup(B_PIN, GPIO.OUT)
GPIO.setwarnings(False)

r_pwm = GPIO.PWM(R_PIN, PWM_FREQ)
g_pwm = GPIO.PWM(G_PIN, PWM_FREQ)
b_pwm = GPIO.PWM(B_PIN, PWM_FREQ)

r_pwm.start(100)
g_pwm.start(100)
b_pwm.start(100)
time.sleep(1)

def setColor(r, g, b):
    r_pwm.ChangeDutyCycle(100-int(r/255*100))
    g_pwm.ChangeDutyCycle(100-int(g/255*100))
    b_pwm.ChangeDutyCycle(100-int(b/255*100))

print("Show Red")
setColor(255, 0, 0)
time.sleep(1)

print("Exiting...")
r_pwm.stop()
g_pwm.stop()
b_pwm.stop()
GPIO.cleanup()