import pygame, sys
import numpy as np
from pygame.locals import *

FPS = 30

ROW = 10
COL = 20
WINDOWWIDTH = 850
WINDOWHEIGHT = 700
GRIDHEIGHT = 500

initGapLR = 60
initGapTB =  60
BoxSize = (GRIDHEIGHT - 2*initGapTB)/(ROW + (ROW-1)/3) if (GRIDHEIGHT - 2*initGapTB)/(ROW + (ROW-1)/3) < (WINDOWWIDTH - 2*initGapLR)/(COL + (COL-1)/3) else (WINDOWWIDTH - 2*initGapLR)/(COL + (COL-1)/3)
Gap = BoxSize/3

state = np.zeros((ROW, COL))
pos = np.zeros(( ROW, COL, 2))
DEAD = 1
ALIVE = 2
EXPLORE = 3

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


pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH , WINDOWHEIGHT))
DISPLAYSURF.fill(BackgroundColor)
FPSCLOCK = pygame.time.Clock()



def main():
    global FPSCLOCK, DISPLAYSURF
    StartChosen = False
    EndChosen = False
    WallChosen = False
    
    
    drawMap()
    displayText("Please Select Starting Position: ")
    prevSpot = None
    while True:
        

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == MOUSEBUTTONDOWN:
                spotx, spoty = pygame.mouse.get_pos()
                
                if StartChosen == False:
                    if prevSpot == None:
                        changeColor(spotx, spoty, GREEN)
                        prevSpot = (spotx, spoty)
                    else:
                        changeColor(prevSpot[0], prevSpot[1], PURPLE)
                        changeColor(spotx, spoty, GREEN)
                        prevSpot = (spotx, spoty)

                elif StartChosen == True and EndChosen == False:
                    if prevSpot == None:
                        changeColor(spotx, spoty, RED)
                        prevSpot = (spotx, spoty)
                    else:
                        changeColor(prevSpot[0], prevSpot[1], PURPLE)
                        changeColor(spotx, spoty, RED)
                        prevSpot = (spotx, spoty)
                elif StartChosen == True and EndChosen == True:
                    changeState(spotx, spoty)


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if StartChosen == False:
                        StartChosen = True
                        prevSpot = None
                        displayText("Please Select Ending Position: ")
                    elif StartChosen == True:
                        EndChosen = True
                        displayText("Please Select Walls: ")
                    else:
                        EndChosen == True
                    

            pygame.display.update()

def drawMap():
    for row in range(ROW):
        for col in range(COL):
            left, top = (initGapLR + Gap + col*(Gap + BoxSize),  (initGapTB + WINDOWHEIGHT - GRIDHEIGHT  + (Gap + row*(Gap + BoxSize))))
            pos[row][col] = (left, top)
            if left + BoxSize < WINDOWWIDTH and top + BoxSize < WINDOWHEIGHT:
                pygame.draw.rect(DISPLAYSURF, PURPLE, (left, top, BoxSize, BoxSize))

def changeColor(x, y, color):
    for row in range(ROW):
        for col in range(COL):
            if x > pos[row][col][0] and x < (pos[row][col][0] + BoxSize) and y > pos[row][col][1] and y < (pos[row][col][1] + BoxSize):
                # print(pos[row][col][1])
                pygame.draw.rect(DISPLAYSURF, color, (pos[row][col][0], pos[row][col][1], BoxSize, BoxSize))

def displayText(text):
    pygame.draw.rect(DISPLAYSURF, WHITE, [20, 20, 800, 100 ])
    font = pygame.font.SysFont(None,70)
    Text = font.render(text, True, BLACK)
    DISPLAYSURF.blit(Text, [30,50])

def changeState(x, y):
    for row in range(ROW):
        for col in range(COL):
            if x > pos[row][col][0] and x < (pos[row][col][0] + BoxSize) and y > pos[row][col][1] and y < (pos[row][col][1] + BoxSize):
                if state[row][col] == 0:
                    state[row][col] = -1
                    pygame.draw.rect(DISPLAYSURF, GRAY, (pos[row][col][0], pos[row][col][1], BoxSize, BoxSize))
                else:
                    state[row][col] = 0
                    pygame.draw.rect(DISPLAYSURF, PURPLE, (pos[row][col][0], pos[row][col][1], BoxSize, BoxSize))
                

if __name__ == '__main__':
    main() 