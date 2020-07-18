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
        self.image_width = self.board.square_side-self.extra_scale
        self.image_height = self.board.square_side-self.extra_scale
        self.image = pygame.transform.scale(self.image,(self.image_width,self.image_height))

        self.position = kwargs["position"]

        self.movable_cells = []
        self.current_row = int(self.position[4])
        self.current_column = int(self.position[1])
        self.max_movable_steps = None
        self.min_movable_steps = None
        self.max_steps_in_column_row = None
        self.name = None

    def DrawOnScreen(self):
        value = self.board.GiveSquareDetails(change=False,cell=self.position,parameter="pos")
        self.board.GiveSquareDetails(change=True,cell=self.position,parameter="img_team",change_value=self.team)
        x , y = value[0] , value[1]
        self.surface.blit(self.image,(x,y))
        self.board.ChangeImageOnSquareSettings(cell=self.position,image=self.image)

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
                test_for_deletable_cell = self.board.squares[cell]
                if test_for_deletable_cell["image_on_it"]:
                    deletables.append(cell)
            except:
                deletables.append(cell)
        check_for_nearby_cells = self.board.GiveNearbyCells(self.position)
        checking_num_cells = 0
        not_horse = True
        if self.name=="horse":
            not_horse = False
        if not_horse:
            for cell in check_for_nearby_cells:
                if cell in deletables or cell not in self.movable_cells:
                    checking_num_cells += 1
        if checking_num_cells == len(check_for_nearby_cells):
            deletables = self.movable_cells.copy()

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

    def MovePlayer(self,**kwargs):
        self.board.GiveSquareDetails(change=True,parameter="image",change_value=None)
        self.board.GiveSquareDetails(change=True,parameter="image-onit",change_value=False)
        cell_no = Player.CheckInput_GIVE_CELL(self,**kwargs)
        self.DefineCurrentPosition(cell_no)
        self.DrawOnScreen()

    def DefineCurrentPosition(self,cell):
        self.position = cell
        self.current_row = int(self.position[4])
        self.current_column = int(self.position[1])

    def DrawBorderOnPlayer(self,**kwargs):
        cell_no = Player.CheckInput_GIVE_CELL(self,**kwargs)
        self.board.DrawBorder(cell=cell_no,border_color=(0,200,0))
        self.DrawOnScreen()

    def DrawBorderOnMovableCells(self):
        for cells  in self.movable_cells:
            self.board.DrawBorder(cell=cells,border_color=(0,0,0))

    def SelectPlayer(self,**kwargs):
        self.GiveMovableCells()
        self.board.RemoveBorderFromAllCells()
        self.DrawBorderOnPlayer(**kwargs)
        self.DrawBorderOnMovableCells()

    @classmethod
    def CheckInput_GIVE_CELL(cls,self,**kwargs):
        try:
            cell_no = kwargs["cell"]
        except:
            mouse_pos_x , mouse_pos_y = kwargs["x"] , kwargs["y"]
            cell_no = self.board.GiveCell(x=mouse_pos_x,y=mouse_pos_y)
        return  cell_no

    def ResizePlayerImage(self,**kwargs):
        extra_width = kwargs["width"]
        extra_height = kwargs["height"]
        self.image_width += extra_width
        self.image_height += extra_height
        self.image = pygame.transform.scale(self.image,(self.image_width,self.image_height))