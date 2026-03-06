import usb_cdc
import storage
import board
import digitalio

usb_cdc.enable(console=False, data=False)

button = digitalio.DigitalInOut(board.GP28)
button.pull = digitalio.Pull.UP

if button.value:
   storage.disable_usb_drive()