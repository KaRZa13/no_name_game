import pygame
from projectile import Projectile


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 300
        self.max_health = 300
        self.attack = 100
        self.velocity = 4
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("assets/player.png")
        self.image = pygame.transform.scale(self.image, (115, 100))
        self.rect = self.image.get_rect()
        self.rect.y = 300
        self.rect.x = 30

    def damage(self, amount):
        self.health -= amount
        if self.health >= 0:
            self.game.game_over()

    def update_heath_bar(self, game):
        self.game = game
        pygame.draw.rect(self.game.screen, (60, 63, 60), [5, 690, self.max_health, 10])
        pygame.draw.rect(self.game.screen, (111, 210, 46), [5, 690, self.health, 10])

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def move(self, dx, dy):
        new_x = self.rect.x + dx * self.velocity
        new_y = self.rect.y + dy * self.velocity

        if 0 <= new_x < 1850:
            self.rect.x = new_x

        if -50 <= new_y < 665:
            self.rect.y = new_y

    def handle_movement(self):
        keys = pygame.key.get_pressed()
        dx = keys[pygame.K_d] - keys[pygame.K_q]
        dy = keys[pygame.K_s] - keys[pygame.K_z]

        # Si le joueur appuie sur plusieurs touches de déplacement, normalisez le vecteur
        if dx != 0 and dy != 0:
            dx /= 1.41
            dy /= 1.41

        self.move(dx, dy)
