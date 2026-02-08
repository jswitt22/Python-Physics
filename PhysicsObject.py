import pygame
from Constants import *


class PhysicsObject:

    def __init__(self, window, stateVector=None):
        self.window = window

        if stateVector is None:
            self.x, self.y, self.vx, self.vy, self.ax, self.ay = 0, 0, 0, 0, 0, 0
        else:
            self.x, self.y, self.vx, self.vy, self.ax, self.ay = stateVector

        self.rect = pygame.Rect(self.x, self.y, DEFAULT_OBJECT_WIDTH, DEFAULT_OBJECT_WIDTH)

    def update(self):

        self.x += self.vx
        self.y += self.vy
        self.vx += self.ax
        self.vy += self.ay

        if self.y+self.rect.height >= GAME_HEIGHT:
            self.y = GAME_HEIGHT-self.rect.height
            self.vy = 0
            self.ay = 0
        else:
            self.ay = GRAVITY

        self.rect.update(self.x, self.y, DEFAULT_OBJECT_WIDTH, DEFAULT_OBJECT_WIDTH)
        pass

    def draw(self):
        pygame.draw.rect(self.window, WHITE, self.rect)
        print(self.x, self.y, self.vx, self.vy, self.ax, self.ay)
        pass