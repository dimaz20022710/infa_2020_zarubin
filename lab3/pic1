import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 400))

rect(screen, (0, 255, 0), (0, 200, 500, 200))
rect(screen, (0, 0, 128), (0, 0, 500, 200))

circle(screen, (255, 255, 0), (30, 30), 30)
line(screen, (255, 255, 0), (30, 30), (80, 50), 7)
line(screen, (255, 255, 0), (30, 30), (70, 80), 7)
line(screen, (255, 255, 0), (30, 30), (55, 84), 7)
line(screen, (255, 255, 0), (30, 30), (40, 87), 7)
line(screen, (255, 255, 0), (20, 30), (25, 80), 7)
line(screen, (255, 255, 0), (30, 30), (87, 30), 7)

ellipse(screen, (128, 128, 128), (100, 130, 70, 180))
line(screen, (0, 0, 0), (120, 300), (80, 350), 5)
line(screen, (0, 0, 0), (150, 300), (190, 350), 5)
line(screen, (0, 0, 0), (110, 170), (60, 250), 5)
line(screen, (0, 0, 0), (160, 170), (225, 250), 5)
circle(screen, (255, 165, 0), (135, 130), 30)
circle(screen, (0, 0, 0), (145, 117), 3)
circle(screen, (0, 0, 0), (125, 117), 3)
circle(screen, (0, 0, 0), (135, 130), 3)
arc(screen, (0, 0, 0), (125, 132, 20, 15), 4, 6)

polygon(screen, (128, 0, 0), [(60, 250), (60, 220), (20, 235)])
circle(screen, (255, 0, 0), (30, 230), 10)
circle(screen, (0, 0, 0), (35, 225), 10)
circle(screen, (255, 255, 255), (50, 220), 10)

polygon(screen, (128, 0, 0), [(230, 300), (400, 300), (315, 130)])
line(screen, (0, 0, 0), (300, 300), (250, 350), 5)
line(screen, (0, 0, 0), (340, 300), (390, 350), 5)
line(screen, (0, 0, 0), (300, 170), (225, 250), 5)
line(screen, (0, 0, 0), (330, 170), (370, 210), 5)
line(screen, (0, 0, 0), (370, 210), (410, 210), 5)
circle(screen, (255, 165, 0), (315, 130), 30)
circle(screen, (0, 0, 0), (325, 117), 3)
circle(screen, (0, 0, 0), (305, 117), 3)
circle(screen, (0, 0, 0), (315, 130), 3)
arc(screen, (0, 0, 0), (305, 132, 20, 15), 4, 6)

line(screen, (128, 128, 128), (410, 210), (470, 100), 2)
ellipse(screen, (255, 0, 0), (460, 50, 40, 50))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
