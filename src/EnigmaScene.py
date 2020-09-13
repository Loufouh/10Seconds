#!/usr/bin/env python3

import pygame

from Scene import Scene

from constants import *

class EnigmaScene(Scene):
    def __init__(self, sceneHandler=None, nextSceneName=""):
        super().__init__(sceneHandler)

        self.clock = sceneHandler.clock

        self.nextSceneName = nextSceneName

        self.timer = 10000

        self.winTimer = 0
        self.validated = False

        self.lostTimer = 0
        self.lost = False

        self.backgroundColor = (52, 52, 255)

        self.timerFont = pygame.font.Font("freesansbold.ttf", 75)

    def update(self):
        super().update()

        if self.timer > 0:
            self.timer -= self.clock.get_time()

        if self.timer <= 0:
            self.loose()
            self.timer = 10000

        if self.validated:
            self.winTimer += self.sceneHandler.clock.get_time()

            if self.winTimer > 500:
                self.__init__(self.sceneHandler)
                self.sceneHandler.setCurrentScene(self.nextSceneName)

        elif self.lost:
            self.lostTimer += self.sceneHandler.clock.get_time() 

            if self.lostTimer > 500:
                self.__init__(self.sceneHandler)
                self.sceneHandler.setCurrentScene("menu")

    def draw(self, drawingSurface):
        super().draw(drawingSurface)

        if not self.lost:
            timerColor = (255, 255, 255)

            if self.timer < 3000:
                timerColor = (255, 52, 52)

            timerRect = self.getTimerRect()
            drawingSurface.blit(self.timerFont.render(self.getTimerStr(), False, timerColor), (timerRect.x, timerRect.y))

    def getTimerRect(self):
        timerDim = self.timerFont.size(self.getTimerStr())
        return pygame.Rect((WINDOW_DIMENSIONS[0]/2 - timerDim[0]/2, 50), timerDim)

    def getTimerStr(self):
        return str(self.timer//1000 + 1)
                    
    def loose(self):
        if self.validated:
            return

        self.lost = True
        self.backgroundColor = (255, 52, 52)

    def win(self):
        if self.lost:
            return

        self.validated = True
        self.backgroundColor = (52, 255, 52)
