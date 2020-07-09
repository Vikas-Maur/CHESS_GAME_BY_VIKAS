import pygame
from . import player

class King(player.Player):
    def __init__(self,**kwargs):
        super(King,self).__init__(kwargs)
        self.max_movable_steps = 1
        self.min_movable_steps = 0
