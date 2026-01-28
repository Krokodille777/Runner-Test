import pygame
from sprites import Player, Ground, Spike, Pterodactyl
from spawner import Spawner

pygame.init()
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()

ground = Ground(0, 450, 800, 50)
player = Player(100, 300, 50, 50)

# initial hazards (optional)
hazards = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(ground, player, hazards)
platforms = pygame.sprite.Group(ground)


spawner = Spawner(
    screen_width=800,
    ground_top_y=450,
    hazards_group=hazards,
    draw_group=all_sprites
)

running = True
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if player.on_ground:
                player.vel.y = -800

    spawner.update(dt)
    hazards.update(dt)                  # hazards only need dt
    player.update(dt, platforms)        # player collid
    if pygame.sprite.spritecollideany(player, hazards, pygame.sprite.collide_mask):
        print("GAME OVER")
        running = False  # or reset, etc.

    screen.fill((30, 30, 30))
    all_sprites.draw(screen)
    pygame.display.flip()