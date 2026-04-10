import pygame
import sys
import random
import settings
from entities import bodies

pygame.init()

window = pygame.display.set_mode((settings.WINDOW_SIZE, settings.WINDOW_HEIGHT))
bodies_count = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if bodies_count <= settings.MAX_BODIES:
        bd_r = random.randint(bodies.brown_dwarf["color"][0][0], bodies.brown_dwarf["color"][1][0])
        bd_g = random.randint(bodies.brown_dwarf["color"][0][1], bodies.brown_dwarf["color"][1][1])
        bd_b = random.randint(bodies.brown_dwarf["color"][0][2], bodies.brown_dwarf["color"][1][2])
        bd_col = (bd_r, bd_g, bd_b)

        bd_x = random.randint(0, settings.WINDOW_SIZE)
        bd_y = random.randint(0, settings.WINDOW_HEIGHT)
        pygame.draw.circle(window, bd_col, (bd_x, bd_y), 5)
        bodies_count += 1

    pygame.display.flip()
