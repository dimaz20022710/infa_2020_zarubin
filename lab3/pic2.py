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
krasny = (255, 0, 0)
beliy = (255, 255, 255)

time = 0

FPS = 10
screen = pygame.display.set_mode((EcrX, EcrY))


def fon(sootnosheniye=0.5):
    """
    делает два прямоугольника: землю и небо
    :param sootnosheniye: высота земли к высоте неба
    :return:
    """
    rect(screen, siniy, (0, EcrY * (1 - sootnosheniye), EcrX, EcrY * sootnosheniye))
    rect(screen, zeleny, (0, 0, EcrX, EcrY * (1 - sootnosheniye)))


def sun(x=30, y=30, r=30, d=2):
    """
    рисует солнышко (не солнце, а именно детское солнышко)
    :param x: координата х центра солнца
    :param y: координата у центра солнца
    :param r: рариус солнца
    :param d: ширина солнечного луча
    :return: ничего))0)
    """
    circle(screen, zhelty, (x, y), r)
    for i in range(0, 90):
        line(screen, zhelty, (x, y), (x + 100 * np.sin(i), y + 100 * np.cos(i)), d)


def roja(x, y, r):
    """
    рисует рожу
    :param x: координата х центра рожи
    :param y: координата у центра рожи
    :param r: размер - радиур рожи
    :return: ))0)
    """
    circle(screen, koja, (x, y), r)
    circle(screen, cherny, (x + r // 3, int(round(y - 4 * r // 9))), r // 10)
    circle(screen, cherny, (x - r // 3, int(round(y - 4 * r // 9))), r // 10)
    circle(screen, cherny, (x, y), r // 10)
    arc(screen, cherny, (x - r // 3, y + r // 15, 2 * r // 3, r // 2), 4, 6)


def pocan(x=135, y=130, r=100):
    """
    рисует поцана
    :param x: координата х центра головы
    :param y: координата у центра головы
    :param r: коэффициент размера, примерно 2/5 высоты
    :return:
    """
    ellipse(screen, futbolka, (x - 35 * r // 100, y, 7 * r // 10, 18 * r // 10))
    line(screen, cherny, (x - 15 * r // 100, y + 17 * r // 10), (x - 55 * r // 100, y + 22 * r // 10), r // 20)
    line(screen, cherny, (x + 15 * r // 100, y + 17 * r // 10), (x + 55 * r // 100, y + 22 * r // 10), r // 20)
    line(screen, cherny, (x - 25 * r // 100, y + 4 * r // 10), (x - 75 * r // 100, y + 12 * r // 10), r // 20)
    line(screen, cherny, (x + 25 * r // 100, y + 4 * r // 10), (x + 75 * r // 100, y + 12 * r // 10), r // 20)
    roja(x, y, 3 * r // 10)


def morojenoe(x=60, y=250, r=10, fi):
    """

    :param x:
    :param y: 
    :param r: коэффициент размера, равен радиусу шариков
    :param fi: угол поворота мороженого
    :return:
    """
    polygon(screen, platye, [(x, y), (x, y - 3 * r), (x - 25 * r // 10, y - 15 * r // 10)])
    circle(screen, krasny, (x - 2 * r, 210), r)
    circle(screen, cherny, (x - 25 * r // 10, 225), r)
    circle(screen, beliy, (x - r, 218), r)


def pocanessa():
    polygon(screen, platye, [(230, 300), (400, 300), (315, 130)])
    line(screen, cherny, (300, 300), (250, 350), 5)
    line(screen, cherny, (340, 300), (390, 350), 5)
    line(screen, cherny, (300, 170), (225, 250), 5)
    line(screen, cherny, (330, 170), (370, 210), 5)
    line(screen, cherny, (370, 210), (410, 210), 5)
    roja(315, 130, 25)


def sharik():
    line(screen, (128, 128, 128), (410, 210), (470, 100), 2)
    ellipse(screen, (255, 0, 0), (460, 50, 40, 50))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    time = time + 1
    fon(0.6)
    sun()
    morojenoe()
    pocan(135, 130, 100)
    pocanessa()
    sharik()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
