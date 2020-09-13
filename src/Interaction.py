#!/usr/bin/env python3

import pygame

class Interaction:
    '''
        Args:
            name (str)
            pos (list(int))
            dim (list(int))

        Attributes:
            name (str)
            pos (list(int))
            dim (list(int))
            actions (list(function)): The actions executed when the interaction is triggered
            isActive (bool)
    '''
    def __init__(self, name, pos, dim):
        self.name = name
        self.pos = pos
        self.dim = dim
        self.isActive = True
        self.actions = []

    def addAction(self, action):
        '''Add an action to the end of the execution list'''
        self.actions.append(action)

    def addAction_firstToExecute(self, action):
        '''Add an action to the begining of the execution list'''
        self.actions.insert(0, action)

    def clearActions(self):
        self.actions = []

    def click(self, event):
        '''
            Args:
                event (Pygame.event.Event)
        '''
        if self.touches(event.pos):
            for action in self.actions:
                action()

    def touches(self, pos):
        return self.isActive and pygame.Rect(self.pos, self.dim).collidepoint(pos)

    def toString(self):
        txt = self.name + ' '
        txt += str(self.pos[0]) + '-' + str(self.pos[1]) + ' '
        txt += str(self.dim[0]) + '-' + str(self.dim[1])

        return txt

    def equals(self, interaction):
        sameName = self.name == interaction.name
        samePos = self.pos == interaction.pos
        sameDim = self.dim == interaction.dim
        sameActions = self.actions == interaction.actions

        return sameName and samePos and sameDim and sameActions

    def setActive(self):
        self.isActive = True

    def setInactive(self):
        self.isActive = False

    def getActions(self):
        return self.actions

    def getIsActive(self):
        return self.isActive

    def getName(self):
        return self.name

def interactionFromString(string):
    name = string.split(' ')[0]
    pos = [int(exprs) for exprs in string.split(' ')[1].split('-')]
    dim = [int(exprs) for exprs in string.split(' ')[2].split('-')]

    return Interaction(name, pos, dim)

def interactionFromGameObject(obj, name):
    return Interaction(name, obj.getPos(), obj.getDim())
