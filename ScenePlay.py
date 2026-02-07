#  Play scene - the main game play scene
import pygame
import pyghelpers
import pygwidgets
from Constants import *

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

        self.highScoresButton = pygwidgets.TextButton(self.window,
                                                      (190, GAME_HEIGHT + 90),
                                                      'settings',
                                                      width=DEFAULT_BUTTON_WIDTH)

        self.playingState = STATE_WAITING

    def getSceneKey(self):
        return SCENE_PLAY

    def enter(self, data):
        pass

    def reset(self):
        pass

    def handleInputs(self, eventsList, keyPressedList):
        if self.playingState == STATE_PLAYING:
            for event in eventsList:
                if event.type == pygame.KEYDOWN:
                    pass
                    # Handle key presses

        for event in eventsList:
            if self.highScoresButton.handleEvent(event):
                self.goToScene(SCENE_SETTINGS)

            if self.quitButton.handleEvent(event):
                self.quit()

    def update(self):
        if self.playingState != STATE_PLAYING:
            return  # only update when playing

    def draw(self):
        self.window.fill(BLACK)

        # Draw all the info at the bottom of the window
        self.controlsBackground.draw()
        self.quitButton.draw()
        self.highScoresButton.draw()

    def leave(self):
        pass