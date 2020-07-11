import pygame
from player import Player
from elephant import Elephant
from bishop import Bishop

class Queen(Player):
    def __init__(self,**kwargs):
        super(Queen, self).__init__(**kwargs)
        self.max_movable_steps = 7
        self.min_movable_steps = 0

    def MoveAlgorithm(self):
        Elephant.ElephantMoveAlgorithm(self)
        Bishop.BishopMoveAlgorithm(self)