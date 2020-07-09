import pygame
from . import player

class Queen(player.Player):
    def __init__(self,**kwargs):
        super(Queen,self).__init__(kwargs)
        self.max_movable_steps = 7
        self.min_movable_steps = 0
