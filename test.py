import sys

import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 800))
screen_rect = screen.get_rect()
vector = pygame.image.load("images/ship.bmp")
vector_rect = vector.get_rect()
vector_rect.center = screen_rect.center
vector_status = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pass
            # if event.key == pygame.K_RIGHT:
            #
            # elif event.key == pygame.K_LEFT:

        elif event.type == pygame.KEYUP:
            pass

    screen.fill("green")
    screen.blit(vector, vector_rect)
    pygame.display.flip()
