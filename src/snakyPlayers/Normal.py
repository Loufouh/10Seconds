#!/usr/bin/env python3

import pygame

from constants import *

from snakyPlayers.Player import Player

class Normal(Player):
    def __init__(self, pos):
        super().__init__(pos)

    def update(self, deltaTime):
        super().update(deltaTime)

        if self.pos[0] >= WINDOW_DIMENSIONS[0] - self.dim[0]:
            self.pos[0] = WINDOW_DIMENSIONS[0] - self.dim[0]
        elif self.pos[0] <= 0:
            self.pos[0] = 0

        if self.pos[1] <= 0:
            self.pos[1] = 0
        elif self.pos[1] >= WINDOW_DIMENSIONS[1] - self.dim[1]:
            self.pos[1] = WINDOW_DIMENSIONS[1] - self.dim[1]
