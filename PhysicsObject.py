import pygame
import pygwidgets

class PhysicsObject:

    def __init__(self, window, stateVector=None, gravity=9.81, mass=1.0, width=1.0, height=1.0, pixelsPerMeter=25, environmentWidth=1000, environmentHeight=1000, displayColor=(255,255,255), debugColor=(255,255,255)):
        self.window = window

        #physics and size
        self.gravity = gravity
        self.mass = mass
        self.width, self.height = width, height
        if stateVector is None:
            self.x, self.y, self.vx, self.vy, self.ax, self.ay = 0, 0, 0, 0, 0, 0
        else:
            self.x, self.y, self.vx, self.vy, self.ax, self.ay = stateVector
        self.xForce, self.yForce = 0, 0

        #conversions
        self.pixelsPerMeter = pixelsPerMeter
        self.environmentWidth = environmentWidth / pixelsPerMeter
        self.environmentHeight = environmentHeight / pixelsPerMeter
        self.displayWidth, self.displayHeight = width * pixelsPerMeter, height * pixelsPerMeter
        self.displayX, self.displayY = self.x * pixelsPerMeter, self.y * pixelsPerMeter

        self.color = displayColor



        self.oDebugText = pygwidgets.DisplayText(self.window,
                                                 (0, 0),
                                                 textColor=debugColor)

        self.rect = pygame.Rect(self.displayX, self.displayY, self.displayWidth, self.displayHeight)

    def displayConversions(self):
        self.displayX, self.displayY = self.x * self.pixelsPerMeter, self.y * self.pixelsPerMeter

    def collideWithBounds(self, restitution=0):
        # Left
        if self.x < 0:
            self.x = 0
            self.vx = -self.vx * restitution
        # Right
        if self.x + self.width > self.environmentWidth:
            self.x = self.environmentWidth - self.width
            self.vx = -self.vx * restitution
        # Top
        if self.y < 0:
            self.y = 0
            self.vy = -self.vy * restitution
        # Bottom
        if self.y + self.height > self.environmentHeight:
            self.y = self.environmentHeight - self.height
            self.vy = -self.vy * restitution

    def setDebugText(self):
        positionString = f"x: {self.x:6.2f}, y: {self.y:6.2f}"
        velocityString = f"vx: {self.vx:6.2f}, vy: {self.vy:6.2f}"
        accelerationString = f"ax: {self.ax:6.2f}, ay: {self.ay:6.2f}"
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
        self.ay = self.gravity + self.yForce/self.mass
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

        #update the display state
        self.displayConversions()
        self.rect.update(self.displayX, self.displayY, self.displayWidth, self.displayHeight)
        self.setDebugText()

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)
        self.oDebugText.draw()