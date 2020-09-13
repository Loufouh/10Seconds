#!/usr/bin/env python3

import pygame.mouse

class SceneHandler:
    '''
        Group of all the scenes and their links

        Args:
            clock (pygame.time.Clock)
            drawingSurface (pygame.Surface)
    '''
    def __init__(self, clock, drawingSurface):
        self.clock = clock
        self.drawingSurface = drawingSurface

        self.scenes = []
        self.scenesDict = {}

        self.currentScene = None

    def addScene(self, scene, name):
        '''
            Args:
                scene (Scene)
                name (str)
        '''
        self.scenes.append(scene)
        self.scenesDict[name] = len(self.scenes) - 1

    def setCurrentScene(self, name):
        '''
            Args:
                name (str)

            Raises:
                KeyError: If the name doesn't correspond to any scene
        '''
        self.currentScene = self.scenes[self.scenesDict[name]]
        pygame.mouse.set_cursor(*pygame.cursors.arrow)

    def getScene(self, name):
        '''
            Args:
                name (str)

            Raises:
                KeyError: If none of the scenes correspond to the name

            Returns:
                scene (Scene)
        '''
        return self.scenes[self.scenesDict[name]]

    def getScenes(self):
        return self.scenes

    def getCurrentScene(self):
        return self.currentScene

    def getDrawingSurface(self):
        return self.drawingSurface
