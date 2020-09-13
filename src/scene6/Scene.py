#!/usr/bin/env python3

import pygame

from pygame.locals import KEYDOWN, K_DOWN, K_LEFT, K_UP, K_RIGHT 

from constants import *

from GameObject import GameObject
from EnigmaScene import EnigmaScene
from Animation import animationFromFolder, convertAlphaImage

from AnimatedGameObject import AnimatedGameObject

from Interaction import Interaction, interactionFromGameObject
from InteractionList import InteractionList

from GameButton import GameButton

from snakyPlayers.Normal import Normal as Player

class Scene(EnigmaScene):
    def __init__(self, sceneHandler=None):
        super().__init__(sceneHandler=sceneHandler, nextSceneName="scene7")

        clock = sceneHandler.clock
        self.player = Player([10, WINDOW_DIMENSIONS[1]/2])

    def update(self):
        super().update()
        self.player.update(self.clock.get_time())

        if pygame.Rect(self.player.pos, self.player.dim).colliderect((600, 500, 25, 25)):
            self.win()

    def draw(self, drawingSurface):
        drawingSurface.fill(self.backgroundColor)
        super().draw(drawingSurface)

        pygame.draw.rect(drawingSurface, (255, 52, 52), (600, 500, 25, 25))
        self.player.drawOn(drawingSurface)

    def handleEvents(self, events):
        super().handleEvents(events)

        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    self.player.direction = (0, 1 - 2*(self.timer//1000%2 == 0))
                elif event.key == K_LEFT:
                    self.player.direction = (-1 + 2*(self.timer//1000%2 == 0), 0)
                elif event.key == K_UP:
                    self.player.direction = (0, -1 + 2*(self.timer//1000%2 == 0))
                elif event.key == K_RIGHT:
                    self.player.direction = (1 - 2*(self.timer//1000%2 == 0), 0)

    def win(self):
        super().win()
        self.player.direction = (0, 0)
