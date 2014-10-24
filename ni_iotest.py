#!/usr/bin/python3
import waferslim.protocol
from waferslim.converters import *
import sys
import os
sys.path.append(os.path.expanduser("~")+"/pyfixtures/hardware/iotest")
from table import *
from ni_usb_6501 import *

class Ni6501IoTest(Table):
    def __init__(self, args=None):
        Table.__init__(self, args)
        self.port = None
        self.pin = None
        self.write = None
        self.direction = [0x00, 0x00, 0x00]
        self.dev = get_adapter()
        if not self.dev:
            raise Exception("No device found")

        self.dev.set_io_mode(0x00, 0x00, 0x00)

    def setDirection(self, value):
        if self.port==None or self.pin==None:
            raise Exception("Pin/port must be set before direction")
        if value == "output":
            self.direction[self.port] |= (1 << self.pin) 
        
    @convert_arg(to_type=int)
    def setPort(self, value):
        if value > 2:
            raise Exception("Illegal port")

        self.port = value
 
    @convert_arg(to_type=int)
    def setPin(self, value):
       if value > 7:
           raise Exception("Illegal pin")

       self.pin = value

    def reset(self):
        self.pin = None
        self.port = None
        self.write = None
        
    def execute(self):
        if self.pin == None and self.port == None:
            raise Exception("Pin and port must be set")

        self.dev.set_io_mode(self.direction[0], self.direction[1], self.direction[2])
        if self.write != None:
            pins = self.dev.read_port(self.port)
            pins &= ~(1 << self.pin) # mask out
            self.dev.write_port(self.port, (pins & (self.write << self.write)))

    # TODO use decorators 
    # write() 1 or 0 for pin
    def set_write(self, value):
        if self.pin == None and self.port == None:
            raise Exception("Pin and port must be set")

        # if input and value = '-' just return
        if value=='-' and (self.direction[self.port] & (1 << self.pin))== 0:
            return

        try:
            print (value)
            value = int(value)
            if value>1: 
                raise

            self.write = value
        except:
            raise Exception("only numeric value allowed 0 or 1")
 
    def read(self):
        if self.pin == None and self.port == None:
            raise Exception("Pin and port must be set")

        data = self.dev.read_port(self.port) & (1 << self.pin) 
        return str(data >> self.pin)

    
if __name__ == "__main__":
    t = IoTest("main")
    t.setPort(0)
    t.setPin(0)
    t.execute()
