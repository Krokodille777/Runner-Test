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