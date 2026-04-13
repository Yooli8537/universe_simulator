import random
import pygame

class Particle:
    def __init__(self, body_type, x, y):
        # Position
        self.x = x
        self.y = y
        # Physics
        self.velocity_x = random.uniform(-1, 1)
        self.velocity_y = random.uniform(-1, 1)
        # Appearance
        self.radius = random.uniform(body_type["size"][0], body_type["size"][1])
        r = random.randint(body_type["color"][0][0], body_type["color"][1][0])
        g = random.randint(body_type["color"][0][1], body_type["color"][1][1])
        b = random.randint(body_type["color"][0][2], body_type["color"][1][2])
        self.color = (r, g, b)

    def draw(self, window):
        pygame.draw.circle(window, self.color, (int(self.x), int(self.y)), int(self.radius))

    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y