from __init__ import Flask, redirect, url_for, abort, render_template, request, session

# Set up test environment.
app = Flask("basic app")

@app.route("/lg")
def login_redirect():
	return redirect("/login")

@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		return "login POST - " + str(request.form)
	elif request.method == "GET":
		return "login GET - " + str(request.args)
	return "login here - request method not supported."

@app.route("/signup")
def signup():
	return "signup here"

@app.route("/blog/<user>/<int:postID>/<float:weight>")
def dynamic_url(user, postID, weight):
	return f"this user {user} has {postID} and weight {weight}"

@app.route("/template")
def template():
    return render_template("hi {{ name }} , {{ age }}", name="kris", age=23)

@app.route("/add_to_session/<user>")
def add_to_session(user):
	session["username"] = {user}
	return "session: " + str(session)
