#!/usr/bin/env python3

import pygame

from pygame.locals import MOUSEBUTTONDOWN

from constants import *

from GameObject import GameObject
from EnigmaScene import EnigmaScene
from Animation import animationFromFolder, convertAlphaImage

from AnimatedGameObject import AnimatedGameObject

from Interaction import Interaction, interactionFromGameObject
from InteractionList import InteractionList

from GameButton import GameButton

class Scene(EnigmaScene):
    def __init__(self, sceneHandler=None):
        super().__init__(sceneHandler=sceneHandler, nextSceneName="scene6")

        clock = sceneHandler.clock

        self.font = pygame.font.SysFont("Comic Sans MS", 120)

        self.questionTxt = "Victoire !"
        self.questionDim = self.font.size(self.questionTxt)

        self.questionSurface = self.font.render(self.questionTxt, False, (255, 255, 255))

        self.showButton = False
        buttonDim = [200, 80]

        self.button = GameButton([a - b - 20 for a, b in zip(WINDOW_DIMENSIONS, buttonDim)], buttonDim, "Continuer")
        self.interactions.add(interactionFromGameObject(self.button, "continueButton"))
        self.interactions.getInteraction("continueButton").addAction(self.win)

        self.interactions.setInactive()

    def update(self):
        super().update()

        if self.timer < 500:
            self.showButton = True
            self.interactions.setActive()

    def draw(self, drawingSurface):
        drawingSurface.fill(self.backgroundColor)
        super().draw(drawingSurface)

        drawingSurface.blit(self.questionSurface, [(a - b)/2 for a, b in zip(WINDOW_DIMENSIONS, self.questionDim)])

        if self.showButton:
            self.button.drawOn(drawingSurface)

