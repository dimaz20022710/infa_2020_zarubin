import pygame
from pygame.draw import *
import numpy as np

pygame.init()
# razmery ecrana
EcrX = 500
EcrY = 400
# KTO? (WHO?) – Цвета (Colors)
siniy = (0, 255, 0)
zeleny = (0, 0, 128)
zhelty = (255, 255, 0)
futbolka = (128, 128, 128)
cherny = (0, 0, 0)
koja = (255, 165, 0)
platye = (128, 0, 0)

FPS = 10
screen = pygame.display.set_mode((EcrX, EcrY))


def fon(sootnosheniye=0.5):
    """
    :param sootnosheniye: высота земли к высоте неба
    :return:
    """
    rect(screen, (0, 255, 0), (0, EcrY * (1 - sootnosheniye), EcrX, EcrY * sootnosheniye))
    rect(screen, (0, 0, 128), (0, 0, EcrX, EcrY * (1 - sootnosheniye)))


def sun(x=30, y=30, r=30, d=2):
    """
    :param x: координата х центра солнца
    :param y: координата у центра солнца
    :param r: рариус солнца
    :param d: ширина солнечного луча
    :return: ничего))0)
    """
    circle(screen, zhelty, (x, y), r)
    for i in range(0, 90):
        line(screen, zhelty, (x, y), (x + 100 * np.sin(i), y + 100 * np.cos(i)), d)


def roja():
    circle(screen, koja, (135, 130), 30)
    circle(screen, cherny, (145, 117), 3)
    circle(screen, cherny, (125, 117), 3)
    circle(screen, cherny, (135, 130), 3)
    arc(screen, cherny, (125, 132, 20, 15), 4, 6)


def pocan():
    ellipse(screen, futbolka, (100, 130, 70, 180))
    line(screen, cherny, (120, 300), (80, 350), 5)
    line(screen, cherny, (150, 300), (190, 350), 5)
    line(screen, cherny, (110, 170), (60, 250), 5)
    line(screen, cherny, (160, 170), (225, 250), 5)
    roja()


def morojenoe():
    polygon(screen, (128, 0, 0), [(60, 250), (60, 220), (20, 235)])
    circle(screen, (255, 0, 0), (30, 230), 10)
    circle(screen, (0, 0, 0), (35, 225), 10)
    circle(screen, (255, 255, 255), (50, 220), 10)


def pocanessa():
    polygon(screen, platye, [(230, 300), (400, 300), (315, 130)])
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


def sharik():
    line(screen, (128, 128, 128), (410, 210), (470, 100), 2)
    ellipse(screen, (255, 0, 0), (460, 50, 40, 50))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    fon(0.4)
    sun()
    morojenoe()
    pocan()
    pocanessa()
    sharik()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
