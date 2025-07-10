import threading
import time
from bricknet.advertise import Advertise

def run_advertise():
    ad = Advertise(channel=1, message="green")
    ad.start()

ad = Advertise(channel=1, message="green")
thread = threading.Thread(target=ad.start)
thread.start()

time.sleep(30)  # Advertise for 30 seconds

ad.stop()
thread.join()
print("Advertisement stopped after 30 seconds.")
