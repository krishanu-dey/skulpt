from helpers import routeMatch

class Request:
    def __init__(self):
        self.method = ""
        self.args = {}
        self.form = {}
request = Request()

global app
html_files = {}

session = {}

class Flask():
    "The starting class for all Flask web apps"
    
    def __init__(self, name):
        self.appName = name
        self.endpointToRoutes = {}
        self.routingTable = {}
        global app
        app = self

    def run(self):
        session = {}
        print("Flask is running")
    
    def route(self, route, **kwargs):
        def wrapper(func):
            self.add_url_route(route, func.__name__, func, **kwargs)
            return func
        return wrapper

    def add_url_route(self, route, endpoint, view_function, **kwargs):
        methods = kwargs.pop('methods', '')
        methods = [method.upper() for method in methods]
        if methods == []:
            methods.append("GET")

        self.endpointToRoutes[endpoint] = route
        self.routingTable[route] = RouteTableEntry(view_function, methods)

    def handleRoute(self, routeInput, requestData):
        response = {}
        for routeFromTable in self.routingTable.keys():
            evaluatedRoute = routeMatch(routeFromTable, routeInput)
            if evaluatedRoute[0]:
                requestMethod = requestData["method"]
                if requestMethod.upper() in self.routingTable[routeFromTable].methods:
                    loadDataToRequest(requestData)
                else:
                    response["error"] = f"The method {routeFromTable} does not support form method {requestMethod}."
                
                try:
                    htmlWithParamsMaybe = self.routingTable[routeFromTable].func(**evaluatedRoute[1])
                    if type(htmlWithParamsMaybe) == str:  	
                        response["html"] = htmlWithParamsMaybe
                    else:
                        response["html"] = htmlWithParamsMaybe[0]
                        response["template_params"] = htmlWithParamsMaybe[1]
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
                    
                    print(e)
                    response["html"] = f"<h4> Syntax Error in the '{routeFromTable}' route function of '{requestMethod}' request type.</h4>"\
                        f'<h6>Error: {str(e)}</h6>'
                    response["error"] = str(e)

                response["endpointToRoutes"] = self.endpointToRoutes

                return response

        response["error"] = "Invalid route requested."
        return response

class RouteTableEntry:
    def __init__(self, func, methods):
        self.func = func
        self.methods = methods

def loadDataToRequest(requestData):
    request.method = requestData["method"]
    if request.method.upper() == "GET":
        request.args = requestData.get("data")
    elif request.method.upper() == "POST":
        request.form = requestData.get("data")

def redirect(newRoute):
    return app.routingTable[newRoute].func()

def url_for(functionName, **kwargs):
    return app.endpointToRoutes[functionName]

#TODO: All HTML files to be passed to flask lib as a dict(key=file name, value=html text)
def render_template(htmlText, **kwargs):
    template_params = {}
    for key, value in kwargs.items():
        template_params[key] = value
    return htmlText, template_params

def abort(code):
	if code == 404:
		return '<title>404 Not Found</title><body><h1>Not Found</h1>'\
		'<p>The requested URL was not found on the server. If you entered '\
		'the URL manually please check your spelling and try again.</p></body>'

	return f'<title>Error Page: {code}</title> Error page for code number {code}'

