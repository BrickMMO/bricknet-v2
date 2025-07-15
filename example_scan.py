import asyncio
from bricknet.scan import Scan

# Create a callback function to handle incoming messages
def handle_message(device, advertisement_data, message):
    print(f"📡 From: {device.address}")
    print(f"📛 Name: {device.name}")
    print(f"📩 Message: {message}")
    print(f"🛰️ RSSI: {advertisement_data.rssi}")

# Create an asynchronous main function to run the scan
async def main():

    scanner = Scan(callback=handle_message)
    await scanner.start()

    print("🔍 Scanning for 10 seconds...")
    await asyncio.sleep(10)

    await scanner.stop()
    print("🛑 Scan complete.")

# Run the main function using asyncio
if __name__ == "__main__":
    asyncio.run(main())