import serial
import platform

class AdafruitUSBBackpackLCD:
    def __init__(self, port):
        self.serial = serial.Serial(port, 9600, timeout=5)
        self.red = 0x0f
        self.green = 0x0f
        self.blue = 0x0f

    def background(self, red, green, blue):
	[self.red, self.green, self.blue] = [red, green, blue]
        self.serial.write(bytearray([0xfe, 0xd0, red, green, blue]))

    def backlight(self, on=True):
        arr = bytearray([0xfe, 0x42])
        if not on:
           arr[1] = 0x46
        self.serial.write(arr)

    def clear(self):
        self.serial.write(bytearray([0xfe, 0x58]))

    def home(self):
        self.serial.write(bytearray([0xfe, 0x48]))

    def write(self, text):
        self.serial.write(text)
