#!/usr/bin/env python3

from Interaction import interactionFromString

class InteractionList:
    '''A group of interactions'''
    def __init__(self):
        self.interactions = []

    def add(self, interaction):
        self.interactions.append(interaction)

    def remove(self, name):
        indeces = []

        for i, interaction in enumerate(self.interactions):
            if interaction.getName() == name:
                indeces.append(i)

        for i in indeces:
            del self.interactions[i]

    def touches(self, pos):
        '''One of the interactions touches the position'''
        for interaction in self.interactions:
            if interaction.touches(pos):
                return True
        return False

    def click(self, event):
        for interaction in self.interactions:
            interaction.click(event)

    def setInactive(self):
        for interaction in self.interactions:
            interaction.setInactive()

    def setActive(self):
        for interaction in self.interactions:
            interaction.setActive()

    def getInteraction(self, name):
        for interaction in self.interactions:
            if interaction.getName() == name:
                return interaction
        return None

    def getInteractions(self):
        return self.interactions

def interactionListFromFile(filePath):
    '''
        File containing one interaction's toString by line
    '''
    interactionList = InteractionList()

    with open(filePath) as data:
        line = data.readline()

        while line != '':
            interactionList.add(interactionFromString(line))
            line = data.readline()

    return interactionList
