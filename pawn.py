import pygame
from player import Player

class Pawn(Player):
    def __init__(self,**kwargs):
        super(Pawn,self).__init__(**kwargs)
        self.max_movable_steps = 2
        self.normal_movable_steps = 1
        self.max_steps_in_column_row = 1
        self.moving_direction = kwargs["direction"]
        self.killing = False

    def MoveAlgorithm(self):
        if self.moving_direction=="down" or self.moving_direction=="d":
            movable_row = int(self.current_row[1]) + self.max_steps_in_column_row
        else:
            movable_row = int(self.current_row[1]) - self.max_steps_in_column_row

        movable_column = self.current_column[1]
        super(Pawn, self).AddMovableCell(column=movable_column,row=movable_row)
        if self.killing:
            movable_column = int(self.current_column[1])
            movable_column += self.max_steps_in_column_row
            super(Pawn, self).AddMovableCell(column=movable_column,row=movable_row)
            movable_column -= 2*self.max_steps_in_column_row
            super(Pawn,self).AddMovableCell(column=movable_column,row=movable_row)


    def ChangeKilling(self,kill):
        self.killing = kill

