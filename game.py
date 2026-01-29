import pygame
from sprites import Player, Ground, Spike, Pterodactyl, score_display, game_over_display
from spawner import Spawner
from physics import accelerate_speed

pygame.init()
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()

world_speed = 200  # Initial world speed
acceleration = 0.1  # Pixels per second squared
max_speed = 500  # Maximum world speed

ground = Ground(0, 450, 800, 50)
player = Player(100, 300, 50, 50)

# initial hazards (optional)
hazards = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
score_display_sprite = score_display(10, 10)
game_over_display_sprite = game_over_display(400, 250)
all_sprites.add(ground, player, hazards, score_display_sprite) 
score = 0
highscore = 0
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
    score += 1
    score_display_sprite.update(score)

    world_speed = accelerate_speed(world_speed, acceleration, dt, max_speed)   

    for h in hazards:
        h.speed = world_speed

    spawner.scroll_speed = world_speed

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
        game_over_display_image = game_over_display_sprite.image
        all_sprites.add(game_over_display_sprite)

        if score > highscore:
            highscore = score
            print(f"New Highscore: {highscore}")
            score_display_sprite.update(score)
        running = False  # or reset, etc.

    screen.fill((30, 30, 30))
    all_sprites.draw(screen)
    pygame.display.flip()