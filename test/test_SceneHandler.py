#!/usr/bin/env python3

import unittest
import sys

sys.path.insert(0, '..')

from src.SceneHandler import SceneHandler

class SceneDummy:
    '''Simplified Scene for testing.'''
    def __init__(self):
        self.drawn = False
        self.updated = False

    def update(self):
        self.updated = True

    def draw(self, surface): # pylint: disable=W0613
        self.drawn = True

class test_SceneHandler(unittest.TestCase):
    def setUp(self):
        self.sceneHandler = SceneHandler("clock", "window")
        self.scenes = [SceneDummy() for i in range(10)]

        for i, scene in enumerate(self.scenes):
            self.sceneHandler.addScene(scene, 'scene' + str(i))

    def test_addScene(self):
        dummy1 = SceneDummy()

        self.assertNotIn(dummy1, self.sceneHandler.getScenes())

        self.sceneHandler.addScene(dummy1, 'dummy1')

        self.assertIn(dummy1, self.sceneHandler.getScenes())
        self.assertIs(self.sceneHandler.getScene("dummy1"), dummy1)

if __name__ == "__main__":
    unittest.main()
