import pygame
from pygame.locals import *

class ChessBoard:
    def __init__(self,surface,surface_side):
        self.square_side = int(surface_side/8)
        self.num_rows = 8
        self.num_columns = 8
        self.square_color = None
        self.squares = {}

        self.white = (255,255,255)
        self.black = (0,0,0)
        self.colors = [self.white,self.black]

        # MADE TO GIVE X , Y COORDINATES TO THE RECTANGLES
        self.square_x = 0
        self.square_y = 0

        # MAKING THE RECTANGLE
        self.GiveBoard(surface)
        
    def GiveBoard(self,surface):    
        for i in range(self.num_rows*self.num_columns):
            # CHECKING FOR SQUARE COLOR
            color = self.GiveColor(i)
        
            # DRAWING SQUARE CUM RECTANGLE
            rect_desc = (self.square_x,self.square_y,self.square_side,self.square_side)
            self.squares[f"square{i}"] = pygame.draw.rect(surface,color,rect_desc)
            
            # CHECKING WHETHER TO GO TO NEXT LINE
            self.CheckForNextLine()
            
    def GiveColor(self,i):
        if i%8==0 and i>1:
            col0 = self.colors[0]
            col1 = self.colors[1]
            self.colors = [col1,col0]

        sq_color = None
        if i%2==0:
            sq_color = self.colors[0]
        else:
            sq_color = self.colors[1]

        return sq_color

    def CheckForNextLine(self):
        if self.square_x==7*self.square_side:
                self.square_y += self.square_side
                self.square_x = 0
        else:
            self.square_x+= self.square_side 
       

# SCREEN_WIDTH = 680
# SCREEN_HEIGHT = 680
# screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# my_board = ChessBoard(screen,SCREEN_WIDTH)

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type==QUIT:
#             running = False
#     pygame.display.update()
