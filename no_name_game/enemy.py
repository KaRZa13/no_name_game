import pygame
import random
import math

LARGEUR_ECRAN = 1920
HAUTEUR_ECRAN = 720

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, image_path, max_health=100, attack=100, velocity=1):
        super().__init__()
        self.game = game
        self.health = max_health
        self.max_health = max_health
        self.attack = attack
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()
        self.rect.x = LARGEUR_ECRAN + 50
        self.rect.y = random.randint(0, HAUTEUR_ECRAN)
        self.angle = 0
        self.velocity = velocity

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.rect.x = LARGEUR_ECRAN + 50
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
            self.rect.x = LARGEUR_ECRAN + 50

class Enemy2(pygame.sprite.Sprite):
    def __init__(self, game, image_path, max_health=100, attack=100, velocity=1):
        super().__init__()  # Appel de la méthode __init__ de la classe parente
        self.game = game
        self.health = max_health
        self.max_health = max_health
        self.attack = attack
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()
        self.rect.x = LARGEUR_ECRAN + 50
        self.rect.y = random.randint(0, HAUTEUR_ECRAN)
        self.angle = 0
        self.velocity = velocity

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.rect.x = LARGEUR_ECRAN + 50
            self.health = self.max_health

    def update(self):
        super().update()
        self.rect.move_ip(-self.velocity, 0)
        if self.rect.right < 0:
            self.kill()
        if self.rect.x < -200 or self.health == 0:
            self.health = self.max_health
            self.rect.x = LARGEUR_ECRAN + 50

