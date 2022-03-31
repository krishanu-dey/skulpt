from helpers import routeMatch

from __init__ import Flask, redirect, url_for, abort, render_template, request, session
from flask_code_for_testing import app, signup

endpointToRoutes = {
	'login_redirect': '/lg', 
	'login': '/login', 
	'signup': '/signup',
	'dynamic_url': '/blog/<user>/<int:postID>/<float:weight>',
	'template': '/template',
	'add_to_session': '/add_to_session/<user>',
}

#Test functions.x
def test_handleRoute():
	requestData = {"method": "GET"}
	needResp = {
	'html': 'this user kris has 12 and weight 70.0', 
	'endpointToRoutes': endpointToRoutes,
	}
	
	gotResp = app.handleRoute("/blog/kris/12/70.0", requestData)
	
	if gotResp != needResp:
		print(f'app.handleRoute("/dynamic_url") returned {gotResp}, but need {needResp}.', None)
		return False

	needResp = {
	'html': 'hi {{ name }} , {{ age }}',
	'template_params': {'name': 'kris', 'age': 23},
	'endpointToRoutes': endpointToRoutes,
	}
	gotResp = app.handleRoute("/template", requestData)
	if gotResp != needResp:
		print(f'app.handleRoute("/template", None) returned {gotResp}, but need {needResp}.')
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


def test_add_url_rule():
    app.add_url_rule("/signup", "signup", signup)	
	
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

	gotResp = routeMatch("/blog/<user>/<int:postID>/<float:long>", "/blog/kris/12/70.0")
	needResp = (True, {'user': 'kris', 'postID': 12, 'long': 70.0})
	if needResp != gotResp:
		print(f"routeMatch() test failed: got response {gotResp}, need response {needResp}")
		return False

	return True


def test_render_template():
    needResp = 'hi', {'name': 'kris', 'age': 23}

    gotResp = render_template("hi", name="kris", age=23)
    if needResp != gotResp:
        print(f'render_template("hi", name="kris", age=23) returned {gotResp}, but need {needResp}.')
        return False

    return True


def test_add_to_session():
	requestData = {"method": "GET"}
	needResp = {
	'html': "session: {'username': {'kris'}}", 
	'endpointToRoutes': endpointToRoutes,
	}
	
	gotResp = app.handleRoute("/add_to_session/kris", requestData)
	
	if gotResp != needResp:
		print(f'app.handleRoute("/add_to_session/kris") returned {gotResp}, but need {needResp}.', None)
		return False

	return True


def test_form_wiring():
	form = {
		"method": "POST",
		"data": {
			"test": "correct post request",
		}
	}
	gotResp = app.handleRoute("/login", form)
	needResp = "login POST - {'test': 'correct post request'}"
	if gotResp["html"] != needResp:
		print(f'test_form_wiring: handleRoute("/login", {form}) returned {gotResp["html"]}, but need {needResp}.')
		return False

	form = {
		"method": "GET",
		"data": {
			"test": "correct get request",
		}
	}
	gotResp = app.handleRoute("/login", form)
	if gotResp["html"] != "login GET - {'test': 'correct get request'}":
		print(f'test_form_wiring: handleRoute("/login", {form}) returned {gotResp["html"]}, but need {needResp}.')
		return False

	form = {	
		"method": "delete",
		"data": {
			"test": "incorrect request",
		}
	}
	gotResp = app.handleRoute("/login", form)
	if gotResp["error"] != 'The method /login does not support form method delete.':
		print(f'test_form_wiring: handleRoute("/login", {form}) returned {gotResp["html"]}, but need {needResp}.')
		return False

	return True


# def test_error():
# 	requestData = {"method": "GET"}
# 	gotResp = app.handleRoute("/error", requestData)
# 	needResp = "<h4> Syntax Error in the '/error' route function of 'GET' request type.</h4><h6>Error: name 'lslslsl' is not defined</h6>"
# 	if gotResp["html"] != needResp:
# 		print(f'test_form_wiring: handleRoute("/error", {requestData}) returned {gotResp["html"]}, but need {needResp}.')
# 		return False

# 	return True

if __name__ == '__main__':
	test_results = [
		test_handleRoute(),
		test_url_for(),
		test_redirect(),
		test_add_url_rule(),
		test_abort(),
		test_routeMatch(),
		test_render_template(),
		test_form_wiring(),
		test_add_to_session(),
		# test_error(),
	]
	if False in test_results:
		print(f"All tests did not pass." + str(test_results))
	else:
		print(f"All tests passed.")

