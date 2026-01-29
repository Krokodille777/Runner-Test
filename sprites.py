import pygame
from pygame.locals import *


class Ground (pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill((0, 0, 0))  # Black color for ground
        self.rect = self.image.get_rect(topleft = (x ,y))
        self.mask = pygame.mask.from_surface(self.image)
        self.type = 'ground' # Type identifier for ground objects

class Obstacles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos = pygame.math.Vector2(0, 0)
        self.speed = 20

    def update(self, dt, *args):
        self.pos.x -= self.speed * dt
        self.rect.x = round(self.pos.x)

        if self.rect.right < 0:
            self.kill()


class Spike(Obstacles):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        pygame.draw.polygon(self.image, (255, 0 ,0),
                            [(0, height), (width/2.0, 0), (width, height)])
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)

        self.pos = pygame.math.Vector2(self.rect.topleft)


class Pterodactyl(Obstacles):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        pygame.draw.polygon(self.image, (255, 0, 0),
                            [(width/2.0, 0), (width, height/2.0),
                             (width/2.0, height), (0, height/2.0)])
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)

        self.pos = pygame.math.Vector2(self.rect.topleft)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        #Player is a green square
        self.image = pygame.Surface((width,height))
        self.image.fill((0, 255, 0))  # Green color for player
        self.rect = self.image.get_rect(topleft = (x ,y)) # Player's rectangle
        self.mask = pygame.mask.from_surface(self.image)
        self.type = 'player' # Type identifier for player objects

        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.vel = pygame.math.Vector2(0, 0)
        self.on_ground = False

    def update(self, dt, colliders):
        from physics import apply_gravity, move_and_collide

        apply_gravity(self, dt)
        move_and_collide(self, colliders, dt)




class score_display(pygame.sprite.Sprite):
    def __init__(self, x, y, font_size=30):
        super().__init__()
        self.font = pygame.font.Font(None, font_size)
        self.color = (255, 255, 255)  # White color for score text
        self.pos = (x, y)
        self.score = 0
        self.image = self.font.render(f"Score: {self.score}", True, self.color)
        self.rect = self.image.get_rect(topleft=self.pos)

    def update(self, score):
        if score != self.score:
            self.score = score
            self.image = self.font.render(f"Score: {self.score}", True, self.color)
            self.rect = self.image.get_rect(topleft=self.pos)

    def display_highscore(self, highscore):
        self.image = self.font.render(f"Highscore: {highscore}", True, self.color)
        self.rect = self.image.get_rect(topleft=self.pos)
    

class game_over_display(pygame.sprite.Sprite):
    def __init__(self, x, y, font_size=50):
        super().__init__()
        self.font = pygame.font.Font(None, font_size)
        self.color = (255, 0, 0)  # Red color for game over text
        self.pos = (x, y)
        self.image = self.font.render("GAME OVER", True, self.color)
        self.rect = self.image.get_rect(center=self.pos)