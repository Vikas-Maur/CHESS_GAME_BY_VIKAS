import pygame
from . import player

class Bishop(player.Player):
    def __init__(self,**kwargs):
        super(Bishop,self).__init__(kwargs)
        self.max_movable_steps = 7
        self.min_movable_steps = 0
