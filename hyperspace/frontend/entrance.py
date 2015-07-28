import pygame, sys, urllib, easygui
from pygame.locals import *

ip="http://localhost:5000"

hp=100
dosh=0
fuel=0
eng=10

def updateData():
    d = urllib.urlopen(ip+"/data/?username="+login[0]).read().split()
    hp=d[0]
    dosh=d[1]
    fuel=d[2]
    eng=d[3]







try:

    login=easygui.multpasswordbox("Login","Hyperspace",["Username","Password"])

    screen = pygame.display.set_mode((1200,768),FULLSCREEN)

    while True:
        updateData()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        kp = pygame.key.get_pressed()
        if kp[K_q]:
            sys.exit()
        screen.fill((0,0,0))
    
except:
    easygui.exceptionbox()
