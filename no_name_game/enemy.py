import pygame
import math
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 100
        self.image = pygame.image.load("assets/alien.png")
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()
        self.rect.x = 1800
        self.rect.y = 465
        self.angle = 0
        self.velocity = 1

    def damage(self, amount):
        # infliger les dégâts
        self.health -= amount
        if self.health <= 0:
            # respawn
            self.rect.x = 1800
            self.health = self.max_health

    def update(self):
        amplitude = 250
        frequency = 0.01
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
            self.rect.y = amplitude * math.sin(self.angle) + 300
            self.angle += frequency
        else:
            self.health = 0
            self.game.player.damage(self.attack)

        if self.rect.x < -200 or self.health == 0:
            self.health = self.max_health
            self.rect.x = 1800
