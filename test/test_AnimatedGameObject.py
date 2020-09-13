#!/usr/bin/env python3

import unittest
import sys

from ClockDummy import ClockDummy

sys.path.insert(0, '..')

from src.AnimatedGameObject import AnimatedGameObject
from src.Animation import Animation

class AnimationDummy:
    def __init__(self, images):
        self.images = images
        self.updated = False
        self.isReset = False

    def getSprite(self):
        return self.images[0]

    def update(self):
        self.updated = True

    def reset(self):
        self.isReset = True

class test_AnimatedGameObject(unittest.TestCase):
    def setUp(self):
        self.obj = AnimatedGameObject([0, 0])
        self.anims = [AnimationDummy([1, 2, 3]) for _ in range(2)]

        self.obj.addAnimation(self.anims[0], "anim0")
        self.obj.addAnimation(self.anims[1], "anim1")

    def test_addAnimation(self):
        self.assertIs(self.obj.getAnimation("anim0"), self.anims[0])
        self.assertIs(self.obj.getAnimation("anim1"), self.anims[1])

        with self.assertRaises(KeyError):
            self.obj.getAnimation("falseName")

    def test_setAnimation(self):
        self.assertIsNone(self.obj.getCurrentAnimation())
        self.obj.setAnimation("anim0")
        self.assertTrue(self.obj.getCurrentAnimation().isReset)
        self.assertEqual(self.obj.getCurrentAnimation(), self.anims[0])
        self.obj.setAnimation("anim1")
        self.assertTrue(self.obj.getCurrentAnimation().isReset)
        self.assertEqual(self.obj.getCurrentAnimation(), self.anims[1])

        with self.assertRaises(KeyError):
            self.obj.setAnimation("falseAnim")

    def test_setAnimation_nextAnimationName(self):
        obj = AnimatedGameObject([0, 0])
        anim1 = Animation(ClockDummy(1), ["img1", "img2"], [1, 1])
        anim2 = Animation(ClockDummy(1), ["img3", "img4"], [1, 1])

        obj.addAnimation(anim1, "anim1")
        obj.addAnimation(anim2, "anim2")

        obj.setAnimation("anim1", nextAnimationName="anim2")

        obj.update()
        self.assertEqual(obj.getCurrentAnimation(), anim1)
        obj.update()
        self.assertEqual(obj.getCurrentAnimation(), anim2)

    def test_isCurrentAnimationName(self):
        obj = AnimatedGameObject([0, 0])

        anim1 = Animation(ClockDummy(1), ["img1", "img2"], [1, 1])
        anim2 = Animation(ClockDummy(1), ["img3", "img4"], [1, 1])

        obj.addAnimation(anim1, "anim1")
        obj.addAnimation(anim2, "anim2")

        obj.setAnimation("anim1")

        self.assertTrue(obj.isCurrentAnimationName("anim1"))
        self.assertFalse(obj.isCurrentAnimationName("anim2"))

    def test_update(self):
        for anim in self.anims:
            self.assertFalse(anim.updated)

        self.obj.update()

        for anim in self.anims:
            self.assertFalse(anim.updated)

        self.obj.setAnimation("anim0")

        self.obj.update()

        self.assertTrue(self.anims[0].updated)
        self.assertFalse(self.anims[1].updated)

    def test_getSprite(self):
        self.assertIsNone(self.obj.getSprite())

        self.obj.setAnimation("anim0")

        self.assertEqual(self.obj.getSprite(), self.anims[0].getSprite())

if __name__ == "__main__":
    unittest.main()
