import pygame
from constants import *

class Trex:
    def __init__(self, player_number):
        self.player_number = player_number
        self.load_images()
        self.image = self.run_img[0]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (50 + player_number * 100, GROUND_HEIGHT)
        self.y = self.rect.y
        self.is_jumping = False
        self.is_ducking = False
        self.jump_velocity = JUMP_HEIGHT
        self.animation_count = 0

    # def load_images(self):
    #     self.run_img = [
    #         pygame.image.load(f'assets/dino{self.player_number}_run1.png').convert_alpha(),
    #         pygame.image.load(f'assets/dino{self.player_number}_run2.png').convert_alpha()
    #     ]
    #     self.duck_img = [
    #         pygame.image.load(f'assets/dino{self.player_number}_duck1.png').convert_alpha(),
    #         pygame.image.load(f'assets/dino{self.player_number}_duck2.png').convert_alpha()
    #     ]
    #     self.jump_img = pygame.image.load(f'assets/dino{self.player_number}_jump.png').convert_alpha()

    def create_surface(self, width, height, color):
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        surface.fill(color)
        return surface
    def load_images(self):
        color = (0, 255, 0) if self.player_number == 1 else (0, 0, 255)
        self.run_img = [self.create_surface(40, 50, color) for _ in range(2)]
        self.duck_img = [self.create_surface(50, 30, color) for _ in range(2)]
        self.jump_img = self.create_surface(40, 50, color)

    def jump(self):
        if not self.is_jumping and not self.is_ducking:
            self.is_jumping = True

    def duck(self):
        if not self.is_jumping:
            self.is_ducking = True
            self.rect.y = GROUND_HEIGHT - self.duck_img[0].get_height()

    def update(self, keys):
        if self.player_number == 1:
            jump_key = pygame.K_w
            duck_key = pygame.K_s
        else:
            jump_key = pygame.K_UP
            duck_key = pygame.K_DOWN

        if keys[jump_key]:
            self.jump()
        elif keys[duck_key]:
            self.duck()
        else:
            self.is_ducking = False
            self.rect.bottomleft = (50 + self.player_number * 100, GROUND_HEIGHT)

        if self.is_jumping:
            self.y -= self.jump_velocity
            self.jump_velocity -= GRAVITY
            if self.jump_velocity < -JUMP_HEIGHT:
                self.is_jumping = False
                self.jump_velocity = JUMP_HEIGHT
                self.y = GROUND_HEIGHT - self.run_img[0].get_height()
            self.image = self.jump_img
        elif self.is_ducking:
            self.image = self.duck_img[self.animation_count // 5]
        else:
            self.image = self.run_img[self.animation_count // 5]

        self.animation_count = (self.animation_count + 1) % 10
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)