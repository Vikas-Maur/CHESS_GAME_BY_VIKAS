import pygame
from player_settings import player , elephant , bishop

class Queen(player.Player):
    def __init__(self,**kwargs):
        super(Queen, self).__init__(img="queen.png",**kwargs)
        self.max_movable_steps = 7
        self.min_movable_steps = 0
        self.name = "queen"

    def MoveAlgorithm(self):
        elephant.Elephant.ElephantMoveAlgorithm(self)
        bishop.Bishop.BishopMoveAlgorithm(self)