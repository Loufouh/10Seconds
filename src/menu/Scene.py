#/usr/bin/env python3

import pygame

from constants import *

from GameObject import GameObject
from Scene import Scene as Scene_abstract
from Animation import animationFromFolder, convertAlphaImage

from AnimatedGameObject import AnimatedGameObject

from Interaction import interactionFromGameObject
from InteractionList import interactionListFromFile

from GameButton import *

class Scene(Scene_abstract):
    def __init__(self, sceneHandler=None):
        super().__init__(sceneHandler=sceneHandler)

        clock = sceneHandler.clock

        self.font = pygame.font.Font("freesansbold.ttf", 96)

        self.titleStr = "10 Seconds"
        self.titleDim = self.font.size(self.titleStr)
        self.titleSurface = self.font.render(self.titleStr, False, (255, 255, 255))
        
        self.playButton = GameButton((WINDOW_DIMENSIONS[0]/2 - 81, WINDOW_DIMENSIONS[1]*9/16 - 50), (162, 100), "Jouer")

        self.interactions.add(interactionFromGameObject(self.playButton, "playButton"))
        self.interactions.getInteraction("playButton").addAction(lambda: sceneHandler.setCurrentScene("scene1"))

    def draw(self, drawingSurface):
        drawingSurface.fill((52, 52, 255))
        super().draw(drawingSurface)

        self.playButton.drawOn(drawingSurface)
        drawingSurface.blit(self.titleSurface, [WINDOW_DIMENSIONS[0]/2 - self.titleDim[0]/2, WINDOW_DIMENSIONS[1]*5/16 - self.titleDim[1]/2])

