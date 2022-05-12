import RPi.GPIO as GPIO
import time

motors = [13,19,26,12,23,24]
r_enable = 12
r_for = 24
r_rev = 23
l_enable = 13
l_for = 19
l_rev = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(motors, GPIO.OUT)
GPIO.output(motors, GPIO.LOW)

GPIO.output(r_enable, 1)
GPIO.output(l_enable, 1)

def drive_motor(pin):
    print(pin)
    GPIO.output(pin, 1)
    time.sleep(1)
    GPIO.output(pin, 0)
    time.sleep(0.5)
    
drive_motor(r_for)
drive_motor(r_rev)
drive_motor(l_for)
drive_motor(l_rev)

GPIO.cleanup()