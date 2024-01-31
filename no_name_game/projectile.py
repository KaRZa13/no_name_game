import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 115
        self.rect.y = player.rect.y + 35
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # fait tourner le projectile
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity

        # verifier la collision avec un ennemi
        for enemy in self.player.game.check_collision(
            self, self.player.game.all_enemies
        ):
            self.remove()
            # inflige des dégâts
            enemy.damage(self.player.attack)

        # verifier si le projectile est toujours dans la fenêtre
        if self.rect.x > 1900:
            self.remove()
