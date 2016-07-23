#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

gpoList = [27]

for i in gpoList:
	GPIO.setup(i, GPIO.OUT)
	#GPIO.output(i, GPIO.HIGH)

try:
	GPIO.output(27, GPIO.LOW)
	print "Pin 27 On IN2"

except KeyboardInterrupt:
	print "Saliendo ..."
	GPIO.cleanup()

