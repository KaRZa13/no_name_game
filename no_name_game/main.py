import pygame
from player import Player
from game import Game

pygame.init()

# generation de la fenêtre du jeu
pygame.display.set_caption("Shoot 'em up")

# bouton "jouer"
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()

# charger le jeu
game = Game()

screen = pygame.display.set_mode((1920, 720))

# importation du background
background = pygame.image.load("assets/bg.jpg")

# Changement de la taille de l'image
nouvelle_taille_background = (1920, 720)
background = pygame.transform.scale(background, nouvelle_taille_background)

# importation du joueur
player = Player(Game)

# paramètre de temps
now = pygame.time.get_ticks()
last_shot = now
last_spawn = now
time_between_shot = 100
time_between_spawn = 1000

running = True

# boucle du jeu
while running:

    # appliquer l'arrière-plan
    screen.blit(background, (0, 0))

    # verifier si le jeu a commencé ou pas
    if game.is_playing:
        game.update_game(screen, player)
    else:
        # screen.blit(banner, (x, y)
        screen.blit(play_button, (0, 0))

    # mise à jour de l'écran
    pygame.display.flip()

    now = pygame.time.get_ticks()

    # gestion du spawn des premiers énnemies
    if now - last_spawn > time_between_spawn:
        game.spawn_enemy()
        last_spawn = now

    # gestion de la cadence de tir
    if game.pressed.get(pygame.K_SPACE) and now - last_shot > time_between_shot:
        game.player.launch_projectile()
        last_shot = now

    # si le joueur ferme la fenêtre
    for event in pygame.event.get():
        # verifier la fermeture
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Quitting")

        # détecter si un joueur lâche une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        # clique sur le bouton "jouer"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
