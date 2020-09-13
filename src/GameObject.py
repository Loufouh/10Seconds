#!/usr/bin/env python3

class GameObject:
    '''
        Entity displayable and updatable

        Args:
            pos (list(int))
            sprite (pygame.surface)
    '''
    def __init__(self, pos, sprite):
        self.pos = pos
        self.sprite = sprite

    def update(self):
        '''
            To call at each game loop iteration
        '''

    def move(self, translationVector):
        '''
            Vector translation

            Args:
                translationVector (list(int))
        '''
        self.pos = [a + b for a, b in zip(self.pos, translationVector)]

    def setSprite(self, sprite):
        self.sprite = sprite

    def setPos(self, pos):
        self.pos = pos

    def getDim(self):
        return [self.getSprite().get_width(), self.getSprite().get_height()]

    def getSprite(self):
        return self.sprite

    def getPos(self):
        return self.pos
