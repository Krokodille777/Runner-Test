import random
import pygame
from sprites import Spike, Pterodactyl

class Spawner:
    def __init__(self, screen_width, ground_top_y, hazards_group, draw_group):
        self.screen_width = screen_width
        self.ground_top_y = ground_top_y
        self.hazards = hazards_group
        self.draw_group = draw_group

        self.spawn_x_buffer = 80
        self.min_gap = 200
        self.max_gap = 400

        self.ptero_y_choices = [
            ground_top_y - 150,
            ground_top_y - 200,
            ground_top_y - 250
        ]

        self.scroll_speed = 450

    def _rightmost_obstacle_right(self):
        if len(self.hazards) == 0:
            return 0
        return max(s.rect.right for s in self.hazards.sprites())

    def update(self, dt):
        if len(self.hazards) == 0:
            self._spawn_one(self.screen_width + self.spawn_x_buffer)
            return

        rightmost_right = self._rightmost_obstacle_right()
        gap_target = random.randint(self.min_gap, self.max_gap)

        if rightmost_right < self.screen_width - gap_target:
            self._spawn_one(self.screen_width + self.spawn_x_buffer)

    def _spawn_one(self, x_pos):
        kind = random.choices(
            population=["spike", "ptero"],
            weights=[0.65, 0.35],
            k=1
        )[0]

        if kind == "spike":
            obj = Spike(x_pos, 0, 50, 50)
            obj.rect.bottom = self.ground_top_y
        else:
            y = random.choice(self.ptero_y_choices)
            obj = Pterodactyl(x_pos, y, 60, 40)

        obj.pos = pygame.Vector2(obj.rect.topleft)
        obj.speed = self.scroll_speed

        self.hazards.add(obj)
        self.draw_group.add(obj)
