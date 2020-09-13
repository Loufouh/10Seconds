#!/usr/bin/env python3

from GameObject import *

import pygame

class GameButton(GameObject):
    def __init__(self, pos, dim, text=""):
        super().__init__(pos, None)
        self.dim = list(dim)
        self.text = text;
    
        self.font = pygame.font.Font("freesansbold.ttf", 38)
        self.textSurface = self.font.render(text, False, (52, 52, 52))
        self.textDim = self.font.size(text)

    def drawOn(self, drawingSurface):
        pygame.draw.rect(drawingSurface, (255, 255, 255), (self.pos[0], self.pos[1], self.dim[0], self.dim[1]))
        drawingSurface.blit(self.textSurface, (self.pos[0] + self.dim[0]/2 - self.textDim[0]/2, self.pos[1] + self.dim[1]/2 - self.textDim[1]/2))

    def update(self):
        '''
            To call at each game loop iteration
        '''

    def move(self, translationVector):
        '''
            Vector translation

            Args:
                translationVector (list(int))
        '''
        self.pos = [a + b for a, b in zip(self.pos, translationVector)]

    def setSprite(self, sprite):
        print("GameButton can't have a sprite")

    def setPos(self, pos):
        self.pos = pos

    def getDim(self):
        return self.dim
