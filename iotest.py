#!/usr/bin/python3
import waferslim.protocol
from waferslim.converters import *
import sys
sys.path.append("/home/pi/pyfixtures/hardware/iotest")
from ni_usb_6501 import *
class Table(object):
    def __init__(self, args=None):
        print ("table init %s" % (args))
        
    def beginTable(self):
        print("begintable is called")

    def endTable(self):
        print("endtable is called")

    def execute(self):
        print("execute when invoked?")

    @convert_arg(to_type=str) 
    def table(self, args):
        print ("table type: %s %s" % (type(args), args))

class IoTest(Table):
    def __init__(self, args=None):
        Table.__init__(self, args)
        self.port = None
        self.pin = None
        self.dev = get_adapter()
#        if not self.dev:
#            raise Exception("No device found")

        
    @convert_arg(to_type=int)
    def setPort(self, value):
        self.port = value
 
    @convert_arg(to_type=int)
    def setPin(self, value):
        self.pin = value

    def reset(self):
        self.pin = None
        self.port = None
        
    def execute(self):
        if self.pin == None and self.port == None:
            raise Exception("Pin and port must be set")

        data = self.dev.read_port(0)
        self.dev.write_port(0, data | (1 << self.pin))
   
    def result(self):
        data = self.dev.read_port(0)
        return str(data)
    
    
if __name__ == "__main__":
    t = IoTest("main")
    t.setPort(0)
    t.setPin(0)
    t.execute()
