#!/usr/bin/env python3
import os
import pygame

class Animation:
    '''
        Args:
            clock (pygame.time.Clock)
            images (list(pygame.Surface))
            lifeSpans (list(int))
    '''
    def __init__(self, clock, images, lifeSpans):
        self.clock = clock
        self.images = images
        self.lifeSpans = lifeSpans

        self.spriteTime = 0
        self.spriteIndex = 0

        self.endAction = None

    def update(self):
        '''To call at each game loop's iteraction'''
        self.spriteTime += self.clock.get_time()

        while self.spriteTime >= self.lifeSpans[self.spriteIndex]:
            self.spriteTime -= self.lifeSpans[self.spriteIndex]
            self.incrementSpriteIndex()

    def reset(self):
        self.spriteIndex = self.spriteTime = 0

    def copy(self):
        '''(the attributes have the same reference)'''
        return Animation(self.clock, self.images, self.lifeSpans)

    def incrementSpriteIndex(self):
        self.spriteIndex += 1

        if self.spriteIndex >= len(self.images):
            self.spriteIndex = 0
            self.callEndAction()

    def callEndAction(self):
        if self.endAction is not None:
            self.endAction()
            self.endAction = None

    def setEndAction(self, action):
        ''' Set the action executed at the end of the animation's iteration '''
        self.endAction = action

    def getSprite(self):
        return None if len(self.images) <= 0 else self.images[self.spriteIndex]

    def getClock(self):
        return self.clock

    def getImages(self):
        return self.images

    def getLifeSpans(self):
        return self.lifeSpans

    def getEndAction(self):
        return self.endAction

def animationFromFolder(folderPath, clock, imageFunc):
    '''
        (The folder that contains an animation file)

        ANIMATION FILE TYPE (settings.anim):
        ------------------------------------
        [imageRelativePath]:[imageLifeSpan]
        [imageRelativePath]:[imageLifeSpan]
        [imageRelativePath]:[imageLifeSpan]
        [imageRelativePath]:[imageLifeSpan]
        ------------------------------------

        Args:
            folderPath (str)
            clock (pygame.Clock)
            imageFunc (func): The function used to get each image with the image path for parameter
    '''
    images, lifeSpans = [], []

    with open(os.path.abspath(folderPath + "/settings.anim"), 'r') as data:
        line = data.readline()

        while line != "":
            lineTab = line.split(':')

            images.append(imageFunc(os.path.abspath(folderPath + '/' + lineTab[0])))
            lifeSpans.append(int(lineTab[1]))

            line = data.readline()

    return Animation(clock, images, lifeSpans)

def convertImage(imgPath):
    return pygame.image.load(imgPath).convert()

def convertAlphaImage(imgPath):
    return pygame.image.load(imgPath).convert_alpha()
