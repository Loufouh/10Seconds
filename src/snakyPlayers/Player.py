#!/usr/bin/env python3

import pygame

from constants import *

from GameObject import GameObject

class Player(GameObject):
    def __init__(self, pos):
        self.pos = list(pos)
        self.dim = [20, 20]
        self.direction = [1, 0]
        self.speed = 140 # pixel per sec

    def update(self, deltaTime):
        self.pos = [a + b*self.speed*deltaTime/1000 for a, b in zip(self.pos, self.direction)]

    def drawOn(self, drawingSurface):
        pygame.draw.rect(drawingSurface, (255, 255, 255), self.pos + self.dim)

    def setPos(self, pos):
        self.pos = pos

    def getDim(self):
        return self.dim

    def getPos(self):
        return self.pos
