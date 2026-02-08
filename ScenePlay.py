#  Play scene - the main game play scene
import pygame
import pyghelpers
import pygwidgets
from Constants import *
from PhysicsObject import *

BOTTOM_RECT = (0, GAME_HEIGHT + 1, WINDOW_WIDTH,
                                WINDOW_HEIGHT - GAME_HEIGHT)
STATE_WAITING = 'waiting'
STATE_PLAYING = 'playing'

class ScenePlay(pyghelpers.Scene):

    def __init__(self, window):
        self.window = window

        self.controlsBackground = pygwidgets.Image(self.window,
                                        (0, GAME_HEIGHT),
                                        'images/controlsBackground.jpg')

        self.quitButton = pygwidgets.TextButton(self.window,
                                                (30, GAME_HEIGHT + 90),
                                                'quit',
                                                width=DEFAULT_BUTTON_WIDTH)

        self.settingsButton = pygwidgets.TextButton(self.window,
                                                    (190, GAME_HEIGHT + 90),
                                                      'settings',
                                                    width=DEFAULT_BUTTON_WIDTH)

        self.oPhysicsObject = PhysicsObject(self.window)

        self.oTimer = pyghelpers.CountUpTimer()
        self.dt = 0

        self.playingState = STATE_PLAYING

    def getSceneKey(self):
        return SCENE_PLAY

    def enter(self, data):
        self.oTimer.start()

    def reset(self):
        pass

    def handleInputs(self, eventsList, keyPressedList):
        if self.playingState == STATE_PLAYING:
            for event in eventsList:
                if event.type == pygame.KEYDOWN:
                    # Handle key presses
                    if event.key == pygame.K_UP:
                        self.oPhysicsObject.applyImpulse(yImpulse=-5)
                    if event.key == pygame.K_RIGHT:
                        self.oPhysicsObject.applyImpulse(xImpulse=5)
                    if event.key == pygame.K_LEFT:
                        self.oPhysicsObject.applyImpulse(xImpulse=-5)

            if keyPressedList[pygame.K_SPACE]:
                self.oPhysicsObject.applyForce(yForce=-1500)
            if keyPressedList[pygame.K_a]:
                self.oPhysicsObject.applyForce(xForce=-500)
            if keyPressedList[pygame.K_d]:
                self.oPhysicsObject.applyForce(xForce=500)

        for event in eventsList:
            if self.settingsButton.handleEvent(event):
                self.goToScene(SCENE_SETTINGS)

            if self.quitButton.handleEvent(event):
                self.quit()

    def update(self):
        if self.playingState != STATE_PLAYING:
            return  # only update when playing
        dt = self.oTimer.getTime()
        self.oPhysicsObject.update(dt)
        self.oTimer.start()

    def draw(self):
        self.window.fill(BLACK)

        #draw objects on top of background
        self.oPhysicsObject.draw()

        # Draw all the info at the bottom of the window
        self.controlsBackground.draw()
        self.quitButton.draw()
        self.settingsButton.draw()

    def leave(self):
        self.oTimer.stop()