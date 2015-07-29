import pygame, sys, urllib, easygui, math
from pygame.locals import *



class Station:
    def __init__(self,x,y):
        self.x=x
        self.y=y

stations = [Station(-300,0)]

ip="http://localhost:5000"

hp=100
dosh=0
fuel=0
eng=10
ship=0
pos=(0,0)

theta=math.pi

def updateData():
    global hp,dosh,fuel,eng,ship,pos,cursor
    d = urllib.urlopen(ip+"/data/?username="+login[0]).read().split()
    #print d
    hp=int(d[0])
    dosh=int(d[1])
    fuel=int(d[2])
    eng=int(d[3])
    ship=int(d[4])
    opos=pos
    pos=(int(d[5]),int(d[6]))
    cursor=(cursor[0]+(opos[0]-pos[0]),cursor[1]+(opos[1]-pos[1]))






try:

    login=easygui.multpasswordbox("Login","Hyperspace",["Username","Password"])

    cursor = (600,(768/2))

    screen = pygame.display.set_mode((1200,768),0*FULLSCREEN)

    heart=pygame.image.load("images/hp.png").convert_alpha()
    bolt=pygame.image.load("images/energy.png").convert_alpha()
    cs=pygame.image.load("images/cursor.png").convert_alpha()
    
    ships_i=[pygame.image.load("images/ship1.png").convert_alpha()]
    
    stations_i=[pygame.transform.scale(pygame.image.load("images/station1.png").convert_alpha(),(256,256))]
    
    rotship=pygame.transform.rotate(ships_i[ship],math.degrees(theta+math.pi))
    
    while True:
        
        updateData()
        #print cursor
        for event in pygame.event.get():
            if event.type == QUIT:
                raise KeyboardInterrupt
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] < 1164:
                urllib.urlopen(ip+"/setdst/?username="+login[0]+"&rpos="+str(event.pos[0]-600)+"_"+str(event.pos[1]-(768/2)))
                theta=math.atan2(event.pos[0]-600,event.pos[1]-(768/2))
                cursor=event.pos
        kp = pygame.key.get_pressed()
        if kp[K_q]:
            sys.exit()
        screen.fill((0,0,0))
        screen.blit(heart,(5,5))
        pygame.draw.line(screen,(255,0,0),(32,14),(32+(hp*4),14),2)
        screen.blit(bolt,(5,26))
        pygame.draw.line(screen,(255,255,0),(32,34),(32+int(eng*4/10000.),34),2)
        
        
        screen.blit(rotship,(600-rotship.get_width()/2,(768/2)-rotship.get_height()/2))
        
        for station in stations:
            screen.blit(stations_i[0],(station.x-pos[0]+600,station.y-pos[1]+(768/2)))
        
        if (cursor[0]-600)**2+(cursor[1]-(768/2))**2 > 32:
            screen.blit(cs,(cursor[0]-8,cursor[1]-8))
            rotship=pygame.transform.rotate(ships_i[ship],math.degrees(theta+math.pi))
        
        
        pygame.display.update()
        
    
except KeyboardInterrupt:
    raise
except SystemError:
    raise
except:
    easygui.exceptionbox()
