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


class Ball:

    def __init__(self, cor):
        self.x = cor[0]
        self.y = cor[1]
        self.r = cor[2]

    def draw_ball(self, x, y):
        self.x = x
        self.y = y
        circle(screen, self.color(), (self.x, self.y), self.r)

    def ball_coordinates(self):
        return (self.x, self.y, self.r)

    def color(self):
        color = COLORS[randint(0, 5)]
        return color


def coordinates():
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    return (x, y, r)

'''def new_ball():
    """рисует новый шарик """
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)'''


pygame.display.update()
clock = pygame.time.Clock()
finished = False

success = 0
fail = 0

a = Ball(coordinates())

while not finished:
    clock.tick(FPS)
    a.draw_ball(coordinates()[0], coordinates()[1])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #a.draw_ball(*event.pos)
            print(event.pos, a.ball_coordinates())
            if (event.pos[0] - a.ball_coordinates()[0])**2 + (event.pos[1] - a.ball_coordinates()[1])**2 < a.ball_coordinates()[2]**2:
                success += 1
            else:
                fail += 1
    print(a.ball_coordinates())
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
print(success, fail)