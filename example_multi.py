from bricknet.multi import Multi

import time

# Define the list of messages
ads = [
    {"channel": 1, "message": "red"},
    {"channel": 2, "message": "blue"},
]

# Create the Multi broadcaster
multi = Multi(messages=ads, delay=0.5)  # Delay is in seconds

# Start broadcasting in a loop
try:
    multi.start()
    time.sleep(10)

# Always stop it cleanly
finally:
    multi.stop()
