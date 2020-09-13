#!/usr/bin/env python3

import unittest
import sys

sys.path.insert(0, '..')

from CallFunctionsVerifier import CallFunctionsVerifier

from src.Interaction import Interaction
from src.InteractionList import InteractionList, interactionListFromFile

class EventDummy: # pylint: disable=R0903
    def __init__(self, pos):
        self.pos = pos

class test_Interaction(unittest.TestCase):
    def setUp(self):
        self.interactionList = InteractionList()

    def test_add(self):
        interaction1 = Interaction("interaction1", [], [])
        interaction2 = Interaction("interaction2", [], [])

        self.interactionList.add(interaction1)
        self.interactionList.add(interaction2)

        self.assertIn(interaction1, self.interactionList.getInteractions())
        self.assertIn(interaction2, self.interactionList.getInteractions())

    def test_remove(self):
        interaction1 = Interaction("interaction1", [], [])
        interaction2 = Interaction("interaction2", [], [])

        self.interactionList.add(interaction1)
        self.interactionList.add(interaction2)

        self.interactionList.remove('interaction2')

        self.assertNotIn(interaction2, self.interactionList.getInteractions())

    def test_touches(self):
        interaction1 = Interaction("interaction1", [2, 10], [20, 30])
        interaction2 = Interaction("interaction2", [100, 200], [54, 3])

        self.interactionList.add(interaction1)
        self.interactionList.add(interaction2)

        self.assertTrue(self.interactionList.touches([10, 20]))
        self.assertTrue(self.interactionList.touches([124, 201]))
        self.assertFalse(self.interactionList.touches([44, 89]))

    def test_click(self):
        callFunctionsVerifier = CallFunctionsVerifier()

        interaction1 = Interaction("interaction1", [2, 10], [20, 30])
        interaction2 = Interaction("interaction2", [100, 200], [54, 3])

        interaction1.addAction(callFunctionsVerifier.function1)
        interaction2.addAction(callFunctionsVerifier.function2)

        self.interactionList.add(interaction1)
        self.interactionList.add(interaction2)

        self.interactionList.click(EventDummy([23, 72]))

        self.assertFalse(callFunctionsVerifier.called1)
        self.assertFalse(callFunctionsVerifier.called2)

        self.interactionList.click(EventDummy([10, 20]))

        self.assertTrue(callFunctionsVerifier.called1)
        self.assertFalse(callFunctionsVerifier.called2)

        self.interactionList.click(EventDummy([101, 202]))

        self.assertTrue(callFunctionsVerifier.called2)

    def test_setInactive(self):
        self.interactionList.add(Interaction("interaction1", [], []))
        self.interactionList.add(Interaction("interaction2", [], []))

        self.interactionList.setInactive()

        self.assertFalse(self.interactionList.getInteractions()[0].getIsActive())
        self.assertFalse(self.interactionList.getInteractions()[1].getIsActive())

    def test_setActive(self):
        self.interactionList.add(Interaction("interaction1", [], []))
        self.interactionList.add(Interaction("interaction2", [], []))

        self.interactionList.setInactive()
        self.interactionList.setActive()

        self.assertTrue(self.interactionList.getInteractions()[0].getIsActive())
        self.assertTrue(self.interactionList.getInteractions()[1].getIsActive())

    def test_getInteraction(self):
        interaction1 = Interaction("interaction1", [], [])
        interaction2 = Interaction("interaction2", [], [])

        self.interactionList.add(interaction1)
        self.interactionList.add(interaction2)

        self.assertEqual(self.interactionList.getInteraction("interaction1"), interaction1)
        self.assertEqual(self.interactionList.getInteraction("interaction2"), interaction2)

    def test_interactionListFromFile(self):
        interactionList = interactionListFromFile('interactionList_files/file1.inter')

        awaitedInteraction1 = Interaction("interaction1", [599, 143], [162, 82])
        awaitedInteraction2 = Interaction("interaction2", [229, 533], [159, 113])

        self.assertTrue(interactionList.getInteraction("interaction1").equals(awaitedInteraction1))
        self.assertTrue(interactionList.getInteraction("interaction2").equals(awaitedInteraction2))

if __name__ == "__main__":
    unittest.main()
