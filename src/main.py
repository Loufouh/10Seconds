#!/usr/bin/env python3

import pygame

if False:
    import pygame._view

from SceneHandler import SceneHandler

from menu.Scene import Scene as MenuScene
from scene1.Scene import Scene as Scene1
from scene2.Scene import Scene as Scene2
from scene3.Scene import Scene as Scene3
from scene4.Scene import Scene as Scene4
from scene5.Scene import Scene as Scene5
from scene6.Scene import Scene as Scene6
from scene7.Scene import Scene as Scene7
from scene8.Scene import Scene as Scene8
from scene9.Scene import Scene as Scene9
from win.Scene import Scene as WinScene

from constants import WINDOW_DIMENSIONS

pygame.init()

clock = pygame.time.Clock()

sceneHandler = SceneHandler(clock, pygame.display.set_mode(WINDOW_DIMENSIONS))

sceneHandler.addScene(MenuScene(sceneHandler), "menu")
sceneHandler.addScene(Scene1(sceneHandler), "scene1")
sceneHandler.addScene(Scene2(sceneHandler), "scene2")
sceneHandler.addScene(Scene3(sceneHandler), "scene3")
sceneHandler.addScene(Scene4(sceneHandler), "scene4")
sceneHandler.addScene(Scene5(sceneHandler), "scene5")
sceneHandler.addScene(Scene6(sceneHandler), "scene6")
sceneHandler.addScene(Scene7(sceneHandler), "scene7")
sceneHandler.addScene(Scene8(sceneHandler), "scene8")
sceneHandler.addScene(Scene9(sceneHandler), "scene9")
sceneHandler.addScene(WinScene(sceneHandler), "winScene")

sceneHandler.setCurrentScene("menu")

while sceneHandler.getCurrentScene().getKeepRunning():
    sceneHandler.getCurrentScene().handleEvents(pygame.event.get())
    sceneHandler.getCurrentScene().update()
    sceneHandler.getCurrentScene().draw(sceneHandler.getDrawingSurface())

    pygame.display.flip()
    clock.tick()
