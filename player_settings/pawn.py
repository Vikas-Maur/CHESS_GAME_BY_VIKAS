import pygame
from player_settings import player

class Pawn(player.Player):
    def __init__(self,**kwargs):
        super(Pawn,self).__init__(img="pawn.png",**kwargs)
        self.max_movable_steps = 2
        self.normal_movable_steps = 1
        self.max_steps_in_column_row = 1
        self.moving_direction = self.ReturnMovingDirection()
        self.killing = False
        super(Pawn, self).ResizePlayerImage(width=-10,height=-10)
        self.name = "pawn"

    def MoveAlgorithm(self):
        if self.moving_direction=="down" or self.moving_direction=="d":
            movable_row = self.current_row + self.max_steps_in_column_row
        else:
            movable_row = self.current_row - self.max_steps_in_column_row

        movable_column = self.current_column
        super(Pawn, self).AddMovableCell(column=movable_column,row=movable_row)
        if self.killing:
            movable_column = self.current_column
            movable_column += self.max_steps_in_column_row
            super(Pawn, self).AddMovableCell(column=movable_column,row=movable_row)
            movable_column -= 2*self.max_steps_in_column_row
            super(Pawn,self).AddMovableCell(column=movable_column,row=movable_row)

    def ChangeKilling(self,kill):
        self.killing = kill

    def ReturnMovingDirection(self):
        direction = None
        if self.team=="blacks":
            direction = "up"
        else:
            direction = "down"
        return direction