import pygame, sys
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 500
WINDOWHEIGHT = 500
BoxSize = 25
Gap = 5
ROW = 30
COL = 30

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
BLACK    = (  0,   0,   0)

UNVISITED = RED
DEAD = GRAY
ALIVE = GREEN

BackgroundColor = BLACK

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH , WINDOWHEIGHT))
    DISPLAYSURF.fill(BackgroundColor)
    drawMap()

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()

def drawMap():
    for row in range(ROW):
        for col in range(COL):
            left, top = (Gap + row*(Gap + BoxSize), Gap + col*(Gap + BoxSize))
            if left + BoxSize < WINDOWWIDTH and top + BoxSize < WINDOWHEIGHT:
                box = pygame.draw.rect(DISPLAYSURF, PURPLE, (left, top, BoxSize, BoxSize))
    return None



if __name__ == '__main__':
    main()