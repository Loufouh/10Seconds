#!/usr/bin/env python3

import pygame

from constants import *

from EnigmaScene import EnigmaScene

from GameObject import GameObject
from Animation import animationFromFolder, convertAlphaImage

from AnimatedGameObject import AnimatedGameObject

from Interaction import interactionFromGameObject
from InteractionList import InteractionList

from GameButton import GameButton 

class Scene(EnigmaScene):
    def __init__(self, sceneHandler=None):
        super().__init__(sceneHandler=sceneHandler, nextSceneName="scene2")

        self.interactions = InteractionList()
    
        self.font = pygame.font.Font("freesansbold.ttf", 90)

        self.questionTxt = "1 + 1 = ?"
        self.questionDim = self.font.size(self.questionTxt)
        self.questionSurface = self.font.render(self.questionTxt, False, (255, 255, 255))

        self.buttons = []

        for y in range(2):
            for x in range(5):
                num = 5*y + x

                self.buttons.append(GameButton((WINDOW_DIMENSIONS[0]/2 - 240 + x*100, WINDOW_DIMENSIONS[1]/2 + 100 + y*100), (80, 80), str(num)))
                self.interactions.add(interactionFromGameObject(self.buttons[-1], "button" + str(num)))

                if num != 2:
                    self.interactions.getInteraction("button" + str(num)).addAction(self.loose)

            self.interactions.getInteraction("button2").addAction(self.win)

    def draw(self, drawingSurface):
        drawingSurface.fill(self.backgroundColor)
        super().draw(drawingSurface)

        drawingSurface.blit(self.questionSurface, (WINDOW_DIMENSIONS[0]/2 - self.questionDim[0]/2, WINDOW_DIMENSIONS[1]/4 + self.questionDim[1]/2))

        for button in self.buttons:
            button.drawOn(drawingSurface)
