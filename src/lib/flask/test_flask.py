from __init__ import Flask, redirect, url_for

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

if __name__ == '__main__':
	test_results = [
		test_handleRoute(),
		test_url_for(),
		test_redirect(),
		test_add_url_route(),
	]
	if False in test_results:
		print(f"All tests did not pass.")
	else:
		print(f"All tests passed.")




