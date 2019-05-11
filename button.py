#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

from signal import pause
from gpiozero import Button, LED, PWMLED

GPIO_RELAY      = 17
GPIO_BUTTON     = 18
GPIO_BUTTON_LED = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(GPIO_RELAY, GPIO.OUT)

led = PWMLED(GPIO_BUTTON_LED)
button = Button(GPIO_BUTTON)
relay = LED(GPIO_RELAY)

input_pressed = False
time_pressed = 0.0

def CapturePhoto(l, r):
    def f():
        l.pulse(0.2, 0.6)
        time.sleep(3.0)
        l.pulse(0.1, 0.3)
        time.sleep(2.0)
        for x in range(0,3):
            r.on()
            time.sleep(0.2)
            r.off()
            time.sleep(0.4)
        r.off()
        l.off()
        time.sleep(0.5)
        l.pulse(1, 3)
        time.sleep(12.0)
        l.pulse(0.4, 1.2)
    return f

def LedPulse():
    led.off()
    time.sleep(0.150)
    led.pulse(1.0, 1.33)

def LedBlink():
    led.blink(0.33,0.33)
    relay.toggle()

button.when_pressed = CapturePhoto(led, relay)
button.when_released = LedPulse
button.when_held = LedBlink

while True:
    button.wait_for_press()
    print("Button pressed")
    pause()

#while True:
#    input_state = GPIO.input(18)
#    if input_state == False:
#        if not input_pressed:
#            time_pressed = time.time()
#            print('Button Pressed')
#            led.on()
#            time.sleep(0.8)
#            led.pulse()
#        input_pressed = True
#        GPIO.output(17, True)
#    else:
#        if input_pressed:
#            time_str = "{:.3f}s".format(time.time() - time_pressed)
#            print('Button Released (%s)' % time_str)
#            led.off()
#            time.sleep(0.9)
#            led.pulse()
#        input_pressed = False
#        GPIO.output(17, False)
#    time.sleep(0.01)
