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
black  = pygame.Color(  0,  0,  0)

def mainLoop():
	pygame.display.flip()
	screen.fill(black)
	clock.tick(60)
	
while True:
	mainLoop()


