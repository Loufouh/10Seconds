#!/usr/bin/env python3

import unittest
import sys
import os

from ClockDummy import ClockDummy
from CallFunctionsVerifier import CallFunctionsVerifier

sys.path.insert(0, '..')

from src.Animation import Animation, animationFromFolder

class test_Animation(unittest.TestCase):
    def test_incrementSpriteIndex(self):
        animation = Animation(ClockDummy(1), ["img1", "img2", "img3"], [1, 1, 1])
        self.assertEqual(animation.getSprite(), "img1")
        animation.incrementSpriteIndex()
        self.assertEqual(animation.getSprite(), "img2")
        animation.incrementSpriteIndex()
        self.assertEqual(animation.getSprite(), "img3")
        animation.incrementSpriteIndex()
        self.assertEqual(animation.getSprite(), "img1")

    def test_update_basic(self):
        animation = Animation(ClockDummy(1), ["img1", "img2", "img3"], [1, 1, 1])

        self.assertEqual(animation.getSprite(), "img1")
        animation.update()
        self.assertEqual(animation.getSprite(), "img2")
        animation.update()
        self.assertEqual(animation.getSprite(), "img3")

    def test_update_advanced(self):
        animation = Animation(ClockDummy(3), ["img1", "img2", "img3"], [2, 1, 5])

        self.assertEqual(animation.getSprite(), "img1")
        animation.update()
        self.assertEqual(animation.getSprite(), "img3")
        animation.update()
        self.assertEqual(animation.getSprite(), "img3")
        animation.update()
        self.assertEqual(animation.getSprite(), "img1")
        animation.update()
        self.assertEqual(animation.getSprite(), "img3")

    def test_update_noLifeSpans(self):
        animation = Animation(ClockDummy(1), ["img1"], [])

        with self.assertRaises(IndexError):
            animation.update()

    def test_update_endAction(self):
        animation = Animation(ClockDummy(1), ["img1", "img2", "img3"], [1, 1, 1])
        callFunctionsVerifier = CallFunctionsVerifier()

        animation.setEndAction(callFunctionsVerifier.function1)

        animation.update()
        self.assertFalse(callFunctionsVerifier.called1)
        animation.update()
        self.assertFalse(callFunctionsVerifier.called1)
        animation.update()
        self.assertTrue(callFunctionsVerifier.called1)

    def test_update_endAction_bigTimePassed(self):
        animation = Animation(ClockDummy(3), ["img1", "img2", "img3"], [1, 1, 1])
        callFunctionsVerifier = CallFunctionsVerifier()

        animation.setEndAction(callFunctionsVerifier.function1)

        animation.update()
        self.assertTrue(callFunctionsVerifier.called1)

    def test_reset(self):
        animation = Animation(ClockDummy(1), ["img1", "img2"], [1, 1])

        animation.reset()
        self.assertEqual(animation.getSprite(), "img1")
        animation.update()
        animation.reset()
        self.assertEqual(animation.getSprite(), "img1")

    def test_copy(self):
        clock = ClockDummy(1)
        images = ['img1', 'img2']
        lifeSpans = [1, 1]

        copy = Animation(clock, images, lifeSpans).copy()

        self.assertIs(copy.getClock(), clock)
        self.assertIs(copy.getImages(), images)
        self.assertIs(copy.getLifeSpans(), lifeSpans)

    def test_setEndAction(self):
        animation = Animation(ClockDummy(1), ["img1", "img2", "img3"], [1, 1, 1])

        self.assertIsNone(animation.getEndAction())
        action = lambda: None
        animation.setEndAction(action)
        self.assertEqual(animation.getEndAction(), action)

    def test_callEndAction(self):
        animation = Animation(ClockDummy(1), ["img1", "img2", "img3"], [1, 1, 1])

        animation.callEndAction()
        self.assertIsNone(animation.getEndAction())
        animation.setEndAction(lambda: None)
        animation.callEndAction()
        self.assertIsNone(animation.getEndAction())

    def test_animationFromFolder_func_file1(self):
        clock = ClockDummy(1)
        filepath = "animation_files/file1"
        animation = animationFromFolder(filepath, clock, lambda imgPath: imgPath)

        self.assertIs(animation.getClock(), clock)
        self.assertListEqual(animation.getLifeSpans(), [600, 600])

        awaitedImages = [os.path.abspath(filepath + '/' + str(i)) for i in range(2)]
        self.assertListEqual(animation.getImages(), awaitedImages)

        filepath = "animation_files//file1/"
        animation = animationFromFolder(filepath, clock, lambda imgPath: imgPath)

        awaitedImages = [os.path.abspath(filepath + '/' + str(i)) for i in range(2)]
        self.assertListEqual(animation.getImages(), awaitedImages)

    def test_animationFromFolder_func_file2(self):
        clock = ClockDummy(1)
        filepath = "animation_files/file2"
        animation = animationFromFolder(filepath, clock, lambda imgPath: imgPath)

        self.assertListEqual(animation.getLifeSpans(), [21, 128, 74, 8])

        awaitedImages = [os.path.abspath(filepath + '/' + str(i)) for i in range(4)]
        self.assertListEqual(animation.getImages(), awaitedImages)

if __name__ == "__main__":
    unittest.main()
