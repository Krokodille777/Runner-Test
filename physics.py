import pygame
from pygame.locals import *
#And now import classes from sprites.py
from sprites import Ground, Player, Spike, Pterodactyl



# Gravity

GRAVITY = 2200  # Pixels per second squared


def apply_gravity(player, dt: float):

    player.vel.y += GRAVITY * dt

def move_and_collide(player, colliders, dt: float):

    player.on_ground = False


    player.pos.y += player.vel.y * dt
    player.rect.y = round(player.pos.y)

    for c in colliders:
        if pygame.sprite.collide_mask(player, c):
            if player.vel.y > 0:  # Falling
                player.rect.bottom = c.rect.top
                player.pos.y = player.rect.y
                player.vel.y = 0
                player.on_ground = True
            elif player.vel.y < 0:  # Jumping
                player.rect.top = c.rect.bottom
                player.pos.y = player.rect.y
                player.vel.y = 0



# Hazard & Scrolling functions


def check_hazard_collision(player, hazards):

    for hazard in hazards:
        if pygame.sprite.collide_mask(player, hazard):
            return True
    return False


def reset_player_position(player, x: int, y: int):
    player.pos = pygame.math.Vector2(x, y)
    player.rect.topleft = (x, y)
    player.vel = pygame.math.Vector2(0, 0)
    player.on_ground = False


# Hazard movement and offscreen check functions

def move_hazard(hazard, speed: float, dt : float):
    hazard.pos.x -= speed * dt
    hazard.rect.x = round(hazard.pos.x)

def is_hazard_offscreen(hazard, screen_width: int):
    #if spike is off the left side of the screen, it will be despawned
    despawn_x = -hazard.rect.width #offscreen to the left
    return hazard.rect.right < despawn_x

def reset_hazard_position(hazard, x: int, y: int):
    hazard.pos = pygame.math.Vector2(x, y)
    hazard.rect.topleft = (x, y)

