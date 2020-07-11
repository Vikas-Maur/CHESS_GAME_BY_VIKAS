import pygame
from player import Player

class Bishop(Player):
    def __init__(self,**kwargs):
        super(Bishop,self).__init__(**kwargs)
        self.max_movable_steps = 7
        self.min_movable_steps = 0
        self.max_steps_in_column_row = 7

    @classmethod
    def BishopMoveAlgorithm(cls,self):
        move_from = [self.current_column,self.current_row]
        move_pairs1 = [(move_from[0],move_from[1],a,-a)for a in range(1,8)]
        move_pairs2 = [(move_from[0],move_from[1],a,a)for a in range(1,8)]
        move_pairs3 = [(move_from[0],move_from[1],-a,a)for a in range(1,8)]
        move_pairs4 = [(move_from[0],move_from[1],-a,-a)for a in range(1,8)]
        adding_range = max(len(move_pairs1),len(move_pairs2),len(move_pairs3),len(move_pairs4))
        for i in range(adding_range):
            self.AddMovableCellWithCellInfo(move_pairs1[i])
            self.AddMovableCellWithCellInfo(move_pairs2[i])
            self.AddMovableCellWithCellInfo(move_pairs3[i])
            self.AddMovableCellWithCellInfo(move_pairs4[i])

    def MoveAlgorithm(self):
        Bishop.BishopMoveAlgorithm(self)