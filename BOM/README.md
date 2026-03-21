# D-Pad Bill of Materials

## Core System
Below is a listing of all the parts required to build a D-Pad as well as the parts needed for optional quality of life features.  There is one part that falls in-between and a decision you'll have to make.

### Choose at least one external USB connector. The rest are optional.

Docking Connector - ADT Link T6A-T8T-NC, 30cm [https://www.aliexpress.us/item/3256804442407128.html](https://www.aliexpress.us/item/3256804442407128.html)  
Left Expansion Port Connector - ADT Link T7B-T6A, 15 cm [https://www.aliexpress.us/item/3256805100333291.html](https://www.aliexpress.us/item/3256805100333291.html)  
Right Expansion Port Connector - ADT Link T7B-T6A, 15 cm [https://www.aliexpress.us/item/3256805100333291.html](https://www.aliexpress.us/item/3256805100333291.html)

### Plastics (Required) - See STL folder
casing-front.stl  
screen-clamp.stl  
batt-mobo-mount-l.stl  
batt-mobo-mount-r.stl  
wifi-mount.stl  
kickstand.stl  
kickstand-clamp.stl  
casing-back.stl  
power-button.stl  

### Electronics (Required)
(1) Wisecoco 9 Inch 2560x1600 2K LCD [https://www.aliexpress.us/item/3256804988426586.html](https://www.aliexpress.us/item/3256804988426586.html)  
(1) ADT Link T6A-T6B, 10m [https://www.aliexpress.us/item/3256804434450164.html](https://www.aliexpress.us/item/3256804434450164.html)  
(1) Framework 13 Speaker Set [https://frame.work/products/speaker-kit?v=FRANBX0001](https://frame.work/products/speaker-kit?v=FRANBX0001)  
(1) Breakout for JST SH-Style Connector, 4-Pin Male Side-Entry [https://www.digikey.com/en/products/detail/pololu/4815/26813865](https://www.digikey.com/en/products/detail/pololu/4815/26813865)  
(1) JST SH-Style Cable, 4-Pin, Single-Ended Female, 30cm [https://www.digikey.com/en/products/detail/pololu/5521/26752073](https://www.digikey.com/en/products/detail/pololu/5521/26752073)  
(1) WiFi Antenna Set [https://www.amazon.com/dp/B0CJDVZYWF](https://www.amazon.com/dp/B0CJDVZYWF)  
(1) Framework 13 Battery (55Wh or 61Wh) [https://frame.work/products/battery?v=FRANGWAT01](https://frame.work/products/battery?v=FRANGWAT01)  
(1) Framework 13 Motherboard [https://frame.work/marketplace/mainboards?search=Framework+Laptop+13+Mainboard\&brand%5B%5D=framework](https://frame.work/marketplace/mainboards?search=Framework+Laptop+13+Mainboard&brand%5B%5D=framework)  
(1) Your choice of RAM, Storage and WiFi/Bluetooth Adapter.  
(1) Your choice of external USB connector from above.  

### Hardware (Required)
(1) Joycon Rail Set (remove flex cables if not doing optional charging) [https://www.amazon.com/dp/B08CZ1DD83](https://www.amazon.com/dp/B08CZ1DD83)  
(15) M3x5x4 Brass Heatset Insert [https://www.amazon.com/dp/B0CDH36ZMX](https://www.amazon.com/dp/B0CDH36ZMX)  
(11) M1.6x2.5x4 Brass Heatset Insert [https://www.amazon.com/dp/B07TTQXVQH](https://www.amazon.com/dp/B07TTQXVQH)  
(3) M3x10 Button Head Cap Screws  
(2) M3x16 Button Head Cap Screws  
(4) M3x20 Button Head Cap Screws  

# Optional Features
All optional features require wire.  https://www.amazon.com/dp/B07PPT11QN  
All optional features require screws. https://www.ebay.com/itm/144381124719  

## Power Button for Display

### Electronics
(1) button-pcb https://github.com/blt3dp/d-pad/tree/main/PCB/button-pcb  
(1) 6x6x5mm through hole tact switch https://www.amazon.com/dp/B07X8T9D2Q  

### Plastics
(1) opt-button.stl 

### Hardware
(1) M1.6x2.5x4 Brass Heatset Insert [https://www.amazon.com/dp/B07TTQXVQH](https://www.amazon.com/dp/B07TTQXVQH)  

# All remaining optional feature require the Framework Input Shim
(1) Framework Input Shim PCB https://github.com/blt3dp/d-pad/tree/main/PCB/framework\_input\_brkt\_smol  
(1) Amphenol 10156001-051100LF https://www.digikey.com/en/products/detail/amphenol-cs-fci/10156001-051100LF/11688418  

## Power button for Console
BOM same as for display.  If doing both just add a tact switch to the same PCB and print another opt-button.stl  

## Volume Control
### Electronics
(1) button-pcb https://github.com/blt3dp/d-pad/tree/main/PCB/button-pcb  
(2) 6x6x5mm through hole tact switch https://www.amazon.com/dp/B07X8T9D2Q  
(1) Waveshare RP2040-One https://www.amazon.com/dp/B0BLMPDMLD  

### Hardware
(1) M1.6x2.5x4 Brass Heatset Insert [https://www.amazon.com/dp/B07TTQXVQH](https://www.amazon.com/dp/B07TTQXVQH)  

### Plastics
(2) opt-button.stl  

## Joycon Charging
### Electronics
(2) Joycon Charge PCB https://github.com/blt3dp/d-pad/tree/main/PCB/joycon-charge-pcb  
(2) FH36W-11S-0.3SHW(99) https://www.digikey.com/en/products/detail/hirose-electric-co-ltd/FH36W-11S-0-3SHW-99/4168641  

### Hardware
(1) Joycon Rail Set from the required list, with flex cables  
(1) M1.6x2.5x4 Brass Heatset Insert [https://www.amazon.com/dp/B07TTQXVQH](https://www.amazon.com/dp/B07TTQXVQH)  
