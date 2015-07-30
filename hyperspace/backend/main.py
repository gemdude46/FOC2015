from flask import Flask
from flask import request
from flask import redirect
from math import *
import os, easygui, json
class MyServer(Flask):

    def __init__(self, *args, **kwargs):
            super(MyServer, self).__init__(*args, **kwargs)

            #instanciate your variables here
            self.v = {"users":{"Alice":User("Alice",""),"Bob":User("Bob","")}}

class Planet:
    def __init__(self,a,t,f,g,d,tmp,ts):
        self.a = a
        self.t = t
        self.file = f
        self.g=g
        self.d=d
        self.tmp=tmp
        self.ts=ts
        self.s=ts
    
    def x(self):
        return self.a*sin(self.t)
    def y(self):
        return self.a*cos(self.t)

class User:
    def __init__(self,user,pswd):
        self.u=user
        self.p=pswd
        self.hp=100
        self.dosh=10000
        self.fuel=1000
        self.eng=1000000
        self.x=149597971700
        self.y=0
        self.ship=0
        self.dest=(149597971700,0)
    
class Station:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
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
    
    
    u=request.args.get("username")
        
    if request.args.get("space") == "1" and app.v["users"][u].eng >= 20:
        app.v["users"][u].eng -= 20
        t=float(request.args.get("t"))
        app.v["users"][u].x+=int(sin(t)*200000)
        app.v["users"][u].y+=int(cos(t)*200000)
    update()
    return str(app.v["users"][u].hp)+" "+str(app.v["users"][u].dosh)+" "+str(app.v["users"][u].fuel)+" "+str(app.v["users"][u].eng)+" "+str(app.v["users"][u].ship)+" "+str(app.v["users"][u].x)+" "+str(app.v["users"][u].y)
    

@app.route("/setdst/")
def setdst():
    u=request.args.get("username")
    p=request.args.get("rpos").split("_")
    app.v["users"][u].dest=(int(p[0])+app.v["users"][u].x,int(p[1])+app.v["users"][u].y)
    return ""


@app.route("/planets/")
def getplanets():
    
    try:
        s=""
        for planet in app.v["planets"]:
            s += " "+str(planet.x())+"|"+str(planet.y())+"|"+planet.file+"|"+str(planet.g)+"|"+str(planet.d)+"|"+planet.tmp
        
        return s
    except:
        easygui.exceptionbox()
        
@app.route("/stations/")
def getstations():
    u=request.args.get("username")
    s=""
    x=int(app.v["users"][u].x)
    y=int(app.v["users"][u].y)
    for station in app.v["stations"]:
        if ((station.x-x)**2 + (station.y-y)**2)**0.5 < 14959797170:
            s+=" "+str(station.x)+"|"+str(station.y)
    return s
        
@app.route("/scan/")
def scanplanet():
    u=request.args.get("username")
    p=int(request.args.get("pid"))
    x=int(app.v["users"][u].x)
    y=int(app.v["users"][u].y)
    px=app.v["planets"][p].x()*149597870700
    py=app.v["planets"][p].y()*149597870700
    d=((x-px)**2+(y-py)**2)**0.5
    if d > 30000000:
        return ""
    s = (1 - d / 30000000) * app.v["planets"][p].s / 2
    app.v["planets"][p].s-=s
    app.v["users"][u].dosh+=int(s)
    
        
        
app.v["planets_j"] = json.loads(open("planets.json","r").read())

app.v["planets"] = [Planet(1,pi/2,"images/earth.png",9.81,24,"hot",1000)]
app.v["stations"] = [Station(149597971700-300,0)]























































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
