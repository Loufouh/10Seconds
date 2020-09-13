#!/usr/bin/env python3

import sys

sys.path.insert(0, '../src')

from GameObject import GameObject # pylint: disable=C0413

class AnimatedGameObject(GameObject):
    '''
        Args:
            pos (list(int))
    '''
    def __init__(self, pos):
        super().__init__(pos, sprite=None)
        self.animations = {}
        self.currentAnimationName = None

    def update(self):
        '''To call at each game loop's iteration'''
        if self.currentAnimationName in self.animations:
            self.animations[self.currentAnimationName].update()

    def addAnimation(self, animation, name):
        self.animations[name] = animation

    def isCurrentAnimationName(self, name):
        return self.currentAnimationName == name

    def setAnimation(self, name, nextAnimationName=None):
        '''
            Set the playing animation

            Raises:
                KeyError: If the animation doesn't exist
        '''
        if name not in self.animations:
            raise KeyError()
        self.currentAnimationName = name
        self.animations[name].reset()

        if nextAnimationName is not None:
            action = lambda: self.setAnimation(nextAnimationName)
            self.animations[self.currentAnimationName].setEndAction(action)

    def getAnimation(self, name):
        '''
            Raises:
                KeyError: If the animation doesn't exist
        '''
        return self.animations[name]

    def getCurrentAnimation(self):
        if self.currentAnimationName not in self.animations:
            return None
        return self.animations[self.currentAnimationName]
    
    def getCurrentAnimationName(self):
        return self.currentAnimationName

    def getSprite(self):
        if self.currentAnimationName not in self.animations:
            return None
        return self.animations[self.currentAnimationName].getSprite()
