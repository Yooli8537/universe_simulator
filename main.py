import pygame
import sys
import random
import settings
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
while len(particle_list) <= settings.MAX_BODIES:
        x = random.randint(0, settings.WINDOW_SIZE)
        y = random.randint(0, settings.WINDOW_HEIGHT)
        chosen_body = random.choices(options, weights)[0]
        particle_list.append(particles.Particle(chosen_body, x, y))

while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

        # Clears the screen
        window.fill((0, 0, 0))

        for i in range(len(particle_list)):
                for j in range(i + 1, len(particle_list)):
                        particle_list[i].apply_gravity(particle_list[j])

        for particle in particle_list:
                particle.draw(window)

        pygame.display.flip()
