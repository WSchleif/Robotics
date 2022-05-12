import RPi.GPIO as GPIO
import time

motors = [13,19,26,12,23,24]
r_enable = 12
r_for = 24
r_rev = 23
r_speed = 99
l_enable = 13
l_for = 19
l_rev = 26
l_speed = 87

GPIO.setmode(GPIO.BCM)
GPIO.setup(motors, GPIO.OUT)
GPIO.output(motors, GPIO.LOW)

l_pwm = GPIO.PWM(l_enable, 1000)
l_pwm.start(l_speed)
r_pwm = GPIO.PWM(r_enable, 1000)
r_pwm.start(r_speed)

def drive_motor(pin1, pin2, state):
    GPIO.output(pin1, state)
    GPIO.output(pin2, state)
    time.sleep(2)
    
drive_motor(r_for, l_for, 1)
drive_motor(r_for, l_for, 0)
drive_motor(r_rev, l_rev, 1)
drive_motor(r_rev, l_rev, 0)

GPIO.cleanup()