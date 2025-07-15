# bricknet/multi.py
import time
import threading

from .advertise import Advertise
from . import config

class Multi:

    def __init__(self, messages, delay=1):
        self.messages = messages
        self.delay = delay
        self.running = False
        self.thread = None

    def _loop(self):

        while self.running:

            for message in self.messages:

                if not self.running:
                    break

                ad = Advertise(message['channel'], message['message'])
                thread = threading.Thread(target=ad.start)
                thread.start()

                time.sleep(self.delay)

                ad.stop()
                thread.join()

    def start(self):

        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._loop)
            self.thread.start()

    def stop(self):
        
        self.running = False
        if self.thread:
            self.thread.join()
