import pygame
from player import Player

class Elephant(Player):
    def __init__(self,**kwargs):
        super(Elephant,self).__init__(**kwargs)
        self.max_movable_steps = 7
        self.min_movable_steps = 0
        self.max_steps_in_column_row = 7

    def MoveAlgorithm(self):
        movable_in_columns = None
        movable_in_rows = None
        for i in range(1,8):
            movable_in_column = f"c{int(self.current_column[1])+i}-{self.current_row}"
            movable_in_row = f"{self.current_column}-r{int(self.current_row[1])+i}"
            self.movable_cells.append(movable_in_column)
            self.movable_cells.append(movable_in_row)
            movable_in_column2 = f"c{int(self.current_column[1])-i}-{self.current_row}"
            movable_in_row2 = f"{self.current_column}-r{int(self.current_row[1])-i}"
            self.movable_cells.append(movable_in_column2)
            self.movable_cells.append(movable_in_row2)
