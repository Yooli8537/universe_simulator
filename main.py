import pygame
import sys
import settings

pygame.init()

pygame.display.set_mode((500, 500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
