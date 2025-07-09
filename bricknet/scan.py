import asyncio
from bleak import BleakScanner

from . import config

class Scan:

    def __init__(self, callback=None, adapter_name=None):
        self.callback = callback
        self.adapter_name = adapter_name or config.DEFAULT_ADAPTER_NAME
        self.scanner = BleakScanner(detection_callback=self._detection_callback,
                                    adapter=self.adapter_name)

    def _detection_callback(self, device, advertisement_data):

        for manufacturer_id, data in advertisement_data.manufacturer_data.items():

            if manufacturer_id == config.DEFAULT_MANUFACTURER_ID:

                try:
                    message = ''.join(chr(b) for b in data if 32 <= b <= 126)
                except Exception:
                    message = None

                if self.callback and message:
                    self.callback(device, advertisement_data, message)

    async def start(self):
        await self.scanner.start()

    async def stop(self):
        await self.scanner.stop()
