class Flask():
    "The starting class for all Flask web apps"
    
    def __init__(self, name):
        self.appName = name
        self.fnNamesToRoutes = {}
        self.routingTable = {}
        global app
        app = self

    def run(self):
        print("Flask is running")
    
    def route(self, route, **kwargs):
        def wrapper(func):
            self.fnNamesToRoutes[func.__name__] = route
            self.routingTable[route] = RouteTableEntry(func, kwargs.pop('methods', ''))
            return func
        return wrapper

    def handleRoute(self, route):
        response = {}
        response["html"] = self.routingTable[route].func()
        response["fnNamesToRoutes"] = self.fnNamesToRoutes
        return response

class RouteTableEntry:
    def __init__(self, func, methods):
        self.func = func
        self.methods = methods

def redirect(newRoute):
    return app.routingTable[newRoute].func()

def url_for(functionName, **kwargs):
    return app.fnNamesToRoutes[functionName]
