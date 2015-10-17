#Created by Joseph Brason
#Pong game

import pygame, sys, time, random
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

screenX = 700
screenY = 500
screen = pygame.display.set_mode((screenX ,screenY))

windowTitle = "Pong"
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

#Sprites
classList = []
all_sprites  = pygame.sprite.Group()

#OTHERS
up = False
down = False
w = False
s = False
edgeGap = 5
arenaWidth = 2

blueScore = 0
redScore = 0

class ball():

    def __init__(self, posX, posY, colour):

        self.posX = posX
        self.posY = posY 
        self.width = 10
        self.colour = colour
        self.changeX = 3
        self.changeY = 2

    def updateSelf(self):

        global blueScore, redScore

        pygame.draw.circle(screen, self.colour, (int(self.posX), int(self.posY)), self.width)

        self.top = self.posY - self.width
        self.left = self.posX - self.width
        self.bottom = self.posY + self.width
        self.right = self.posX + self.width

        if self.top <= 7:
            self.changeY = -self.changeY

        if self.bottom >= screenY-7:
            self.changeY = -self.changeY
        
        if self.changeX < 0:
            if self.posX < screenX // 2:
                self.colour = red
            if self.left <= redPlayer.width + 2 and self.left > 0:
                if self.posY - self.width >= redPlayer.top and self.posY - self.width <= redPlayer.bottom:   
                    self.changeX -= 0.5         
                    self.changeX = -self.changeX
                    self.changeY += (random.randrange(-51, 50) // 50)
                    print(self.changeY)
            if self.posX < 0:
                self.posX = screenX // 2
                self.posY = screenY // 2
                self.changeX = 5
                if random.randrange(0,2) == 1:
                    self.changeX = -self.changeX
                blueScore += 1


        if self.changeX > 0:
            if self.posX > screenX // 2:
                self.colour = blue
            if self.right >= screenX - (bluePlayer.width + 2) and self.right > 0:
                if self.posY - self.width >= bluePlayer.top and self.posY - self.width <= bluePlayer.bottom:  
                    self.changeX += 0.5             
                    self.changeX = -self.changeX
                    self.changeY += (random.randrange(-51, 50) // 50)
                    print(self.changeY)
            if self.posX > screenX:
                self.posX = screenX // 2
                self.changeX = 5
                self.posY = screenY // 2
                if random.randrange(0,2) == 1:
                    self.changeX = -self.changeX
                redScore += 1

        self.posX += self.changeX
        self.posY += self.changeY

class redPaddle():

    def __init__(self):

        self.posX = arenaWidth + edgeGap
        self.posY = screenY // 2
        self.height = 50
        self.width = 15
        self.top = self.posY - (self.height // 2)
        self.bottom = self.posY + (self.height // 2)

    def updateSelf(self):

        pygame.draw.rect(screen, red, (self.posX, self.posY, self.width, self.height)) 
        self.top = self.posY
        self.bottom = self.posY + self.height
        self.posY = mainBall.posY - mainBall.width - 10 

        if self.posY + self.height >= screenY - edgeGap - arenaWidth:
            self.posY = screenY - self.height - edgeGap - arenaWidth

class bluePaddle():

    def __init__(self):
        self.width = 15
        self.posX = screenX - (arenaWidth + edgeGap) - self.width
        self.posY = screenY // 2
        self.height = 50
        self.top = self.posY - (self.height // 2)
        self.bottom = self.posY + (self.height // 2)

    def updateSelf(self):

        pygame.draw.rect(screen, blue, (self.posX, self.posY, self.width, self.height)) 
        self.top = self.posY
        self.bottom = self.posY + self.height
        #self.posY = mainBall.posY - mainBall.width - 10   

        if self.posY + self.height > screenY + edgeGap + arenaWidth:
            self.posY = screenY - self.height - edgeGap - arenaWidth

redPlayer = redPaddle()
classList.append(redPlayer)

bluePlayer = bluePaddle()
classList.append(bluePlayer)

for x in range(2):
    mainBall = ball(screenX // 2, screenY // 2, red)
    classList.append(mainBall)


def keyDetection():
    global up, down, w, s

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            if event.key == K_UP:
                up = True                
            if event.key == K_DOWN:
                down = True
            if event.key == ord('w'):
                w = True
            if event.key == ord('s'):
                s = True
        if event.type == KEYUP:
            if event.key == K_UP:
                up = False
            if event.key == K_DOWN:
                down = False
            if event.key == ord('w'):
                w = False
            if event.key == ord('s'):
                s = False

    if up:
        if bluePlayer.top > edgeGap + arenaWidth: 
            bluePlayer.posY -= 5
    if down:
        if not bluePlayer.bottom >= screenY - edgeGap - arenaWidth:
            bluePlayer.posY += 5
    if w:
        if redPlayer.top > edgeGap + arenaWidth:
            redPlayer.posY -= 5
    if s:
        if not redPlayer.bottom >= screenY - edgeGap - arenaWidth:
            redPlayer.posY += 5

def updateListObjs():
    for thing in classList:
        thing.updateSelf()

def drawArena():
    pygame.draw.rect(screen, white, (edgeGap, edgeGap, screenX - 10, screenY - 10), arenaWidth) 
    pygame.draw.line(screen, white, (screenX // 2, edgeGap),(screenX // 2, screenY - edgeGap))

def displayText(text, colour, size, posX, posY):
    font = pygame.font.Font('freesansbold.ttf', size)
    surf = font.render(text, True, colour)
    rect = surf.get_rect()
    rect.midtop = (posX, posY)
    screen.blit(surf, rect)

def showScore():
    displayText(str(redScore), white, 72, screenX // 3 , screenY // 5)
    displayText(str(blueScore), white, 72, screenX // 1.5, screenY // 5)

def gameOver():
    if redScore >= 20 or blueScore >= 20:
        if redScore > blueScore:
            winner = "RED"
        else:
            winner = "BLUE"

        def drawArena():
            pygame.draw.rect(screen, white, (edgeGap, edgeGap, screenX - 10, screenY - 10), arenaWidth) 

        def keyDetection():
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.event.post(pygame.event.Event(QUIT))

        while True:
            keyDetection()
            displayText((winner + " WINS!"), white, 50, screenX // 2, screenY // 2)
            drawArena()
            pygame.display.flip()
            screen.fill(black)
            clock.tick(60)

def mainLoop():
    keyDetection()
    updateListObjs()
    drawArena()
    showScore()
    gameOver()
    pygame.display.flip()
    screen.fill(black)
    clock.tick(60)
    
while True:
    mainLoop()
