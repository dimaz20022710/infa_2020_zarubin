import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def click(event):
    print(x, y, r)
    print(event.pos[0], event.pos[1])

'''рисует новый шарик '''
def new_ball():
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

success = 0
fail = 0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (event.pos[0] - x)**2 + (event.pos[1] - y)**2 < r**2:
                success += 1
            else:
                fail += 1
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
print(success, fail)