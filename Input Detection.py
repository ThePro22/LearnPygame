#Created by Joseph Brason
#Blank Pygame 

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
red    = pygame.Color(255,  0,  0)
orange = pygame.Color(255,130,  0)
yellow = pygame.Color(255,255,  0)
green  = pygame.Color(  0,255,  0)
cyan   = pygame.Color(  0,255,255)
blue   = pygame.Color(  0,  0,255)
purple = pygame.Color(130,  0,255)
pink   = pygame.Color(255,  0,255)
black  = pygame.Color(  0,  0,  0)
white  = pygame.Color(255,255,255)
grey   = pygame.Color(150,150,150)

def keyDetection():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            if event.key == K_RIGHT:
                print("Right arrow pressed")
            elif event.key == K_LEFT:
                print("Left arrow pressed")
            elif event.key == K_DOWN:
                print("Down arrow pressed")
            elif event.key == K_UP:
                print("Up arrow pressed")
        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            if event.key == K_RIGHT:
                print("Right arrow released")
            elif event.key == K_LEFT:
                print("Left arrow released")
            elif event.key == K_DOWN:
                print("Down arrow released")
            elif event.key == K_UP:
                print("Up arrow released")

def mouseDetection():
    mouseX, mouseY = pygame.mouse.get_pos()
    mouse1, mouse2, mouse3 = pygame.mouse.get_pressed()

def mainLoop():
    keyDetection()
    mouseDetection()
    pygame.display.flip()
    screen.fill(black)
    clock.tick(60)

    
while True:
    mainLoop()
