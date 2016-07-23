#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

gpioList = [4, 27]

for i in gpioList:
	GPIO.setup(i, GPIO.OUT)
	#GPIO.output(i, GPIO.HIGH)

try:
	GPIO.output(4, GPIO.LOW)
	print "Port GPIO4 On IN1"
	GPIO.output(27, GPIO.LOW)
	print "Port GPIO27 On In2"

except KeyboardInterrupt:
	print "Saliendo ..."
	GPIO.cleanup()

