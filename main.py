import pygame
from pygame.locals import *
from board import ChessBoard
from teams import blacks
from teams import whites
pygame.init()


# pygame.draw.rect(surface, color, (x,y,width,height)) width and height is recommended to be integer type
# pygame.draw.circle(screen, color, (x,y), radius, thickness)
# pygame.Rect.inflate(-10,-10) makes the rectangle small
# pygame.mouse.get_pos()
# image = pygame.image.load(r'C:\Users\user\Pictures\geek.jpg') 
# screen.blit(image, (x,y))   
# pygame.transform.scale(img, (1280, 720))
# rect = picture.get_rect()


SCREEN_WIDTH = 680
SCREEN_HEIGHT = 680
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

COLORS = {"green":(0,255,0),"blue":(0,0,255),"red":(255,0,0),"black":(0,0,0),"white":(255,255,255),
          "golden":(255,215,0)}

KEYS = {"UP":pygame.K_UP,"DOWN":pygame.K_DOWN,"LEFT":pygame.K_LEFT,"RIGHT":pygame.K_RIGHT}

my_chess_board = ChessBoard(screen,SCREEN_WIDTH)

myteam = blacks.BlackTeam(surface=screen,board=my_chess_board)
myteam.DrawAllPlayers()
myteam2 = whites.WhiteTeam(surface=screen,board=my_chess_board)
myteam2.DrawAllPlayers()

def GamePlay():
    running = True    
    while running:

        for event in pygame.event.get():
            if event.type==QUIT:
                running = False

            if event.type==pygame.KEYDOWN:
                if ((event.key==KEYS["UP"] or event.key==KEYS["DOWN"] or event.key==KEYS["LEFT"] or event.key==KEYS["RIGHT"]) and len(my_chess_board.squares_with_border)==0):
                    my_chess_board.DrawBorder(cell="c1-r8",border_color=COLORS["red"])

                if event.key== KEYS["UP"] and len(my_chess_board.squares_with_border)==1: # KEY : 273
                    my_chess_board.MoveBorderOnArrow(arrow="u",border_color=COLORS["red"])

                if event.key== KEYS["DOWN"] and len(my_chess_board.squares_with_border)==1: # KEY : 274 
                    my_chess_board.MoveBorderOnArrow(arrow="d",border_color=COLORS["red"])

                if event.key== KEYS["RIGHT"] and len(my_chess_board.squares_with_border)==1: # KEY : 275
                    my_chess_board.MoveBorderOnArrow(arrow="r",border_color=COLORS["red"])

                if event.key== KEYS["LEFT"] and len(my_chess_board.squares_with_border)==1: # KEY : 276
                    my_chess_board.MoveBorderOnArrow(arrow="l",border_color=COLORS["red"])

            if event.type==pygame.MOUSEBUTTONDOWN:
                click_x , click_y = pygame.mouse.get_pos()
                myteam.SetPlayerToMove(x=click_x,y=click_y)
                myteam2.SetPlayerToMove(x=click_x,y=click_y)

             
        pygame.display.update()

GamePlay()
