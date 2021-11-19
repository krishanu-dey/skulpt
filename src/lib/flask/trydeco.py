from __init__ import Flask

app = Flask("basic app")

@app.route("/login", methods=["POST", "GET"])
def login():
    print("login here")

@app.route("/signup")
def signup():
    print("signup here")
    
if __name__ == '__main__':
    app.run()