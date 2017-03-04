#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from smartclock import GUI, DHT11
from time import sleep
import signal


# Setup RPI
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
running = False


def stop(signum=None, frame=None):
    global running
    running = False


try:
    signal.signal(signal.SIGTERM, stop)
    running = True
    gui = GUI()
    dht11 = DHT11()

    while running:
        hum, c, f = dht11.read()
        gui.render_string("Humidity: {0}, Temperature: {1}F".format(hum, f))
        sleep(0.1)

    print("Cleaning up GPIO")
    GPIO.cleanup()
    print("Exiting...")
except KeyboardInterrupt:
    stop()
