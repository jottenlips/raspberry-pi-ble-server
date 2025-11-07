#!/usr/bin/env python3
from bluezero import peripheral


# Pi BLE adapter and local name
ADAPTER_ADDR = 'B8:27:EB:16:8F:44'
LOCAL_NAME = 'raspberrypi'

# Create peripheral
ble_peripheral = peripheral.Peripheral(adapter_address=ADAPTER_ADDR,
                                       local_name=LOCAL_NAME)

# Service UUID and ID
SERVICE_UUID = '12345678-1234-5678-1234-56789abcdef1'
SERVICE_ID = 0  # internal service index

def send_response(message: str):
    # Encode string as bytes
    value = bytes(message, 'utf-8')
    # Send notification to all subscribed clients
    ble_peripheral.notify(SERVICE_ID, CHAR_UUID, value)

# Callback when client writes
def write_callback(value):
    print("Raw bytes received:", list(value))
    try:
        send_response("Echo: " + value.decode())
    except Exception:
        print("Received raw bytes:", value)

# Add service
ble_peripheral.add_service(
    srv_id=SERVICE_ID,
    uuid=SERVICE_UUID,
    primary=True
)

# Characteristic UUID
CHAR_UUID = '12345678-1234-5678-1234-56789abcdef0'

# Add writable characteristic
ble_peripheral.add_characteristic(
    srv_id=SERVICE_ID,       # use same service ID
    chr_id=0,                # first characteristic
    uuid=CHAR_UUID,
    value=bytearray(),       # initial value
    notifying=True,
    flags=['write', 'write-without-response', 'notify'],         # BLE write flags
    write_callback=write_callback
)


# Start advertising
print(f"Advertising as {LOCAL_NAME}. Waiting for BLE writes...")

ble_peripheral.publish()  # <-- use publish() instead of run()

# Keep the program running
import signal
signal.pause()  # waits indefinitely for signals (like Ctrl+C to stop)
