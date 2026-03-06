# D-Pad volume control HID device



This folder contains instructions and code that you will upload to the RP2040 for it to function as a volume control HID device.



### Installing CircuitPython 

The software is written in CircuitPython 10.x and uses the HID module of CircuitPython Library Bundle.

1. Download the latest stable 10.x CircuitPython UF2 from the official website [here](https://circuitpython.org/board/pimoroni\_tiny2040/).

2. Push and hold the BOOTSEL button and plug your Tiny 20240 into the USB port of your computer. Release the BOOTSEL button after your microcontroller is connected.

3. It will mount as a Mass Storage Device called RPI-RP2.

4. Drag and drop the CircuitPython UF2 file onto the RPI-RP2 volume. 



### Installing HID libraries

1. Download the library bundle for the CircuitPython version you installed 10.x from [here](https://circuitpython.org/libraries).

2. Unzip the bundle; Copy `adafruit\_hid` from the `lib` folder to `<CIRCUITPY DRIVE>/lib/`.



### Software installation

1. Download the 2 .py files from this folder.

2. Place them in the root of the \<CIRCUITPY DRIVE>.

   2a. The code should immediately run and begin functioning as a volume up (GP28) and volume down (GP29) when either are bridged to ground.
   
   2b. The boot.py will stop the <CIRCUITPY DRIVE> from mounting on the next boot.  It does make it more difficult to edit the code if you wish to.  If you need to access the code, hold the volume up (GP28) button while powering on the system and it will mount the \<CIRCUITPY DRIVE>.


