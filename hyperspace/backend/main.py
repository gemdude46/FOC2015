from flask import Flask
from flask import request
class MyServer(Flask):

    def __init__(self, *args, **kwargs):
            super(MyServer, self).__init__(*args, **kwargs)

            #instanciate your variables here
            self.v = {}

app = MyServer(__name__)

@app.route("/")
def index():
    return "This is the Index, why are you here?"


if __name__ == "__main__":
    app.run()
