#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

from signal import pause
from gpiozero import LED
from gpiozero import PWMLED

led = PWMLED(27)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN,   pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT)

input_pressed = False
time_pressed = 0.0

led.pulse()

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        if not input_pressed:
            time_pressed = time.time()
            print('Button Pressed')
            led.on()
            time.sleep(0.8)
            led.pulse()
        input_pressed = True
        GPIO.output(17, True)
    else:
        if input_pressed:
            time_str = "{:.3f}s".format(time.time() - time_pressed)
            print('Button Released (%s)' % time_str)
            led.off()
            time.sleep(0.9)
            led.pulse()
        input_pressed = False
        GPIO.output(17, False)
    time.sleep(0.01)
