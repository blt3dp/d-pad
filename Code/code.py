import time
import digitalio
import board
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# Define the pins for the buttons
btn1_pin = board.GP28
btn2_pin = board.GP29

# Create the Keyboard object
consumer = ConsumerControl(usb_hid.devices)

# Set up the buttons
btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.UP

while True:
    # Check if button 1 is pressed
    if not btn1.value:
        consumer.send(ConsumerControlCode.VOLUME_INCREMENT)
        time.sleep(0.1)

    # Check if button 2 is pressed
    if not btn2.value:
        consumer.send(ConsumerControlCode.VOLUME_DECREMENT)
        time.sleep(0.1)

    # Delay to avoid excessive CPU usage
    time.sleep(0.1)