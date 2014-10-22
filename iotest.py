#!/usr/bin/python3
import waferslim.protocol
from waferslim.converters import *
from NI_USB_6501.ni_usb_6501 import *
class Table(object):
    def __init__(self, args):
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
    def __init__(self, args):
        Table.__init__(self, args)
        self.port = None
        self.pin = None
        dev = get_adapter()
        if not dev:
            raise Exception("No device found")

        
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

        data = dev.read_port(0)
        dev.writePort(0, data | (1 << self.pin))
   
    def result(self):
        return "1"
    
    
if __name__ == "__main__":
    t = IoTest("main")
    t.setPort(0)
    t.setPin(0)
    t.execute()