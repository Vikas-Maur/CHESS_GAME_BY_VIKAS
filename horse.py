import pygame
from player import Player

class Horse(Player):
    def __init__(self,**kwargs):
        super(Horse,self).__init__(**kwargs)
        self.max_movable_steps = 3
        self.min_movable_steps = 0
        self.max_steps_in_column_row = 2

    def MoveAlgorithm(self):
        """
        I AM HAVING , SELF.CURRENT_ROW , SELF.CURRENT_COLUMN
        OPERTORS = + , -
        MOVING = ROW , COLUMN
        """
        move_by = [(self.max_movable_steps-self.max_steps_in_column_row),-(self.max_movable_steps-self.max_steps_in_column_row),(self.max_steps_in_column_row),-(self.max_steps_in_column_row)]
        for items in move_by:
            row = int(self.current_row[1])+items
            left_steps = self.max_movable_steps - abs(items)
            column = int(self.current_column[1])
            column += left_steps
            self.movable_cells.append(f"c{column}-r{row}")
            column -= 2*left_steps
            self.movable_cells.append(f"c{column}-r{row}")


