#/usr/bin/env python3

import pygame

from constants import *

from GameObject import GameObject
from Scene import Scene as Scene_abstract
from Animation import animationFromFolder, convertAlphaImage

from AnimatedGameObject import AnimatedGameObject

from Interaction import interactionFromGameObject
from InteractionList import interactionListFromFile

from GameButton import GameButton

class Scene(Scene_abstract):
    def __init__(self, sceneHandler=None):
        super().__init__(sceneHandler=sceneHandler)

        clock = sceneHandler.clock

        self.font = pygame.font.SysFont("Comic Sans MS", 120)
        self.txt = "Jeu terminé !"
        self.txtDim = self.font.size(self.txt)
        self.txtSurface = self.font.render(self.txt, False, (255, 255, 255))

        buttonDim = [140, 60]
        self.button = GameButton([a - b - 20 for a, b in zip(WINDOW_DIMENSIONS, buttonDim)], buttonDim, "Menu")

        self.interactions.add(interactionFromGameObject(self.button, "button"))
        self.interactions.getInteraction("button").addAction(lambda: self.sceneHandler.setCurrentScene("menu"))
        
    def draw(self, drawingSurface):
        drawingSurface.fill((52, 52, 255))
        super().draw(drawingSurface)

        drawingSurface.blit(self.txtSurface, [(a - b)/2 for a, b in zip(WINDOW_DIMENSIONS, self.txtDim)])
        self.button.drawOn(drawingSurface)

