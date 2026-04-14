import pygame
import sys
import random
import settings
import math
from entities import bodies
from entities import particles

pygame.init()

window = pygame.display.set_mode((settings.WINDOW_SIZE, settings.WINDOW_HEIGHT))

options = []
weights = []
for body in bodies.ALL_BODIES:
    if body["name"] in settings.ACTIVE_BODIES:
        options.append(body)
        weights.append(body["rarity"])

particle_list = []
if settings.MODE == "GALAXY":
    x = settings.GALAXY_CENTER_X
    y = settings.GALAXY_CENTER_Y
    particle_list.append(particles.Particle(bodies.galaxy_center, x, y, 0, 0))
    particle_list[0].pinned = True

while len(particle_list) <= settings.MAX_BODIES:
    center_mass = particle_list[0].mass

    x = random.randint(0, settings.WINDOW_SIZE)
    y = random.randint(0, settings.WINDOW_HEIGHT)
# Watching them all unfold from the same position is fascinating.
# If you want to see for yourself, comment out the x & y definitions above and remove the comment for the definitions below.
#    x = settings.GALAXY_CENTER_X
#    y = settings.GALAXY_CENTER_Y
    chosen_body = random.choices(options, weights)[0]

    dx = x - settings.GALAXY_CENTER_X
    dy = y - settings.GALAXY_CENTER_Y
    distance = math.hypot(dx, dy)
    orbital_velocity = math.sqrt(settings.GRAVITY_CONSTANT * center_mass / distance)
    perpendicular_vel_x = (-dy / distance) * orbital_velocity
    perpendicular_vel_y = (dx / distance) * orbital_velocity

    particle_list.append(particles.Particle(chosen_body, x, y, perpendicular_vel_x, perpendicular_vel_y))

clock = pygame.time.Clock()

while True:
    dt = clock.tick(settings.FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clears the screen. Commenting this out will cause trails which is also cool
    window.fill((0, 0, 0))

    for i in range(len(particle_list)):
        for j in range(i + 1, len(particle_list)):
            particle_list[i].apply_gravity(particle_list[j], dt)

    for particle in particle_list:
        particle.update(dt)
        particle.draw(window)

    pygame.display.flip()
