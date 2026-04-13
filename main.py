import pygame
import sys
import random
import settings
from entities import bodies
from entities import particles

pygame.init()

window = pygame.display.set_mode((settings.WINDOW_SIZE, settings.WINDOW_HEIGHT))

particle_list = []
while len(particle_list) <= settings.MAX_BODIES:
        x = random.randint(0, settings.WINDOW_SIZE)
        y = random.randint(0, settings.WINDOW_HEIGHT)
#        for name in len(settings.ACTIVE_BODIES):
#            body = bodies.name
        particle_list.append(particles.Particle(bodies.brown_dwarf, x, y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for particle in particle_list:
         particle.draw(window)

    pygame.display.flip()
