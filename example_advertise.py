import threading
import time

from bricknet.advertise import Advertise

# Create a function to make the advertisement
def run_advertise():

    ad = Advertise(channel=1, message="green")
    ad.start()

# Create and start the advertisement in a separate thread
ad = Advertise(channel=1, message="green")
thread = threading.Thread(target=ad.start)
thread.start()

# Allow the advertisement to run for 30 seconds
time.sleep(30)

# Stop the advertisement and wait for the thread to finish
ad.stop()
thread.join()
print("Advertisement stopped after 30 seconds.")
