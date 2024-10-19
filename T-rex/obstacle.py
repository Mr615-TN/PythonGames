import pygame
import random
from constants import *

class Obstacle:
    def __init__(self):
        self.load_images()
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.reset()

    def create_surface(self, width, height, color):
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        surface.fill(color)
        return surface
    def load_images(self):
        self.images = [
            self.create_surface(20, 40, (255, 0, 0)),  # Red rectangle for cactus
            self.create_surface(40, 20, (128, 0, 128))  # Purple rectangle for bird
        ]

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def reset(self):
        self.x = SCREEN_WIDTH
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        if self.image == self.images[1]:  # bird
            self.y = random.choice([GROUND_HEIGHT - 60, GROUND_HEIGHT - 100])
        else:  # cactus
            self.y = GROUND_HEIGHT - self.rect.height
        self.rect.bottomleft = (self.x, self.y)
        self.speed = OBSTACLE_SPEED

    def draw(self, screen):
        screen.blit(self.image, self.rect)