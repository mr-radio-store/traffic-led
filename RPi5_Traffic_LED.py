from gpiozero import LED
from gpiozero.pins.lgpio import LGPIOFactory
from time import sleep

# | LED Color | GPIO Pin | Pin number (BCM / Physical) | Notes                    |
# | --------- | -------- | --------------------------- | ------------------------ |
# | Red       | 17       | BCM 17 / Physical 11        | Series resistor required |
# | Yellow    | 27       | BCM 27 / Physical 13        | Series resistor required |
# | Green     | 22       | BCM 22 / Physical 15        | Series resistor required |

factory = LGPIOFactory()

red = LED(17, pin_factory=factory)
yellow = LED(27, pin_factory=factory)
green = LED(22, pin_factory=factory)

try:
    while True:
        # RED
        red.on()
        yellow.off()
        green.off()
        sleep(0.5)

        # RED + YELLOW
        yellow.on()
        sleep(0.5)

        # GREEN
        red.off()
        yellow.off()
        green.on()
        sleep(0.5)

        # YELLOW
        green.off()
        yellow.on()
        sleep(0.5)

        yellow.off()

except KeyboardInterrupt:
    pass
finally:
    red.off()
    yellow.off()
    green.off()
