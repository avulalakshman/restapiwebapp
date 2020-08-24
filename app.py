from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello world!"

@app.route("/")
def index():
    return "Welcome to flask app"

if __name__ == "__main__":
    app.run(port=5000)
