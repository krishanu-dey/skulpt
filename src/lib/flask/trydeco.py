class Flask():
    "The starting class for all Flask web apps"

    

    def __init__(self, name):
        self.appName = name
        self.request = "0"
        self.session = "off"
        self.routes = []
        self.routingTable = {}

    def run(self):
        print(self.routingTable)
        for route in self.routes:
            print(route + " -> " + str(self.routingTable[route].func) +
             " with methods="+ str(self.routingTable[route].methods))
    
    def route(self, route, **kwargs):
        def wrapper(func):
            self.routes.append(route)
            rt = RouteTable(func, kwargs.pop('methods', ''))
            self.routingTable[route] = rt
            return func
        return wrapper

class RouteTable:
    def __init__(self, func, methods):
        self.func = func
        self.methods = methods


app = Flask("basic app")

@app.route("/login", methods=["POST", "GET"])
def login():
    print("login here")

@app.route("/signup")
def signup():
    print("signup here")
    
if __name__ == '__main__':
    app.run()