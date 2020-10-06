import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (255, 255, 255), (0, 0, 400, 400))
circle(screen, (255, 255, 0), (200, 175), 150)
circle(screen, (0, 0, 0), (200, 175), 150, 2)
circle(screen, (255, 0, 0), (150, 115), 30)
circle(screen, (255, 0, 0), (250, 115), 30)
circle(screen, (0, 0, 0), (250, 115), 10)
circle(screen, (0, 0, 0), (150, 115), 10)
rect(screen, (0, 0, 0), (100, 220, 200, 30))
polygon(screen, (0, 0, 0), [(110, 35), (100, 45), (190, 110), (200, 90)])
polygon(screen, (0, 0, 0), [(310, 35), (300, 55), (240, 105), (220, 90)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
