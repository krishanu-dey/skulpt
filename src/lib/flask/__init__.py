from helpers import routeMatch

global app

class Flask():
    "The starting class for all Flask web apps"
    
    def __init__(self, name):
        self.appName = name
        self.endpointToRoutes = {}
        self.routingTable = {}
        global app
        app = self

    def run(self):
        print("Flask is running")
    
    def route(self, route, **kwargs):
        def wrapper(func):
            self.endpointToRoutes[func.__name__] = route
            self.routingTable[route] = RouteTableEntry(func, kwargs.pop('methods', ''))
            return func
        return wrapper

    def add_url_route(self, route, endpoint, view_function, **kwargs):
        self.endpointToRoutes[endpoint] = route
        self.routingTable[route] = RouteTableEntry(view_function, kwargs.pop('methods', ''))

    def handleRoute(self, routeInput):
        response = {}
        for routeFromTable in self.routingTable.keys():
            evaluatedRoute = routeMatch(routeFromTable, routeInput)
            if evaluatedRoute[0]:    	
                response["html"] = self.routingTable[routeFromTable].func(**evaluatedRoute[1])
                response["endpointToRoutes"] = self.endpointToRoutes
        return response

class RouteTableEntry:
    def __init__(self, func, methods):
        self.func = func
        self.methods = methods

def redirect(newRoute):
    return app.routingTable[newRoute].func()

def url_for(functionName, **kwargs):
    return app.endpointToRoutes[functionName]

def abort(code):
	if code == 404:
		return '<title>404 Not Found</title><body><h1>Not Found</h1>'\
		'<p>The requested URL was not found on the server. If you entered '\
		'the URL manually please check your spelling and try again.</p></body>'

	return f'<title>Error Page: {code}</title> Error page for code number {code}'

