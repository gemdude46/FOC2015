from flask import Flask
from flask import request
from flask import redirect
from math import *
import hashlib, os, easygui, json
class MyServer(Flask):

    def __init__(self, *args, **kwargs):
            super(MyServer, self).__init__(*args, **kwargs)

            #instanciate your variables here
            self.v = {"users":{"test":User("test","")}}

class Planet:
    def __init__(self,a,t,f):
        self.a = a
        self.t = t
        self.file = f

class User:
    def __init__(self,user,pswd):
        self.u=user
        self.p=pswd
        self.hp=100
        self.dosh=10000
        self.fuel=1000
        self.eng=1000000
        self.x=0
        self.y=0
        self.ship=0
        self.dest=(0,0)
    
def newuser(u,p):
    return User(u,hashlib.sha224(u+":"+p).hexdigest())

app = MyServer(__name__)

@app.route("/")
def index():
    return """
    
    
    <a href="register">Register</a><br>
    <a href="login">Login</a>
    
    
    
    """





























def update():
    #try:
    for user in app.v["users"].values():
        #print user.dest
        if (user.x-user.dest[0])**2+(user.y-user.dest[1])**2 > 25:
            user.x+=int(sin(atan2(user.dest[0]-user.x,user.dest[1]-user.y))*5)
            user.y+=int(cos(atan2(user.dest[0]-user.x,user.dest[1]-user.y))*5)
    

@app.route("/data/")
def data():
    
    try:
        update()
        u=request.args.get("username")
        return str(app.v["users"][u].hp)+" "+str(app.v["users"][u].dosh)+" "+str(app.v["users"][u].fuel)+" "+str(app.v["users"][u].eng)+" "+str(app.v["users"][u].ship)+" "+str(app.v["users"][u].x)+" "+str(app.v["users"][u].y)
    except:
        easygui.exceptionbox()


@app.route("/setdst/")
def setdst():
    u=request.args.get("username")
    p=request.args.get("rpos").split("_")
    app.v["users"][u].dest=(int(p[0])+app.v["users"][u].x,int(p[1])+app.v["users"][u].y)
    return ""



app.v["planets_j"] = json.loads(open("planets.json","r").read())

app.v["planets"] = [Planet(1,pi/2,"images/earth.png")]























































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
