import pygame
from player_settings import player

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
        self.color1 = (220,100,0)
        self.color2 = (240,150,0)
        self.colors = [self.color1,self.color2]

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

            pygame.draw.rect(self.surface,color,rect_desc)
            self.squares[self.cell_name] = {"rect":rect_desc, "color":color,
                                            "position":(self.square_x, self.square_y),
                                            "image_on_it": False, "image": None,"image_team":None}

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
        border_rect = self.squares[kwargs['cell']]
        border_color = kwargs["border_color"]
        pygame.draw.rect(self.surface,border_color,border_rect["rect"])
        pygame.draw.rect(self.surface,border_rect["color"],border_rect["rect"].inflate(-10,-10))
        self.squares_with_border.append(kwargs['cell'])

    def RemoveBorder(self,cell):
        cell_to_remove_border = self.squares[cell] 
        pygame.draw.rect(self.surface,cell_to_remove_border["color"],cell_to_remove_border["rect"])
        if cell_to_remove_border["image_on_it"]:
            image = cell_to_remove_border["image"]
            x = cell_to_remove_border["position"][0]
            y = cell_to_remove_border["position"][1]
            self.surface.blit(image,(x,y))
        del self.squares_with_border[self.squares_with_border.index(cell)]

    def RemoveBorderFromAllCells(self):
        deletable_cells = self.squares_with_border.copy()
        for cell in deletable_cells:
            self.RemoveBorder(cell)

    def MoveBorder(self,**kwargs):
        cell_name = kwargs['cell']
        cell_border = kwargs['border_color']
        if len(self.squares_with_border)==1:
            self.RemoveBorder(self.squares_with_border[0])
        self.DrawBorder(cell=cell_name,border_color=cell_border)

    def MoveAllBorders(self,**kwargs):
        cell_to_remove_border = kwargs["remove_border"]
        try:
            for cell in cell_to_remove_border:
                self.RemoveBorder(cell)
        except:
            pass
        cell_to_add_border = kwargs["add_border"]
        for cell in cell_to_add_border:
            self.DrawBorder(cell=cell,border_color=kwargs["border_color"])

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

    def GiveSquareDetails(self,**kwargs):
        cell = kwargs["cell"]
        returning_parameter = self.CheckReturningParameter(kwargs["parameter"])
        given_square = self.squares[cell]
        try:
            if kwargs["change"]==True or kwargs["change"]=="true" or kwargs["change"]=="True":
                changing_value = kwargs["change_value"]
                self.squares[cell][returning_parameter] = changing_value
            else:
                return given_square[returning_parameter]
        except:
            return given_square[returning_parameter]

    def CheckReturningParameter(self,parameter):
        if "p" in parameter:
            if parameter=="pos" or parameter=="position" or parameter=="p":
                return "position"
        elif "c" in parameter:
            if parameter=="color" or parameter=="c":
                return "color"
        elif "r" in parameter:
            if parameter=="rect_desc" or parameter=="rectangle" or parameter=="rect" or parameter=="r":
                return "rect"
        elif "i" in parameter:
            if parameter=="imageonit" or parameter=="image-onit" or parameter=="image-on-it" or parameter=="image_on_it" or parameter=="img_on_it" or parameter=="image_onit":
                return "image_on_it"
            elif parameter=="image":
                return "image"
            elif parameter=="image_team" or parameter=="img_team" or parameter=="img-team" or parameter=="image-team":
                return "image_team"
        else:
            raise Exception("THE GIVEN PARAMETER IS NOT PRESENT IN SELF.SQUARES CHECK THE INPUT")

    def ChangeImageOnSquareSettings(self,**kwargs):
        cell_to_change = kwargs["cell"]
        image_on_it = kwargs["image"]
        self.squares[cell_to_change]["image_on_it"] = True
        self.squares[cell_to_change]["image"] = image_on_it

    def GiveNearbyCells(self,cell):
        cell_column = int(cell[1])
        cell_row = int(cell[-1])
        nearby_columns = [0,1,-1]
        nearby_row = [0,1,-1]
        nearby_cells = [f"c{col+cell_column}-r{row+cell_row}" for col in nearby_columns for row in nearby_row]
        del nearby_cells[0]
        check_nearby_cells = nearby_cells.copy()
        for cell in check_nearby_cells:
            if ("c9" in cell or "r9" in cell or "c0" in cell or "r0" in cell):
                nearby_cells.remove(cell)
        return nearby_cells

    def DrawASquare(self,**kwargs):
        cell_to_draw = player.Player.CheckInput_GIVE_CELL(self,**kwargs)
        rect_to_draw = self.GiveSquareDetails(change=False,parameter="r",cell=cell_to_draw)
        rect_color = self.GiveSquareDetails(change=False,parameter="color",cell=cell_to_draw)
        pygame.draw.rect(self.surface,rect_color,rect_to_draw)