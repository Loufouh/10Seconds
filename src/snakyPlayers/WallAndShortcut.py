#!/usr/bin/env python3

import pygame

from constants import *

from snakyPlayers.Player import Player

class WallAndShortcut(Player):
    def __init__(self, pos):
        super().__init__(pos)

        self.usedShortcut = False

    def update(self, deltaTime):
        super().update(deltaTime)

        if not self.usedShortcut and self.pos[0] >= 540 - self.dim[0]:
            self.pos[0] = 540 - self.dim[0]
        elif self.usedShortcut and self.pos[0] >= WINDOW_DIMENSIONS[0]:
            self.pos[0] = -self.dim[0]
            self.usedShortcut = False

        elif self.usedShortcut and self.pos[0] <= 552:
            self.pos[0] = 552
        elif self.pos[0] <= -self.dim[0]:
            self.pos[0] = WINDOW_DIMENSIONS[0]
            self.usedShortcut = True

        if self.pos[1] <= -self.dim[1]:
            self.pos[1] = WINDOW_DIMENSIONS[1]
        elif self.pos[1] >= WINDOW_DIMENSIONS[1]:
            self.pos[1] = -self.dim[1] 
