import time

import digitalio
import analogio
import board
import usb_hid
from adafruit_ble import BLERadio, Advertisement
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# for testing
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# declare UART server
ble = BLERadio()
uart_server = UARTService()
advertisement = ProvideServicesAdvertisement(uart_server)
scan_response = Advertisement()
scan_response.complete_name = "CircuitPython HID"
if not ble.connected:
    print("advertising")
    ble.start_advertising(advertisement, scan_response)
else:
    print("already connected")
    print(ble.connections)

# initialize keyboard
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# Advertise when not connected.
led.value = True

left_foot = analogio.AnalogIn(board.A1)
right_foot = analogio.AnalogIn(board.A2)
pressure_input = analogio.AnalogIn(board.A4)

while True:
    while not ble.connected:
        pass
    print("Start typing:")

    while ble.connected:
        print("connected")
        if left_foot.value > 30000 and right_foot.value > 30000:
            keyboard.press(Keycode.SPACE)
            keyboard.release_all()
        time.sleep(0.1)
