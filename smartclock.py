#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from Adafruit_DHT import DHT11, read
from time import sleep
import signal
import sdl2
import sdl2.ext


# Setup RPI
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
running = False

# Setup GUI
sdl2.ext.init()
window = sdl2.ext.Window("Sensor", size=(1920, 1080), flags=sdl2.SDL_WINDOW_FULLSCREEN)
window.show()
font_manager = sdl2.ext.FontManager(font_path='fonts/OpenSans-Regular.ttf', size=90)
renderer = sdl2.ext.Renderer(window)
factory = sdl2.ext.SpriteFactory(renderer=renderer)
sdl2.SDL_ShowCursor(0)


def c_to_f(temp):
    return temp * 9.0 / 5.0 + 32


def stop(signum=None, frame=None):
    global running
    running = False


def render(output):
    global renderer
    global factory

    renderer.clear(sdl2.ext.Color(0, 0, 0))
    text = factory.from_text(output, fontmanager=font_manager)
    renderer.copy(text, dstrect=(0, 0, text.size[0], text.size[1]))
    renderer.present()


try:
    signal.signal(signal.SIGTERM, stop)
    running = True
    while running:
        sleep(2.1)
        hum, temp = read(DHT11, 4)
        if hum and temp:
            data = "Humidity: {0}%, Temperature: {1}F".format(hum, c_to_f(temp))
            render(data)
    print("Cleaning up GPIO")
    GPIO.cleanup()
    print("Exiting...")
except KeyboardInterrupt:
    stop()
