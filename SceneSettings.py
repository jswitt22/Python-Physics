# High Scores scene
import pygwidgets
import pyghelpers
from Constants import *

class SceneSettings(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window

        self.quitButton = pygwidgets.TextButton(self.window,
                                                (30, 650),
                                                'quit',
                                                width=DEFAULT_BUTTON_WIDTH)

        self.backButton = pygwidgets.TextButton(self.window,
                                                (240, 650),
                                                'back',
                                                width=DEFAULT_BUTTON_WIDTH)

    def getSceneKey(self):
        return SCENE_SETTINGS

    def enter(self, newHighScoreValue=None):
        pass

    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.quitButton.handleEvent(event):
                self.quit()

            elif self.backButton.handleEvent(event):
                self.goToScene(SCENE_PLAY)

    def draw(self):
        self.window.fill(BLACK)
        self.quitButton.draw()
        self.backButton.draw()

    def respond(self, requestID):
        pass
