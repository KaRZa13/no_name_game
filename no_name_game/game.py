import pygame
from player import Player
from enemy import Enemy


class Game:
    def __init__(self):
        # générer le joueur quand on lance une partie
        self.is_playing = False
        self.screen = pygame.display.set_mode((1520, 720))
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # generation groupe d'ennemies
        self.all_enemies = pygame.sprite.Group()
        self.all_enemies.add(self.all_enemies)
        self.enemy_count = 0
        self.max_enemies = 10
        self.pressed = {}
        self.enemy_spawn_delay = 1500


    def start(self):
        self.is_playing = True
        self.spawn_enemy()

    def game_over(self):
        if self.player.health <= 0:
            self.all_enemies = pygame.sprite.Group()
            self.player.health = self.player.max_health
            self.is_playing = False

    def update_game(self, screen, player):
        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser barre de vie
        player.update_heath_bar(self)

        # récupérer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # récupérer les énemies du jeu
        for enemy in self.all_enemies:
            enemy.update()

        # appliquer l'image des enemies
        self.all_enemies.draw(screen)

        # appliquer l'image des projectiles
        self.player.all_projectiles.draw(screen)

        # verifier quels déplacements veut faire le joueur
        self.player.handle_movement()

    # Système de collision avec les enemies
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_enemy(self):
        if self.enemy_count < self.max_enemies:
            enemy = Enemy(self)
            self.all_enemies.add(enemy)
            self.enemy_count += 1
