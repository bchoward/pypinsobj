# pypinsobj

Hardwiring pin numbers into raspberry pi code makes it difficult to combine projects,
and makes adapting or changing difficult and prone to bugs.  This interface isolates
the pin definitions, allowing you to refer to the pins by name.


*Usage:*
```
from pypinsobj import *

p = pins.Pins()        #defaults to BCM mode, or use p = Pins(mode=BOARD)
p.add(23, 'temp_sensor', IN)
p.add(24, 'doorbell', IN)
p.add(22, 'test_LED', OUT)
p.add(25, 'latch', OUT)
p.add(1, 'vcc', RESERVED, 'connected to positive 3v')
p.add(9, 'MISO', RESERVED, 'used for MISO SPI')

...

if p.input('temp_sensor'):
       p.turn_on('test_LED')


def doorbell_cb(pin):
    if pin == p.getp('doorbell'):
        p.turn_on('latch')
        sleep(2)
        p.turn_off('latch')

wait_event('doorbell', RISING, callback=doorbell_cb, bouncetime=200)

GPIO.cleanup()
```
