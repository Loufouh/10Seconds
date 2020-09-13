#!/usr/bin/env python3

import unittest
import sys

sys.path.insert(0, '..')

from src.GameObject import GameObject

class SpriteDummy:
    ''' Simplified Sprite class for testing.'''
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def get_width(self):
        return self.dimensions[0]

    def get_height(self):
        return self.dimensions[1]

class test_GameObject(unittest.TestCase):
    def setUp(self):
        self.object = GameObject([1, 3], SpriteDummy([0, 0]))

    def test_move(self):
        self.assertListEqual(self.object.getPos(), [1, 3])
        self.object.move([10, 25])
        self.assertListEqual(self.object.getPos(), [11, 28])

    def test_getDim(self):
        self.assertListEqual(self.object.getDim(), [0, 0])
        self.assertEqual(GameObject([12, 54], SpriteDummy([12, 45])).getDim(), [12, 45])

if __name__ == "__main__":
    unittest.main()
