from flask import Flask
from flask import request
from flask import redirect
import hashlib, os
class MyServer(Flask):

    def __init__(self, *args, **kwargs):
            super(MyServer, self).__init__(*args, **kwargs)

            #instanciate your variables here
            self.v = {"users":[]}

class User:
    def __init__(self,user,pswd):
        self.u=user
        self.p=pswd
    
def newuser(u,p):
    return User(u,hashlib.sha224(u+":"+p).hexdigest())

app = MyServer(__name__)

@app.route("/")
def index():
    return """
    
    
    <a href="register">Register</a><br>
    <a href="login">Login</a>
    
    
    
    """



































































@app.route("/register/")
def register():
    try:
        u=request.args.get("usr")
        p=request.args.get("psk")
        if u==None or p==None :
            raise KeyError
        app.v["users"][u]=newuser(u,p)
        return redirect("login")
    except KeyError:
        return """
        
        Register
        
        <form>
        Username: <input type=text name=usr></input><br>
        Password: <input type=text name=psk></input>
        <input type=submit></input>
        </form>
        
        
        """
        
@app.route("/login/")
def login():
    return """
        
        Login
        
        <form action= method=POST>
        Username: <input type=text name=usr></input><br>
        Password: <input type=text name=psk></input>
        <input type=submit></input>
        </form>
        
        
        """

@app.route("/getsid/")
def getsid():
    sid=os.urandom(64)
    return redirect("game?sid="+sid)

@app.route("/game/")
def game():
    return """
    
    
    
    <head><title>"""+request.args.get("usr")+"""</title>
<style>
html, body {
    width:  100%;
    height: 100%;
    margin: 0px;
}
</style>
</head>
<body>
<canvas id=c>
</canvas>
<img src="../static/ship1.png" id=ship1 style=position:absolute;top:0px;>
<script>

var c = document.getElementById("c");
var ctx = c.getContext("2d");

function draw() {
    ctx.canvas.width  = window.innerWidth;
    ctx.canvas.height = window.innerHeight;
    ctx.rect(0,0,window.innerWidth,window.innerHeight);
    ctx.fillStyle="black";
    ctx.fill();
    ctx.drawImage(document.getElementById("ship1"),window.innerWidth/2-32,window.innerHeight/2-32);
}

setInterval(draw,50);
</script>
</body>
    
    
    
    
    
    """

if __name__ == "__main__":
    app.run()
