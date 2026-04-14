import random
import pygame
import math
import settings

class Particle:
    def __init__(self, body_type, x, y, velocity_x, velocity_y):
        # Appearance
        self.radius = random.uniform(body_type["size"][0], body_type["size"][1])
        r = random.randint(body_type["color"][0][0], body_type["color"][1][0])
        g = random.randint(body_type["color"][0][1], body_type["color"][1][1])
        b = random.randint(body_type["color"][0][2], body_type["color"][1][2])
        self.color = (r, g, b)
        # Position
        self.x = x
        self.y = y
        # Physics
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.mass = self.radius * body_type["density"]
        self.pinned = False

    def draw(self, window):
        pygame.draw.circle(window, self.color, (int(self.x), int(self.y)), int(self.radius))

    def update(self, dt):
        if not self.pinned:
            self.x += self.velocity_x * dt
            self.y += self.velocity_y * dt

    def apply_gravity(self, other, dt):
        distance = math.hypot(other.x - self.x, other.y - self.y)
        force = settings.GRAVITY_CONSTANT * (self.mass * other.mass) / (distance ** 2 + settings.SOFTENING ** 2)
        angle = math.atan2(other.y - self.y, other.x - self.x)

        force_x = math.cos(angle) * force
        force_y = math.sin(angle) * force

        self.velocity_x += (force_x / self.mass) * dt
        self.velocity_y += (force_y / self.mass) * dt
        other.velocity_x -= (force_x / other.mass) * dt
        other.velocity_y -= (force_y / other.mass) * dt