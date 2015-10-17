#Created by Joseph Brason
#Drawing Shapes

import pygame, sys
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

screenX = 1200
screenY = 720
screen = pygame.display.set_mode((screenX ,screenY))

windowTitle = "Blank Pygame window"
pygame.display.set_caption(windowTitle)

#COLOURS
black  = pygame.Color(  0,  0,  0)
red    = pygame.Color(255,  0,  0)
green  = pygame.Color(  0,255,  0)
blue   = pygame.Color(  0,  0,255)

def keyDetection():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

def drawRectangle(): #Generally, it's best to use functions in the loop, rather than just placing this in the mainLoop
    rectanglePosX = 150
    rectanglePosY = 200
    rectangleSizeX = 300
    rectangleSizeY = 200
    rectangleWidth = 0 #0 is filled
    pygame.draw.rect(screen, red, (rectanglePosX, rectanglePosY, rectangleSizeX, rectangleSizeY), rectangleWidth) 
    #You can just type in raw values into the function, you don't have to use variables

def drawCircle():
    circleColour = green
    circlePosX = 200
    circlePosY = 100
    circleRadius = 50
    circleWidth = 15 #0 is filled
    pygame.draw.circle(screen, circleColour, (circlePosX, circlePosY), circleRadius, circleWidth)
    #(surface you are drawing to, Center point (x,y), radius of the circle, width of circle)

def drawLine():
    pygame.draw.line(screen, blue, (500,600), (600,500), 10)

def mainLoop():
    keyDetection()
    drawRectangle()
    drawCircle()
    drawLine()

    pygame.display.flip()
    screen.fill(black)
    clock.tick(60)

    
while True:
    mainLoop()
