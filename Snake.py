#!/usr/bin/env python
# Snake

import pygame, sys, time, random
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
playSurface = pygame.display.set_mode((640,480))
pygame.display.set_caption('Snake')

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

snakePosition = [100,100]
snakeSegments = [[100, 100],[80, 100],[60, 100]]
raspberryPosition = [300,300]
raspberrySpawned = 1
direction = 'right'
changeDirection = direction

def gameOver():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 72)
    gameOverSurf = gameOverFont.render('Game Over', True, grey)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320, 10)
    playSurface.blit(gameOverSurf, gameOverRect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()
    
def keyDetection():
    global changeDirection
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            if event.key == K_RIGHT or event.key == ord('d') or event.key == ord('x'):
                changeDirection = 'right'   
            if event.key == K_LEFT or event.key == ord('a') or event.key == ord('z'):
                changeDirection = 'left'
            if event.key == K_UP or event.key == ord('w') or event.key == ord(';'):
                changeDirection = 'up'  
            if event.key == K_DOWN or event.key == ord('s') or event.key == ord('.'):
                changeDirection = 'down'
                
def directionChange():
    global direction
    if changeDirection == 'right' and not direction == 'left':
        direction = changeDirection
    if changeDirection == 'left' and not direction == 'right':
        direction = changeDirection
    if changeDirection == 'down' and not direction == 'up':
        direction = changeDirection
    if changeDirection == 'up' and not direction == 'down':
        direction = changeDirection
    if direction == 'right':
        snakePosition[0] += 20
    if direction == 'left':
        snakePosition[0] -= 20
    if direction == 'up':
        snakePosition[1] -= 20
    if direction == 'down':
        snakePosition[1] += 20      
        
def listsUpdate():
    snakeSegments.insert(0,list(snakePosition))
    global raspberryPosition, raspberrySpawned
    if snakePosition[0] == raspberryPosition[0] and snakePosition[1] == raspberryPosition[1]:
        raspberrySpawned = 0
    else:
        snakeSegments.pop()
    if raspberrySpawned == 0:
        x = random.randrange(1, 32)
        y = random.randrange(1, 24)
        raspberryPosition = [int(x*20), int(y*20)]
    raspberrySpawned = 1
        
def drawScreen():
    for position in snakeSegments:
        pygame.draw.rect(playSurface, white, Rect(position[0], position[1],20,20))
    pygame.draw.rect(playSurface,red, Rect(raspberryPosition[0], raspberryPosition[1],20,20))
    
def gameDetection():
    if snakePosition[0] > 620 or snakePosition[0] < 0:
        gameOver()
    if snakePosition[1] > 460 or snakePosition[1] < 0:
        gameOver()
    for snakeBody in snakeSegments[1:]:
        if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
            gameOver()

while True:
    keyDetection()
    directionChange()
    listsUpdate()
    drawScreen()
    pygame.display.flip()
    gameDetection()
    playSurface.fill(black)
    fpsClock.tick(15)

    
