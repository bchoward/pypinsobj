#!/usr/bin/env python

import RPi.GPIO as GPIO
from RPi.GPIO import (
    IN,
    OUT,
)

class Pins(object):

    class PinNameError(Exception):
	pass

    def __init__(self, mode=GPIO.BCM):
	self.pins = []
	GPIO.setmode(mode)
	#GPIO.setmode(GPIO.BOARD)
	
    def delist(self,x):
	if x and len(x) == 1:
	    return x[0]
	else:
	    return x
    
    def add(self,pin, name, state):
	if name in [p['name'] for p in self.pins]:
	    raise PinNameError('name {} already taken'.format(name))
	else:
	    self.pins.append({'pin':pin, 'name':name, 'state':state})
	    GPIO.setup(pin, state)

    def get(self,name):
	return self.delist( [ p for p in self.pins if p['name'] == name ] )

    # not safe if 2+ pins have same name
    def getp(self, name):
	return self.get(name)['pin']

    def setup(self):
	for p in pins:
	    GPIO.setup(p['pin'], p['state'])
	
    def input(self, name):
	return GPIO.input(self.getp(name))

    def output(self, name, value):
	GPIO.output(self.getp(name), value)
	

    """
    pins = Pins()
    pins.add(23, 'doorbell_input', IN)
    pins.add(22, 'test_led', OUT)
    pins.setup()
    """
