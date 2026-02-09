import pygame
import pygwidgets
from Constants import *


class PhysicsObject:

    def __init__(self, window, stateVector=None):
        self.window = window

        if stateVector is None:
            self.x, self.y, self.vx, self.vy, self.ax, self.ay = 0, 0, 0, 0, 0, 0
        else:
            self.x, self.y, self.vx, self.vy, self.ax, self.ay = stateVector
        self.xPrev = self.x
        self.yPrev = self.y

        self.mass = 1.0 #placeholder for now
        self.xForce, self.yForce = 0, 0

        self.oDebugText = pygwidgets.DisplayText(self.window,
                                                 (0, 0),
                                                 textColor=WHITE,)

        self.rect = pygame.Rect(self.x, self.y, DEFAULT_OBJECT_WIDTH, DEFAULT_OBJECT_WIDTH)

    def collideWithBounds(self, restitution=0.5):
        # Left
        if self.x < 0:
            self.x = 0
            self.vx = -self.vx * restitution
        # Right
        if self.x + self.rect.width > WINDOW_WIDTH:
            self.x = WINDOW_WIDTH - self.rect.width
            self.vx = -self.vx * restitution
        # Top
        if self.y < 0:
            self.y = 0
            self.vy = -self.vy * restitution
        # Bottom
        if self.y + self.rect.height > GAME_HEIGHT:
            self.y = GAME_HEIGHT - self.rect.height
            self.vy = -self.vy * restitution

    def setDebugText(self):
        positionString = f"x: {self.x:4.0f}, y: {self.y:4.0f}"
        velocityString = f"vx: {self.vx:4.0f}, vy: {self.vy:4.0f}"
        accelerationString = f"ax: {self.ax:4.0f}, ay: {self.ay:4.0f}"
        strList = [positionString, velocityString, accelerationString]
        self.oDebugText.setText(strList)

    def applyImpulse(self, xImpulse=0, yImpulse=0):
        if xImpulse == 0 and yImpulse == 0:
            return
        self.vx += xImpulse
        self.vy += yImpulse

    def applyForce(self, xForce=0, yForce=0):
        if xForce == 0 and yForce == 0:
            return
        self.xForce += xForce
        self.yForce += yForce

    def update(self, dt):
        # Velocity Verlet method
        # Set initial acceleration
        ax0, ay0 = self.ax, self.ay
        # Calculate acceleration from forces
        self.ax = self.xForce/self.mass
        self.ay = GRAVITY + self.yForce/self.mass
        # Update Position
        self.x += self.vx * dt + 0.5 * self.ax * dt * dt
        self.y += self.vy * dt + 0.5 * self.ay * dt * dt
        # Recompute acceleration based on position (if this is the case)
        ax1, ay1 = self.ax, self.ay
        # Update Velocity
        self.vx += 0.5 * (ax0 + ax1) * dt
        self.vy += 0.5 * (ay0 + ay1) * dt

        self.xForce, self.yForce = 0, 0

        # Check wall collision
        self.collideWithBounds()

        self.rect.update(self.x, self.y, DEFAULT_OBJECT_WIDTH, DEFAULT_OBJECT_WIDTH)
        self.setDebugText()

    def draw(self):
        pygame.draw.rect(self.window, WHITE, self.rect)
        self.oDebugText.draw()
        pass