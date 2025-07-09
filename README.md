# bricknet-v2
A Python Bluetooth communication library for the LEGO Spike


```python 
from pybricks.hubs import InventorHub, ThisHub

from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

from urandom import randint

# from pybricks.iodevices import XboxController

hub = InventorHub()
hub = ThisHub(broadcast_channel=1)

colors = [Color.RED, Color.ORANGE, Color.YELLOW, Color.GREEN, Color.CYAN, Color.BLUE, Color.VIOLET, Color.MAGENTA]
test = [
    "Hello", 
    "Canada", 
    "Stars",
    "123456789012345678901234"
]

while True:

    rand = randint(0, 3)

    print("Broadcasting...")
    print(test[rand])
    hub.ble.broadcast(test[rand])

    # hub.light.on(test[rand])

    wait(2000)
```

```python
from pybricks.hubs import EssentialHub, ThisHub

from pybricks.pupdevices import Motor, ColorSensor, ColorLightMatrix
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

id = 1

hub = EssentialHub()
hub = ThisHub(observe_channels=[id])

# colors = [Color.RED, Color.ORANGE, Color.YELLOW, Color.GREEN, Color.CYAN, Color.BLUE, Color.VIOLET, Color.MAGENTA]

while True:

    print("Observing...")

    data = hub.ble.observe(id)

    if data is not None or True:
        
        print(data)
        hub.light.on(Color.RED)

    wait(2000)

```