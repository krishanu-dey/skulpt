class Flask():
    "The starting class for all Flask web apps"
    
    def __init__(self, name):
        self.appName = name
        self.routes = []
        self.routingTable = {}

    def run(self):
        # print(self.routingTable)
        # for route in self.routes:
        #     if len(self.routingTable[route].methods) == 0:
        #         print(route + " -> " + str(self.routingTable[route].func))
        #     else:
        #         print(route + " -> " + str(self.routingTable[route].func) +
        #             " with methods="+ str(self.routingTable[route].methods))
        print("Flask is running")
    
    def route(self, route, **kwargs):
        def wrapper(func):
            self.routes.append(route)
            self.routingTable[route] = RouteTableEntry(func, kwargs.pop('methods', ''))
            return func
        return wrapper

    def handleRoute(self, route):
        return self.routingTable[route].func()

class RouteTableEntry:
    def __init__(self, func, methods):
        self.func = func
        self.methods = methods