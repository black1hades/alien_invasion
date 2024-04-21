import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 800))
screen_rect = screen.get_rect()
vector = pygame.image.load("../images/ship.bmp")
vector_rect = vector.get_rect()
vector_rect.center = screen_rect.center
vector_status = False
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill("green")
    screen.blit(vector, vector_rect)
    pygame.display.flip()
