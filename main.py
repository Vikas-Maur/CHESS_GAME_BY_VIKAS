import pygame
from pygame.locals import *
from board import ChessBoard

pygame.init()

# pygame.draw.rect(surface, color, (x,y,width,height)) width and height is recommended to be integer type
# pygame.draw.circle(screen, color, (x,y), radius, thickness)

SCREEN_WIDTH = 680
SCREEN_HEIGHT = 680
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

my_chess_board = ChessBoard(screen,SCREEN_WIDTH)

def GamePlay():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type==QUIT:
                running = False
        pygame.display.update()

GamePlay()