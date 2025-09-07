from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome User"

@app.route("/index")
def index():
    return "Welcome User index change to this that mm"


if __name__ == "__main__":
    app.run(debug=True)