from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def index():
    return "This is the Index, why are you here?"


if __name__ == "__main__":
    app.run()
