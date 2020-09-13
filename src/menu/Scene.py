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

        self.playButton = GameButton((WINDOW_DIMENSIONS[0]/2 - 81, WINDOW_DIMENSIONS[1]/2 - 50), (162, 100), "Jouer")

        self.interactions.add(interactionFromGameObject(self.playButton, "playButton"))
        self.interactions.getInteraction("playButton").addAction(lambda: sceneHandler.setCurrentScene("scene1"))

    def draw(self, drawingSurface):
        drawingSurface.fill((52, 52, 255))
        super().draw(drawingSurface)

        self.playButton.drawOn(drawingSurface)

