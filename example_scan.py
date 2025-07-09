import asyncio
from bricknet.scan import Scan

def handle_message(device, advertisement_data, message):
    print(f"📡 From: {device.address}")
    print(f"📛 Name: {device.name}")
    print(f"📩 Message: {message}")
    print(f"🛰️ RSSI: {advertisement_data.rssi}")

async def main():
    scanner = Scan(callback=handle_message)
    await scanner.start()

    print("🔍 Scanning for 10 seconds...")
    await asyncio.sleep(10)

    await scanner.stop()
    print("🛑 Scan complete.")

if __name__ == "__main__":
    asyncio.run(main())