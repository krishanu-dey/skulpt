from __init__ import Flask, redirect, url_for

app = Flask("basic app")

@app.route("/lg", methods=["POST", "GET"])
def login():
	print("login here")
	return redirect("/signup")

@app.route("/signup")
def signup():
	print("signup here")
	return "<h1>Hi</h1>"
    
if __name__ == '__main__':
	app.run()
	response = app.handleRoute("/lg")

	print(url_for("login"))


