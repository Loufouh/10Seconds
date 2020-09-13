#!/usr/bin/env python3

import unittest
import sys

sys.path.insert(0, '..')

from CallFunctionsVerifier import CallFunctionsVerifier

from src.Interaction import Interaction, interactionFromString, interactionFromGameObject

class EventDummy: # pylint: disable=R0903
    def __init__(self, pos):
        self.pos = pos

class GameObjectDummy:
    def __init__(self, pos, dim):
        self.pos = pos
        self.dim = dim

    def getPos(self):
        return self.pos

    def getDim(self):
        return self.dim

class test_Interaction(unittest.TestCase):
    def setUp(self):
        self.interaction = Interaction('interaction', [0, 0], [10, 10])

    def test_addAction(self):
        self.interaction.addAction('a')
        self.interaction.addAction('b')

        self.assertListEqual(self.interaction.getActions(), ['a', 'b'])

    def test_addAction_firstToExecute(self):
        self.interaction.addAction_firstToExecute('a')
        self.interaction.addAction_firstToExecute('b')

        self.assertListEqual(self.interaction.getActions(), ['b', 'a'])

    def test_clearActions(self):
        self.interaction.addAction('a')
        self.interaction.addAction('b')

        self.interaction.clearActions()
        self.assertListEqual(self.interaction.getActions(), [])

    def test_setActive(self):
        self.interaction.setInactive()
        self.interaction.setActive()
        self.assertTrue(self.interaction.getIsActive())

    def test_setInactive(self):
        self.interaction.setActive()
        self.interaction.setInactive()
        self.assertFalse(self.interaction.getIsActive())

    def test_touches(self):
        self.assertTrue(self.interaction.touches([5, 6]))
        self.assertFalse(self.interaction.touches([3, 11]))

        self.interaction.setInactive()

        self.assertFalse(self.interaction.touches([0, 0]))
        self.assertFalse(self.interaction.touches([5, 6]))

    def test_click(self):
        callFunctionsVerifier = CallFunctionsVerifier()

        self.interaction.addAction(callFunctionsVerifier.function1)
        self.interaction.addAction(callFunctionsVerifier.function2)

        self.interaction.click(EventDummy([2, 12]))

        self.assertFalse(callFunctionsVerifier.called1)
        self.assertFalse(callFunctionsVerifier.called2)

        self.interaction.click(EventDummy([8, 5]))

        self.assertTrue(callFunctionsVerifier.called1)
        self.assertTrue(callFunctionsVerifier.called2)

        self.assertLess(callFunctionsVerifier.executionTime1, callFunctionsVerifier.executionTime2)

    def test_toString(self):
        self.assertEqual(self.interaction.toString(), "interaction 0-0 10-10")

    def test_interactionFromString(self):
        strInteraction = interactionFromString(self.interaction.toString())

        self.assertTrue(strInteraction.equals(self.interaction))

    def test_interactionFromGameObject(self):
        obj = GameObjectDummy([0, 0], [10, 10])
        interaction = interactionFromGameObject(obj, "interaction")
        awaitedInteraction = Interaction("interaction", [0, 0], [10, 10])

        self.assertTrue(interaction.equals(awaitedInteraction))

if __name__ == "__main__":
    unittest.main()
