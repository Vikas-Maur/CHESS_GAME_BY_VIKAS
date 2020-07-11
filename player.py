import pygame

class Player:
    def __init__(self,**kwargs):
        """
        moving algorithm-movable amount
        starting_position
        """
        self.team = kwargs["team"]
        self.surface = kwargs["surface"]
        self.board = kwargs["board"]
        # IMAGE SETTINGS
        self.image = pygame.image.load(f'assets/{self.team}/{kwargs["img"]}').convert_alpha()
        self.extra_scale = 10
        self.image = pygame.transform.scale(self.image,(self.board.square_side-self.extra_scale,self.board.square_side-self.extra_scale))

        self.position = kwargs["position"]

        self.movable_cells = []
        self.current_row = int(self.position[4])
        self.current_column = int(self.position[1])
        self.max_movable_steps = None
        self.min_movable_steps = None
        self.max_steps_in_column_row = None

    def DrawOnScreen(self):
        x = self.board.squares[self.position][2][0]
        y = self.board.squares[self.position][2][1]
        self.surface.blit(self.image,(x,y))

    def Change_position(self,position):
        self.position = position
        self.DrawOnScreen()

    def MoveAlgorithm(self):
        return "PLAYER OBJECT HAS NO ALGORITHM OF ITS OWN"

    def GiveMovableCells(self):
        self.MoveAlgorithm()
        deletables = []
        for cell in self.movable_cells:
            try:
                x = self.board.squares[cell]
            except:
                deletables.append(cell)

        for cell in deletables:
            self.movable_cells.remove(cell)

    def AddMovableCell(self,**kwargs):
        try :
            cell_name = kwargs["cell"]
            self.movable_cells.append(cell_name)
        except:
            movable_column = f'c{kwargs["column"]}'
            movable_row = f'r{kwargs["row"]}'
            self.movable_cells.append(f"{movable_column}-{movable_row}")

    def AddMovableCellWithCellInfo(self,given_cell_info):
        # A METHOD WHICH CONTAINS CELL INFO IN THE FORM -
        # (COLUMN , ROW , ADDITION IN COLUMN , ADDITION IN ROW)
        #  ADDS "COLUMN + ADDTION IN COLUMN" AND "ROW + ADDITION IN ROW"
        # AND THEN ADDS TO MOVABLE CELLS
        cell_info = given_cell_info
        moving_column = cell_info[0] + cell_info[2]
        moving_row = cell_info[1] + cell_info[3]
        self.AddMovableCell(row=moving_row, column=moving_column)

