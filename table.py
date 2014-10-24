#!/usr/bin/python3
import waferslim.protocol
from waferslim.converters import *
import sys
sys.path.append("/home/pi/pyfixtures/hardware/iotest")
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


