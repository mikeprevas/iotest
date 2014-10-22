import waferslim.protocol
from waferslim.converters import *

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
        
        
    @convert_arg(to_type=int)
    def setPort(self, value):