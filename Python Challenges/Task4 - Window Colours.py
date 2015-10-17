#Created by Joseph Brason
#Key detection and changing screen colour

import pygame, sys
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

screenX = 1200
screenY = 720
screen = pygame.display.set_mode((screenX ,screenY))

windowTitle = 'Changing Colours'
pygame.display.set_caption(windowTitle)

<<<<<<< HEAD
#COLOURS 
=======
#COLOURS
>>>>>>> 52517930ca46b720e71596d90322d966379b9a8d
black  = pygame.Color(  0,  0,  0)
grey   = pygame.Color(150,150,150)
white  = pygame.Color(255,255,255)
red    = pygame.Color(255,  0,  0)
green  = pygame.Color(  0,255,  0)
blue   = pygame.Color(  0,  0,255)

#VARIABLES
screenColour = black

def displayText(text, colour, posX, posY): #Ignore this function for now
    font = pygame.font.Font('freesansbold.ttf', 72)
    surf = font.render(text, True, colour)
    rect = surf.get_rect()
    rect.midtop = (posX, posY)
    screen.blit(surf, rect)

def keyDetection():
    global screenColour
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            elif event.key == ord('w'):
                screenColour = white
            elif event.key == ord('r'):
                screenColour = red
            elif event.key == ord('g'):
                screenColour = green
            elif event.key == ord('b'):
                screenColour = blue
                

def mainLoop():
    keyDetection()
    displayText("PRESS W, R, G or B", grey, screenX / 2, screenY / 2 - 100) #Ignore these too
    displayText("TO CHANGE COLOUR", grey, screenX / 2, screenY / 2) #Displaying text will be covered in the future :D
    pygame.display.flip()
    screen.fill(screenColour)
    clock.tick(60)

    
while True:
    mainLoop()
