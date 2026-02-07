# Splash scene - first scene the user sees
import pygwidgets
import pyghelpers
from Constants import *

class SceneSplash(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window

        self.startButton = pygwidgets.TextButton(self.window,
                                                 (250, 500),
                                                 'start',
                                                 width=DEFAULT_BUTTON_WIDTH)

        self.quitButton = pygwidgets.TextButton(self.window,
                                                (30, 650),
                                                'quit',
                                                width=DEFAULT_BUTTON_WIDTH)

        self.highScoresButton = pygwidgets.TextButton(self.window,
                                                      (470, 650),
                                                      'settings',
                                                      width=DEFAULT_BUTTON_WIDTH)

    def getSceneKey(self):
        return SCENE_SPLASH

    def handleInputs(self, events, keyPressedList):
        for event in events:
            if self.startButton.handleEvent(event):
                self.goToScene(SCENE_PLAY)
            elif self.quitButton.handleEvent(event):
                self.quit()
            elif self.highScoresButton.handleEvent(event):
                self.goToScene(SCENE_SETTINGS)

    def draw(self):
        self.window.fill(BLACK)
        self.startButton.draw()
        self.quitButton.draw()
        self.highScoresButton.draw()
