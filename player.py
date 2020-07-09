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
        self.image = pygame.image.load(kwargs["img"]).convert_alpha()
        self.extra_scale = 10
        self.image = pygame.transform.scale(self.image,(self.board.square_side-self.extra_scale,self.board.square_side-self.extra_scale))

        self.position = kwargs["position"]

        self.movable_cells = []
        self.current_row = self.position[3:5]
        self.current_column = self.position[:2]
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
        print(self.movable_cells)
        deletables = []
        for cell in self.movable_cells:
            try:
                x = self.board.squares[cell]
            except:
                print(cell)
                deletables.append(cell)
        for cell in deletables:
            self.movable_cells.remove(cell)

    def AddMovableCell(self,**kwargs):
        movable_column = f'c{kwargs["column"]}'
        movable_row = f'r{kwargs["row"]}'
        self.movable_cells.append(f"{movable_column}-{movable_row}")

