#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import datetime


def detect():
    while True:
        if GPIO.input(12) == True:
            print(str(datetime.datetime.now()) + "    Somebody is closing.")
        else:
            print(str(datetime.datetime.now()) + "    Nobody.")
        time.sleep(1)


def motion_detect():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.IN)
    motion = GPIO.input(12)
    GPIO.cleanup()
    return motion

if __name__ == "__main__":
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.IN)
    detect()
    GPIO.cleanup()
