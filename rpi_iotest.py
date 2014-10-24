#!/usr/bin/python3
import waferslim.protocol
from waferslim.converters import *
import sys
import os
sys.path.append(os.path.expanduser('~')+"/pyfixtures/hardware/iotest")
from RPi.GPIO import gpio
class IoTest(Table):
    def __init__(self, args=None):
        Table.__init__(self, args)
        self.port = None
        self.pin = None
#        gpio.set_mode()
        
    @convert_arg(to_type=int)
    def setPort(self, value):
        if value > 2:
            raise Exception("Illegal port")

        self.port = value
 
    @convert_arg(to_type=int)
    def setPin(self, value):
       if value > 7:
           raise Exception("Illegal pin")

       print(value)
       self.pin = value

    def reset(self):
        self.pin = None
        self.port = None
        
    def execute(self):
        if self.pin == None and self.port == None:
            raise Exception("Pin and port must be set")

        print("port %d %d" % (self.port, self.pin))
        data = self.dev.read_port(self.port)
        if self.port == 1 and self.pin == 0:
#            data = data & 0xEF
            self.dev.write_port(1, 0)

        print("exec")

   
    def result(self):
#	if not self.pin or not self.port:
        data = self.dev.read_port(self.port) & (1 << self.pin) 
        print("result")
        return str(data >> self.pin)

    
if __name__ == "__main__":
    t = IoTest("main")
    t.setPort(0)
    t.setPin(0)
    t.execute()
