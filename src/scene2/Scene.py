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

from GameButton import *

class Scene(EnigmaScene):
    def __init__(self, sceneHandler=None):
        super().__init__(sceneHandler=sceneHandler, nextSceneName="scene3")

        self.interactions = InteractionList()
        self.useInteractionsCursor = False
    
        self.font = pygame.font.SysFont("Comic Sans MS", 60)

        self.questionTxt = "Trouve le bouton caché."
        self.questionDim = self.font.size(self.questionTxt)
        self.questionSurface = self.font.render(self.questionTxt, False, (255, 255, 255))

        self.hiddenButtonRect = (100, 500, 50, 50)

        self.interactions.add(Interaction("hiddenButton", self.hiddenButtonRect[0:2], self.hiddenButtonRect[2:4]))
        self.interactions.getInteraction("hiddenButton").addAction(self.win)

    def draw(self, drawingSurface):
        drawingSurface.fill(self.backgroundColor)
        super().draw(drawingSurface)

        if not self.lost:
            pygame.draw.rect(drawingSurface, (54, 54, 255), self.hiddenButtonRect)

        drawingSurface.blit(self.questionSurface, (WINDOW_DIMENSIONS[0]/2 - self.questionDim[0]/2, WINDOW_DIMENSIONS[1]/4 + self.questionDim[1]/2))

    def handleEvents(self, events):
        super().handleEvents(events)

        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                if not self.interactions.touches(event.pos):
                    self.loose()
