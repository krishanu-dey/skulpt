from __init__ import Flask, redirect, url_for, abort
from helpers import routeMatch

# Set up test environment.
app = Flask("basic app")

@app.route("/lg")
def login_redirect():
	return redirect("/login")

@app.route("/login", methods=["POST", "GET"])
def login():
	return "login here"

@app.route("/signup")
def signup():
	return "signup here"

#Test functions.
def test_handleRoute():
	needResp = {
	'html': 'signup here', 
	'endpointToRoutes': {
		'login_redirect': '/lg', 
		'login': '/login', 
		'signup': '/signup'
		}
	}
	
	gotResp = app.handleRoute("/signup")
	
	if gotResp != needResp:
		print(f'app.handleRoute("/signup") returned {gotResp}, but need {needResp}.')
		return False
	return True

def test_url_for():
	needResp = "/lg"
	
	gotResp = url_for("login_redirect")

	if gotResp != needResp:
		print(f'url_for("/signup") returned {gotResp}, but need {needResp}.')
		return False
	return True

def test_redirect():
	needResp = "signup here"
	
	gotResp = redirect("/signup")

	if gotResp != needResp:
		print(f'redirect("/signup") returned {gotResp}, but need {needResp}.')
		return False
	return True

def test_add_url_route():
    app.add_url_route("/signup", "signup", signup)	
	
    needRoute = "/signup"
    gotRoute = app.endpointToRoutes["signup"]
    if needRoute != gotRoute:
        print(f'app.endpointToRoutes["signup"] returned {gotRoute}, but need {needRoute}.')
        return False

    needResp = "signup here"
    gotResp = app.routingTable["/signup"].func()
    if needResp != gotResp:
        print(f'app.routingTable["/signup"] returned {gotResp}, but need {needResp}.')
        return False

    return True

def test_abort():
    code = 401
    needResp = f'<title>Error Page: {code}</title> Error page for code number {code}'

    gotResp = abort(code)
    if needResp != gotResp:
        print(f'abort({code}) returned {gotResp}, but need {needResp}.')
        return False

    return True

def test_routeMatch():

	if True != routeMatch("/blog/<int:postID>", "/blog/12")[0]:
		print("routeMatch() test failed")
		return False
	
	if False != routeMatch("/blog/<user>/<int:postID>/<float:long>", "/blog/12")[0]:
		print("routeMatch() test failed")
		return False

	if False != routeMatch("/blog/<user>/<int:postID>/<float:long>", "/blog/kris/12/stringo")[0]:
		print("routeMatch() test failed")
		return False

	gotResp = routeMatch("/blog/<user>/<int:postID>/<float:long>", "/blog/kris/12/3.0")
	needResp = (True, {'user': 'kris', 'postID': 12, 'long': 3.0})
	if needResp != gotResp:
		print(f"routeMatch() test failed: got response {gotResp}, need response {needResp}")
		return False

	return True

if __name__ == '__main__':
	test_results = [
		test_handleRoute(),
		test_url_for(),
		test_redirect(),
		test_add_url_route(),
		test_abort(),
		test_routeMatch()
	]
	if False in test_results:
		print(f"All tests did not pass.")
	else:
		print(f"All tests passed.")

