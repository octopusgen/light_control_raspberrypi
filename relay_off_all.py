#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

gpioList = [4, 27]

for i in gpioList:
	GPIO.setup(i, GPIO.OUT)
	#GPIO.output(i, GPIO.HIGH)

try:
	GPIO.output(27, GPIO.HIGH)
	print "Gpio 27 OFF in2. "
	GPIO.output(4, GPIO.HIGH)
	print "Gpio 4 OFF in1. "

except KeyboardInterrupt:
	print "Saliendo ..."
	GPIO.cleanup()

