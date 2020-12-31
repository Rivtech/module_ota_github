########################################################################################
# neopixel_demo.py (microPython)
# Author:   Modified example
# Date:     Created:  29.12.2020
#
# First proof of concept for a simple enviromental sensor peripheral with scd30 sensiron 
# sensor module.
#
# Short neopixel hello world demo.
#
# Development environment specifics:
#   IDE: VS-Code 1.45.1
#   Compiler: MicroPython 1.13
#   Hardware Platform: ESP32
#   Underlying Hardware Module Interface: neopixel.py
#
#######################################################################################

import machine
import time
import neopixel

class NeoDemo:
    def __init__(self):
        # Hardware config
        self.led_pin = machine.Pin(14, machine.Pin.OUT)
        self.setup_led_indicator()

    def setup_led_indicator(self):
        self.rgb_indicator = neopixel.NeoPixel(self.led_pin, 1)
        self.led_number =  self.rgb_indicator.n

    def cycle(self):
        for i in range(4 * self.led_number):
            for j in range(self.led_number):
                self.rgb_indicator[j] = (0, 0, 0)
            self.rgb_indicator[i % self.led_number] = (255, 255, 255)
            self.rgb_indicator.write()
            time.sleep_ms(25)

    def white_intensity_sweep(self):
        for i in range(255):
            col_val = i
            for j in range(self.led_number):
                self.rgb_indicator[j] = (col_val, col_val, col_val)
            self.rgb_indicator.write()
            time.sleep_ms(10)
        for i in range(255):
            col_val = 255 - i
            for j in range(self.led_number):
                self.rgb_indicator[j] = (col_val, col_val, col_val)
            self.rgb_indicator.write()
            time.sleep_ms(10)


    def rainbow_sweep(self):
        red_val = 0
        green_val = 0
        blue_val = 0
        sleep_time_ms = 10
        # Sweep red to green
        for i in range(255):
            red_val = 255 - i
            green_val = i
            for j in range(self.led_number):
                self.rgb_indicator[j] = (red_val, green_val, blue_val)
            self.rgb_indicator.write()
            time.sleep_ms(sleep_time_ms)
        # Sweep green to blue
        for i in range(255):
            green_val = 255 - i
            blue_val = i
            for j in range(self.led_number):
                self.rgb_indicator[j] = (red_val, green_val, blue_val)
            self.rgb_indicator.write()
            time.sleep_ms(sleep_time_ms)
        # Sweep blue to red
        for i in range(255):
            blue_val = 255 - i
            red_val = i
            for j in range(self.led_number):
                self.rgb_indicator[j] = (red_val, green_val, blue_val)
            self.rgb_indicator.write()
            time.sleep_ms(sleep_time_ms)


def demo():
    led_pixel = NeoDemo()
    led_pixel.white_intensity_sweep()


if __name__ == "__main__":
    demo()