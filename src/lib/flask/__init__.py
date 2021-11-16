class Flask():
    "The starting class for all Flask web apps"

    def __init__(self, name):
        self.appName = name
    	self.request = "0"
    	self.session = "off"
    	self.routingTable = {}

    @classmethod
    def run(self):
        print("Flask.app here!")

    
    def route(func):
    	self.routingTable["/"] = func

