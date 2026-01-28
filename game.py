import pygame
from pygame.locals import *
from sprites import Player, Ground, Spike, Pterodactyl


pygame.init()
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()
colliders = pygame.sprite.Group()


ground = Ground(0, 450, 800, 50)
player = Player(100, 300, 50, 50)
spike = Spike(600, 400, 50, 50)
pterodactyl = Pterodactyl(700, 200, 60, 40)


all_sprites.add(ground, player, spike, pterodactyl)
colliders.add(ground, spike, pterodactyl)

running = True
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if player.on_ground:
                player.vel.y = -800  # Jump velocity
    all_sprites.update(dt, colliders)

    screen.fill((30, 30, 30))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()