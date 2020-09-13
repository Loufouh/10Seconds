#!/usr/bin/env python3

import pygame

from pygame.locals import MOUSEBUTTONDOWN
from math import pi, sin

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
        super().__init__(sceneHandler=sceneHandler, nextSceneName="winScene")

        clock = sceneHandler.clock

        self.font = pygame.font.SysFont("Comic Sans MS", 120)

        self.questionAnimationTime = 0
        self.questionAnimationMaxAngle = 0
        self.angle = 0
        self.questionHitCounter = 0
        self.questionFalling = False
        self.questionPos = []

        self.questionTxt = "Victoire !"
        self.questionDim = self.font.size(self.questionTxt)

        self.questionSurface = pygame.Surface([a + 20 for a in self.questionDim]).convert_alpha()
        self.questionSurface.fill((255, 255, 255))

        self.questionSurface.blit(self.font.render(self.questionTxt, False, (52, 52, 255)), (10, 10))

        buttonDim = [200, 80]
        self.hiddenButton = GameButton([(a - b)/2 for a, b in zip(WINDOW_DIMENSIONS, buttonDim)], buttonDim, "Continuer")
        self.interactions.add(interactionFromGameObject(self.hiddenButton, "continueButton"))
        self.interactions.getInteraction("continueButton").addAction(self.win)

        self.interactions.setInactive()

    def update(self):
        super().update()
        self.timer = 10000
        self.questionAnimationTime += self.clock.get_time()

        if self.questionFalling:
            self.questionPos[1] += self.clock.get_time()*1000/1000 # 1000 px/s
        else:
            self.questionPos = [(a - b)/2 for a, b in zip(WINDOW_DIMENSIONS, self.getRotatedQuestionSurface().get_size())]

    def draw(self, drawingSurface):
        drawingSurface.fill(self.backgroundColor)
        super().draw(drawingSurface)

        self.hiddenButton.drawOn(drawingSurface)
        drawingSurface.blit(self.getRotatedQuestionSurface(), self.questionPos)

    def handleEvents(self, events):
        super().handleEvents(events)

        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                if pygame.Rect(self.questionSurface.get_rect(center=[a/2 for a in WINDOW_DIMENSIONS])).collidepoint(event.pos):
                    if self.questionFalling:
                        continue

                    if self.questionHitCounter >= 20:
                        self.questionFalling = True
                        self.interactions.setActive()
                    else:
                        self.questionHitCounter += 1

                    self.questionAnimationTime = 0
                    self.questionAnimationMaxAngle = 50/20*self.questionHitCounter + 5

    def getRotatedQuestionSurface(self):
        x  = self.questionAnimationTime/100
        maxAngle = self.questionAnimationMaxAngle

        if x >= 5:
            return self.questionSurface
        return pygame.transform.rotate(self.questionSurface, sin(x)*(-x*maxAngle/5 + maxAngle))
