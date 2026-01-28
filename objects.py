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

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        #Player is a green square
        self.image = pygame.Surface((width,height))
        self.image.fill((0, 255, 0))  # Green color for player
        self.rect = self.image.get_rect(topleft = (x ,y)) # Player's rectangle
        self.mask = pygame.mask.from_surface(self.image)
        self.type = 'player' # Type identifier for player objects

class Spike (pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        #Spike is a red triangle
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))  # Transparent background
        pygame.draw.polygon(self.image, (255, 0 ,0), [(0, height), (width/2.0, 0), (width, height)])  # Red triangle
        self.rect = self.image.get_rect(topleft = (x ,y)) # Spike's rectangle
        self.mask = pygame.mask.from_surface(self.image)
        self.type = 'spike' # Type identifier for spike objects

class Pterodactyl(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        #In this game, the pterodactyl is represented as a red rhpmbus
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))  # Transparent background
        pygame.draw.polygon(self.image, (255, 0 , 0), [(width / 2.0, 0), (width, height / 2.0), (width / 2.0, height), (0, height / 2.0)]) # Red rhombus
        self.rect = self.image.get_rect(topleft = (x ,y)) # Pterodactyl's rectangle
        self.mask = pygame.mask.from_surface(self.image)
        self.type = 'pterodactyl' # Type identifier for pterodactyl objects