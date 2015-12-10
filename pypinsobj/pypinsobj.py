#!/usr/bin/env python

import RPi.GPIO as GPIO
import os, sys
from ast import literal_eval

RESERVED = -1
IN = GPIO.IN
OUT = GPIO.OUT
RISING = GPIO.RISING
FALLING = GPIO.FALLING
BOTH = GPIO.BOTH
BCM = GPIO.BCM
BOARD = GPIO.BOARD

class Pins(object):

    class PinNameError(Exception):
        pass

    def __init__(self, mode=GPIO.BCM, fromfile=None):
        self.pins = []
        if fromfile:
            if not os.path.isfile(filename):
                sys.exit("File not found: {}").format(filename)
            with open(filename, mode='r') as f:

                """ format is
                {'mode':GPIO.BM,
                 'pins': [
                            {'name':'test_led',
                             'pin' : 23,
                             'state': IN
                            },
                         ]
                """
                x = f.read()
                raw = literal_eval(x)
                mode = raw['mode']
                self.pins = raw['pins']
                GPIO.setmode(mode)
                self.__setup()
        else:
            GPIO.setmode(mode)
            #GPIO.setmode(GPIO.BOARD)

    def delist(self,x):
        if x and len(x) == 1:
            return x[0]
        else:
            return x

    def add(self,pin, name, state, comment=None):
        if name in [p['name'] for p in self.pins]:
            raise PinNameError('name {} already taken'.format(name))
        if pin in [p['pin'] for p in self.pins]:
            raise PinNameError('pin number {} already assigned to ' \
                               .format(name,
                                       next(p['name'] for p in pins \
                                              if p[pin] == pin)))
        else:
            self.pins.append({'pin':pin, 'name':name, 'state':state, 'comment':comment})
            if state in [IN, OUT]:
                GPIO.setup(pin, state)

    def get(self,name):
        return self.delist( [ p for p in self.pins if p['name'] == name ] )

    def getp(self, name):
        return self.get(name)['pin']

    def __setup(self):
        for p in pins:
            if p['state'] in [IN, OUT]:
                GPIO.setup(p['pin'], p['state'])

    def get_comment(self, name):
        return self.get(name)['comment']

    def input(self, name):
        return GPIO.input(self.getp(name))

    def output(self, name, value):
        GPIO.output(self.getp(name), value)

    def turn_on(self, name):
        GPIO.output(self.getp(name), 1)

    def turn_off(self, name):
        GPIO.output(self.getp(name), 0)

    def wait_event(self, name, direction, callback, bouncetime=None):
        if direction in [RISING, FALLING, BOTH]:
            GPIO.add_event_detect(p.getp(name),
                                  direction,
                                  callback=callback,
                                  bouncetime=bouncetime
                                  )





