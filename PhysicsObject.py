import pygame
import pygwidgets
from Constants import *


class PhysicsObject:

    def __init__(self, window, stateVector=None):
        self.window = window

        if stateVector is None:
            self.x, self.y, self.ax, self.ay = 0, 0, 0, 0
        else:
            self.x, self.y, self.ax, self.ay = stateVector
        self.xPrev = self.x
        self.yPrev = self.y

        self.oDebugText = pygwidgets.DisplayText(self.window,
                                                 (0, 0),
                                                 textColor=WHITE,)

        self.rect = pygame.Rect(self.x, self.y, DEFAULT_OBJECT_WIDTH, DEFAULT_OBJECT_WIDTH)

    def collideWithBounds(self, restitution=0):
        # Left
        if self.x < 0:
            vx = self.x - self.xPrev
            self.x = 0
            vx = -vx * restitution
            self.xPrev = self.x - vx
        # Right
        if self.x + self.rect.width > WINDOW_WIDTH:
            vx = self.x - self.xPrev
            self.x = WINDOW_WIDTH - self.rect.width
            vx = -vx * restitution
            self.xPrev = self.x - vx
        # Top
        if self.y < 0:
            vy = self.y - self.yPrev
            self.y = 0
            vy = -vy * restitution
            self.yPrev = self.y - vy
        # Bottom
        if self.y + self.rect.height > GAME_HEIGHT:
            vy = self.y - self.yPrev
            self.y = GAME_HEIGHT - self.rect.height
            vy = -vy * restitution
            self.yPrev = self.y - vy

    def setDebugText(self):
        positionString = f"x: {self.x:4.0f}, y: {self.y:4.0f}"
        accelerationString = f"ax: {self.ax:4.0f}, ay: {self.ay:4.0f}"
        strList = [positionString, accelerationString]
        self.oDebugText.setText(strList)

    def update(self, dt, xImpulse=0, yImpulse=0):
        # Verlet method
        # Apply forces
        self.ax = 0 # sum forces and calculate ax
        self.ay = GRAVITY + 0 # sum forces and calculate ay
        # Apply impulses if any
        self.xPrev = self.xPrev - xImpulse * dt
        self.yPrev = self.yPrev - yImpulse * dt
        # Verlet integration
        xPrev, yPrev = self.x, self.y
        self.x = 2*self.x - self.xPrev + self.ax * dt * dt
        self.y = 2*self.y - self.yPrev + self.ay * dt * dt
        self.xPrev, self.yPrev = xPrev, yPrev

        # Check wall collision
        self.collideWithBounds()

        self.rect.update(self.x, self.y, DEFAULT_OBJECT_WIDTH, DEFAULT_OBJECT_WIDTH)
        self.setDebugText()

    def draw(self):
        pygame.draw.rect(self.window, WHITE, self.rect)
        self.oDebugText.draw()
        pass