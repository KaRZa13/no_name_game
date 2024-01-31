import pygame
from player import Player
from enemy import Enemy, Enemy2
import random

pygame.init()



class Game:
    def __init__(self):
        self.is_playing = False
        self.screen = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)

        self.all_enemies = pygame.sprite.Group()
        self.all_enemies2 = pygame.sprite.Group()

        # Appeler la méthode pour générer les ennemis
        self.generate_enemies()

        self.enemy_count = 0
        self.max_enemies = 10
        self.pressed = {}
        self.enemy_spawn_delay = 1500

    def generate_enemies(self):
        # Générer les ennemis au démarrage
        self.all_enemies.add(Enemy(self, "assets/alien.png"))
        self.all_enemies2.add(Enemy2(self, "assets/mechant.png"))

    def start(self):
        self.is_playing = True
        self.spawn_enemy()

    def game_over(self):
        if self.player.health <= 0:
            self.all_enemies = pygame.sprite.Group()
            self.all_enemies2 = pygame.sprite.Group()
            self.player.health = self.player.max_health
            self.is_playing = False

    def update_game(self, screen, player):
        screen.blit(self.player.image, self.player.rect)
        player.update_heath_bar(self)

        for projectile in self.player.all_projectiles:
            projectile.move()

        for enemy in self.all_enemies:
            enemy.update()

        for enemy2 in self.all_enemies2:
            enemy2.update()

        self.all_enemies.draw(screen)
        self.all_enemies2.draw(screen)

        self.player.all_projectiles.draw(screen)
        self.player.handle_movement()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_enemy(self):
        if self.enemy_count < self.max_enemies:
            image_path = "assets/alien.png"
            enemy = Enemy(self, image_path)
            self.all_enemies.add(enemy)

            image_path2 = "assets/mechant.png"
            enemy2 = Enemy2(self, image_path2)
            self.all_enemies2.add(enemy2)

            self.enemy_count += 1

# Fermeture de pygame
pygame.quit()

