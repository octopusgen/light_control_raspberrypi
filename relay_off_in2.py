#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

gpioList = [27]

for i in gpioList:
	GPIO.setup(i, GPIO.OUT)
	#GPIO.output(i, GPIO.HIGH)

try:
	GPIO.output(27, GPIO.HIGH)
	print "GPIO27 OFF in2"

except KeyboardInterrupt:
	print "Saliendo ..."
	GPIO.cleanup()

