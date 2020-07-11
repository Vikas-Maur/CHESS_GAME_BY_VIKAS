import pygame
from pygame.locals import *

class ChessBoard:
    def __init__(self,surface,surface_side):
        self.square_side = int(surface_side/8)
        self.total_rows = 8
        self.total_columns = 8
        self.square_color = None

        # GETTING A DICT OF SQUARE WITH KEY AS 
        # CELL-NUMBER AND VALUE AS THAT RECTANGLE
        self.squares = {}

        # DEFINING COLOR ASPECT
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.colors = [self.white,self.black]

        # MADE TO GIVE X , Y COORDINATES TO THE RECTANGLES
        self.square_x = 0
        self.square_y = 0
        self.current_row = 1    # MADE FOR NAMING RECTANGLES PROPERLY   
        self.current_column = 1 # MADE FOR NAMING RECTANGLES PROPERLY  
        self.cell_name = f"c{self.current_column}-r{self.current_row}"
        self.square_x_coordinates = self.square_y_coordinates = [i*self.square_side for i in range(8)]
        # self.square_positions = [] # HOLDS X,Y HISTORY OF SQUARES

        self.squares_with_border = []

        # MAKING THE RECTANGLE
        self.surface = surface
        self.GiveBoard()
        
    def GiveBoard(self):    
        for i in range(self.total_rows*self.total_columns):
            # CHECKING FOR SQUARE COLOR
            color = self.GiveColor(i)
        
            # DRAWING SQUARE CUM RECTANGLE
            rect_desc = pygame.Rect(self.square_x,self.square_y,self.square_side,self.square_side)
            # self.squares[f"c{i}"] = pygame.draw.rect(surface,color,rect_desc)

            pygame.draw.rect(self.surface,color,rect_desc)
            self.squares[self.cell_name] = [rect_desc,color,(self.square_x,self.square_y),{"image-onit":False}]

            # self.squares_with_border[self.cell_name]=False
            # self.square_positions.append((self.square_x,self.square_y))
            
            # CHECKING WHETHER TO GO TO NEXT LINE
            self.CheckForBlockPlacement()
            
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

    def CheckForBlockPlacement(self):
        if self.square_x==7*self.square_side:
                self.square_y += self.square_side
                self.square_x = 0
                self.current_row += 1
                self.current_column = 1
        else:
            self.square_x+= self.square_side 
            self.current_column +=1
        self.cell_name = f"c{self.current_column}-r{self.current_row}"
       
    def DrawBorder(self,**kwargs):
        if len(self.squares_with_border)>1:
            for item in self.squares_with_border:
                del self.squares_with_border[self.squares_with_border.index(item)]       

        border_rect = self.squares[kwargs['cell']]
        border_color = kwargs["border_color"]
        pygame.draw.rect(self.surface,border_color,border_rect[0]) 
        pygame.draw.rect(self.surface,border_rect[1],border_rect[0].inflate(-10,-10)) 
        self.squares_with_border.append(kwargs['cell'])

    def RemoveBorder(self,cell):
        cell_to_remove_border = self.squares[cell] 
        pygame.draw.rect(self.surface,cell_to_remove_border[1],cell_to_remove_border[0])
        del self.squares_with_border[self.squares_with_border.index(cell)]

    def MoveBorder(self,**kwargs):
        cell_name = kwargs['cell']
        cell_border = kwargs['border_color']
        for item in self.squares_with_border:
            self.RemoveBorder(item)
        self.DrawBorder(cell=cell_name,border_color=cell_border)

    def MoveBorderOnArrow(self,**kwargs):
        arrow = kwargs["arrow"]
        cell_to_move = self.squares_with_border[0]
        cell_to_move = list(cell_to_move)
        if arrow=="up" or arrow=="u":
            if cell_to_move[4]!="1":
                cell_to_move[4]=str(int(cell_to_move[4])-1)

        elif arrow=="down" or arrow=="d":
            if cell_to_move[4]!="8":
                cell_to_move[4]=str(int(cell_to_move[4])+1)

        elif arrow=="left" or arrow=="l":
            if cell_to_move[1]!="1":
                cell_to_move[1]=str(int(cell_to_move[1])-1)

        elif arrow=="right" or arrow=="r":
            if cell_to_move[1]!="8":
                cell_to_move[1]=str(int(cell_to_move[1])+1)
        cell_to_move = "".join(cell_to_move)
        self.MoveBorder(cell=cell_to_move,border_color=kwargs["border_color"])

    def GiveCell(self,**kwargs):
        row_no = column_no = 0
        x,y = kwargs['x'] , kwargs['y']
        for i in range(8):
            checking_row = checking_column = i
            squareX = squareY = self.square_x_coordinates[i]
            if x-squareX<self.square_side and x-squareX>=0:
                column_no = checking_column
            if y-squareY<self.square_side and y-squareY>=0:
                row_no = checking_row
            if row_no != 0 and column_no !=0:
                break

        row_no+=1
        column_no+=1
        cell = f"c{column_no}-r{row_no}"
        return cell

    def TellPos(self,cell):
        return self.squares[cell][2]

    def TellColor(self,cell):
        return self.squares[cell][1]

    def TellDict(self,cell):
        return self.squares[cell][3]