#!/usr/bin/python3
""" Example of the game of life 8x8 LED matrix dispplay class """

from threading import Lock

from Adafruit_Python_LED_Backpack.Adafruit_LED_Backpack import BicolorMatrix8x8

import led8x8life

if __name__ == '__main__':
    LOCK = Lock()
    DISPLAY = BicolorMatrix8x8.BicolorMatrix8x8()
    DISPLAY.begin()
    LIFE = led8x8life.Led8x8Life(DISPLAY, LOCK)
    LIFE.reset()
    while True:
    	LIFE.display()

