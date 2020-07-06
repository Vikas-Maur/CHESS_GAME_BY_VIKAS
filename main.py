import pygame
from pygame.locals import *
from board import ChessBoard

pygame.init()

# pygame.draw.rect(surface, color, (x,y,width,height)) width and height is recommended to be integer type
# pygame.draw.circle(screen, color, (x,y), radius, thickness)
# pygame.Rect.inflate(-10,-10) makes the rectangle small

SCREEN_WIDTH = 680
SCREEN_HEIGHT = 680
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

COLORS = {"green":(0,255,0),"blue":(0,0,255),"red":(255,0,0),"black":(0,0,0),"white":(255,255,255),
          "golden":(255,215,0)}

my_chess_board = ChessBoard(screen,SCREEN_WIDTH)
def GamePlay():
    running = True
    
    while running:
        # click  = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==QUIT:
                running = False

            if event.type==pygame.MOUSEBUTTONDOWN:
                click_x , click_y = pygame.mouse.get_pos()
                cell_clicked = my_chess_board.GiveCell(x=click_x,y=click_y)
                if my_chess_board.squares_with_border[cell_clicked]!=True:
                    my_chess_board.DrawBorder(cell=cell_clicked,border_color=COLORS["red"])
                else:
                    my_chess_board.RemoveBorder(cell_clicked)

        pygame.display.update()

GamePlay()
