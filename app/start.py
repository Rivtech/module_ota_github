########################################################################################
# start.py (microPython)
# Author:   Modified example
# Date:     Created:  29.12.2020
#
# First proof of concept for OTA Updated main replacement
#
#
# Development environment specifics:
#   IDE: VS-Code 1.45.1
#   Compiler: MicroPython 1.13
#   Hardware Platform: ESP32
#   Underlying Hardware Module Interface: neopixel_demo.py
#
#######################################################################################


import neopixel_demo, time
RELEASE_TAG = '0.0'
DEMO_FUNKTION = 'Weiss blinken in einer Loop'

print('Executing Start.py')
print('To check for updates, force an (hardware) machine.reset')

while True:
    print('Release Version: ' + RELEASE_TAG)
    print('LED Demo Funktion: ' + DEMO_FUNKTION)
    neopixel_demo.demo()
    time.sleep_ms(1000)


 