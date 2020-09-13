#!/usr/bin/env python3

import pygame

from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, MOUSEMOTION, MOUSEBUTTONDOWN # pylint: disable=E0611
from InteractionList import InteractionList

class Scene:
    '''
        A group of gameObjects

        Args:
            sceneHandler (SceneHandler) (optional)

        Attributes:
            keepRunning (bool)
    '''
    def __init__(self, sceneHandler=None):
        self.objects = []
        self.objectsDict = {}
        self.keepRunning = True
        self.sceneHandler = sceneHandler
        self.interactions = InteractionList()

        self.useInteractionsCursor = True
                    
    def addObject(self, obj, name):
        '''
            Args:
                obj (GameObject)
                name (str)
        '''
        self.objects.append(obj)
        self.objectsDict[name] = len(self.objects) - 1

    def getObject(self, name):
        return self.objects[self.objectsDict[name]]

    def removeObject(self, name):
        '''
            Raises:
                KeyError: If the name doesn't exist
        '''
        del self.objects[self.objectsDict[name]]

        for key in self.objectsDict:
            if self.objectsDict[key] > self.objectsDict[name]:
                self.objectsDict[key] -= 1

        del self.objectsDict[name]

    def update(self):
        '''To call at each iteration of the game loop'''
        for obj in self.objects:
            obj.update()

    def draw(self, drawingSurface):
        '''
            Args:
                drawingSurface (pygame.Surface)
        '''
        for obj in self.objects:
            drawingSurface.blit(obj.getSprite(), obj.getPos())

    def handleEvents(self, events):
        '''
            Args:
                events (list(pygame.event.Event))
        '''
        for event in events:
            if event.type == QUIT:
                self.keepRunning = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.keepRunning = False
            elif event.type == MOUSEMOTION:
                if self.interactions.touches(event.pos) and self.useInteractionsCursor:
                    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                else:
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
            elif event.type == MOUSEBUTTONDOWN:
                self.interactions.click(event)

    def setSceneHandler(self, sceneHandler):
        self.sceneHandler = sceneHandler

    def getSceneHandler(self):
        return self.sceneHandler

    def getKeepRunning(self):
        return self.keepRunning

