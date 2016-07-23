#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

gpioList = [4]

for i in gpioList:
	GPIO.setup(i, GPIO.OUT)
	#GPIO.output(i, GPIO.HIGH)

try:
	GPIO.output(4, GPIO.HIGH)
	print "GPIO4 OFF in1."

except KeyboardInterrupt:
	print "Saliendo ..."
	GPIO.cleanup()

