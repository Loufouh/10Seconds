#!/usr/bin/env python3

import unittest
import sys

sys.path.insert(0, '..')

from src.Scene import Scene

class ObjectDummy:
    """Simplified GameObject for testing"""

    def __init__(self, pos, sprite):
        self.pos = pos
        self.sprite = sprite

        self.updated = False

    def update(self):
        self.updated = True

    def getSprite(self):
        return self.sprite

    def getPos(self):
        return self.pos

class SurfaceDummy: # pylint: disable=R0903
    """Simplified surface for testing"""
    def __init__(self):
        self.drawnDict = {}

    def blit(self, sprite, pos):
        self.drawnDict[sprite] = pos

class test_Scene(unittest.TestCase):
    def setUp(self):
        self.scene = Scene()

        self.objs = [ObjectDummy([i]*2, -i) for i in range(100)]

        for i, obj in enumerate(self.objs):
            self.scene.addObject(obj, i)

    def test_addObject(self):
        for i, obj in enumerate(self.objs):
            self.assertIs(self.scene.getObject(i), obj)

    def test_removeObject(self):
        self.scene.removeObject(0)

        with self.assertRaises(KeyError):
            self.scene.getObject(0)

    def test_update(self):
        for obj in self.objs:
            self.assertFalse(obj.updated)

        self.scene.update()

        for obj in self.objs:
            self.assertTrue(obj.updated)

    def test_draw(self):
        surface = SurfaceDummy()

        self.assertEqual(len(surface.drawnDict.keys()), 0)
        self.scene.draw(surface)

        for obj in self.objs:
            self.assertTrue(obj.getSprite() in surface.drawnDict)

if __name__ == "__main__":
    unittest.main()
