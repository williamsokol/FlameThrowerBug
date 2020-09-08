"""
William Sokol 9/7/2020

This is a Recreation of the FlameThrowerBug
game I made in Scratch
"""

#import libaraies
import pygame
import random
import math
import sys

pygame.init()

#declare variables
WIDTH = 478
HEIGHT = 300

FRAMERATE = 60

BUGWIDTH = 60
BUGHEIGHT = 50
SPEED = 2

BALLOONWIDTH = 32
BALLOONHEIGHT = 60

FLAMEWIDTH = 48
FLAMEHEIGHT = 30

i = 0
playerX= 100
playerY= 100
slope=[1]
bullets = []
shooting = False
#declare classes
class Flame:
    SPEED = 3
    
    def __init__(self,x,y,angle,slopeX,slopeY):
        self.x = x
        self.y = y
        self.slopeX = slopeX
        self.slopeY = slopeY
        self.angle = angle
        self.img = pygame.transform.rotate(flame,angle)
        self.vels = moving(self.slopeX,self.slopeY,self.SPEED)

    def checkCollision(self):
        if(self.x + flame.get_width() >= balloonObj.x and
           self.x <= balloonObj.x + balloon.get_width()and
           self.y + flame.get_height() >= balloonObj.y and
           self.y <= balloonObj.y + balloon.get_height()):

            balloonObj.popped()
            pygame.mixer.Sound.play(pop_sound)

        self.border = borderCheck(self.x,self.y)
        if self.border == True:
            #print("yep")
            del self

    def update(self):
        self.checkCollision()
        self.x -= self.vels[0]
        self.y -= self.vels[1]
        screen.blit(self.img,(round(self.x),round(self.y)))
class Balloon:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width  = balloon.get_width()
        self.height = balloon.get_height()

    def popped(self):
        self.x = random.randint(1,WIDTH-balloon.get_width())
        self.y = random.randint(1,HEIGHT-balloon.get_height())
        
    def update(self):
        screen.blit(balloon,(self.x,self.y))
def moving(slopeX,slopeY,speed):
    
    if(abs(slopeX) > abs(slopeY)):
        vx = math.copysign(speed,slopeX)
        a = abs(slopeX/speed)
        vy = slopeY/a
    else:
        vy = math.copysign(speed,slopeY)
        a = abs(slopeY/speed)
        vx = slopeX/a
        
    return vx,vy
def borderCheck(x,y):
    if(x > WIDTH or
       x < 0 or
       y > HEIGHT or
       y < 0):
        return True

def update_fps():
	fps = str( int(clock.get_fps()))
	fps_text = font.render("fps: "+fps, 1, pygame.Color("black"))
	return fps_text
#draw the scenario
screen = pygame.display.set_mode((WIDTH,HEIGHT))

backGround  = pygame.image.load("BackGround.png")
backGround = pygame.transform.scale(backGround,(WIDTH,HEIGHT))

bug         = pygame.image.load("Bug.png")
bug = pygame.transform.scale(bug,(BUGWIDTH,BUGHEIGHT))
bug2 = pygame.transform.scale(bug,(BUGWIDTH,BUGHEIGHT))


balloon     = pygame.image.load("Balloon.png")
balloon = pygame.transform.scale(balloon,(BALLOONWIDTH,BALLOONHEIGHT))
pop_sound = pygame.mixer.Sound("Pop.wav")


flame       = pygame.image.load("Flame.png")
flame = pygame.transform.scale(flame,(FLAMEWIDTH,FLAMEHEIGHT))

centerX = round(playerX- bug.get_width()/2)
centerY = round(playerY- bug.get_height()/2)

balloonObj = Balloon(random.randint(1,WIDTH-balloon.get_width()),random.randint(1,HEIGHT-balloon.get_height()))

pygame.display.flip()

font = pygame.font.SysFont("Arialms", 18)

clock = pygame.time.Clock()
#game loop
while True:

    #input handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                pygame.quit()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
            slope.insert(0, playerX - mousePos[0])
            slope.insert(1, playerY - mousePos[1])
            angle= round(math.degrees(math.atan2(slope[0], slope[1]))+90)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            shooting = True
            
        if event.type == pygame.MOUSEBUTTONUP:
            shooting = False

    #shoot flames
    if(slope[0] != 0 and slope[1] != 0):
        if shooting == True:
            bullets.insert(i,Flame(centerX,centerY,angle,slope[0],slope[1]))
            
        else:
            vels = moving(slope[0],slope[1],SPEED)
            border = borderCheck(playerX - vels[0],playerY - vels[1])
            if(border != True):
                # movement          note:[0] is x and [1] is y
                
                
                
                playerX -= vels[0]
                playerY -= vels[1]
            else:
               pass
    bug2 = pygame.transform.rotate(bug,angle)

    
    # refresh sprites (be sure to put in after background)
    screen.blit(backGround,(0,0))

    for bull in bullets:
        bull.update()
    balloonObj.update()
    centerX = round(playerX- bug2.get_width()/2)
    centerY = round(playerY-bug2.get_height()/2)
    screen.blit(bug2,(centerX,centerY))
    screen.blit(update_fps(),(10,0))
    pygame.display.flip()

    clock.tick(FRAMERATE)
    
