import pygame
from player import Player

class Elephant(Player):
    def __init__(self,**kwargs):
        super(Elephant,self).__init__(**kwargs)
        self.max_movable_steps = 7
        self.min_movable_steps = 0
        self.max_steps_in_column_row = 7

    @classmethod
    def ElephantMoveAlgorithm(cls,self):
        # SELF.CURRENT_ROW , SELF.CURRENT_COLUMN
        columns_right = self.board.total_columns - self.current_column
        columns_left = self.current_column - 1
        rows_down = self.board.total_rows - self.current_row
        rows_up = self.current_row - 1
        moving_range = max(columns_left,columns_right,rows_up,rows_down)
        for i in range(moving_range):
            if columns_right>0:
                movable_column = self.current_column + columns_right
                columns_right -= 1
                movable_row = self.current_row
                self.AddMovableCell(column=movable_column,row=movable_row)
            if columns_left>0:
                movable_column = self.current_column - columns_left
                columns_left -= 1
                movable_row = self.current_row
                self.AddMovableCell(column=movable_column,row=movable_row)
            if rows_down>0:
                movable_column = self.current_column
                movable_row = self.current_row + rows_down
                rows_down -= 1
                self.AddMovableCell(column=movable_column,row=movable_row)
            if rows_up>0:
                movable_column = self.current_column
                movable_row = self.current_row - rows_up
                rows_up -= 1
                self.AddMovableCell(column=movable_column,row=movable_row)

    def MoveAlgorithm(self):
        Elephant.ElephantMoveAlgorithm(self)