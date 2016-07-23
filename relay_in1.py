#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
# GPioPort numero 4
gpioList = [4]

for i in gpioList:
	GPIO.setup(i, GPIO.OUT)
	#GPIO.output(i, GPIO.HIGH)

try:
	GPIO.output(4, GPIO.LOW)
	print "Port GPIO4 On IN1"

except KeyboardInterrupt:
	print "Saliendo ..."
	GPIO.cleanup()

