#Bouncing Algorithm - www.101computing.net/bouncing-algorithm/
from processing import *
from random import randint

WIDTH=300
HEIGHT=300
x = 30
y = 30
vx = randint(-10,10)
vy = randint(-10,10)
delay = 5
radius = 30

def setup():
    strokeWeight(3)
    frameRate(20)
    size(300,300)

def moveBall():    
    global x,y,vx,vy, WIDTH, HEIGHT
    background(200,200,200)
    fill(112,48,160)
    stroke(255,255,255)
    
    #Bouncing Algorithm when the Ball hit the edge of the canvas
    x=x+vx
    y=y+vy
    if x<0 or x>WIDTH:
        vx=-vx
        x=x+vx
    if y<0 or y>HEIGHT:
        vy=-vy
        y=y+vy
        
    #Draw ball  
    ellipse(x,y,30,30)
    

draw = moveBall
run() #This function from the processing library will call the setup() function once and then the moveBall() function every x ms to create the frame based animation.
