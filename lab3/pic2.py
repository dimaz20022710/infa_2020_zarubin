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
zakryto = 0

FPS = 10
screen = pygame.display.set_mode((EcrX, EcrY))

pygame.font.SysFont('arial', 36)
f1 = pygame.font.Font(None, 20)


def fon(sootnosheniye=0.5, tip=0):
    """
    делает два прямоугольника: землю и небо
    :param tip: задает вид фона
    :param sootnosheniye: высота земли к высоте неба
    :return:
    """
    if tip == 0:
        rect(screen, siniy, (0, EcrY * (1 - sootnosheniye), EcrX, EcrY * sootnosheniye))
        rect(screen, zeleny, (0, 0, EcrX, EcrY * (1 - sootnosheniye)))


def muzica(n):
    file1 = 'muzhickij_dozhd1.mp3'
    file0 = 'Muzhickij_dozhd.mp3'
    file2 = 'muzhickij_dozhd2.mp3'
    pygame.init()
    pygame.mixer.init()
    if n == 1:
        pygame.mixer.music.load(file1)
    if n == 0:
        pygame.mixer.music.load(file0)
    if n == 2:
        pygame.mixer.music.load(file2)
    pygame.mixer.music.play(-1)


def music_box(t):
    if t % 2 == 0:
        lines(screen, krasny, False, [[EcrX - 6, 12], [EcrX - 3, 9], [EcrX - 3, 6], [EcrX - 9, 0], [EcrX - 9, 21]])
        polygon(screen, krasny,
                [[EcrX - 9, 21], [EcrX - 9, 18], [EcrX - 12, 15], [EcrX - 15, 15], [EcrX - 18, 18], [EcrX - 18, 21],
                 [EcrX - 15, 24], [EcrX - 12, 24]])
    if t % 2 == 1:
        line(screen, krasny, [EcrX - 20, 0], [EcrX, 20])
        line(screen, krasny, [EcrX, 0], [EcrX - 20, 20])
        polygon(screen, beliy, [[EcrX - 200, 0], [EcrX, 0], [EcrX, 150], [EcrX - 200, 150]])
        screen.blit(f1.render('мужицкий дождь', 1, (0, 0, 0)), (EcrX - 200, 0))
        screen.blit(f1.render('мужицкий дождь', 1, (0, 0, 0)), (EcrX - 200, 25))
        screen.blit(f1.render('мужицкий дождь', 1, (0, 0, 0)), (EcrX - 200, 50))
        screen.blit(f1.render('мужицкий дождь', 1, (0, 0, 0)), (EcrX - 200, 75))
        screen.blit(f1.render('мужицкий дождь', 1, (0, 0, 0)), (EcrX - 200, 100))
        screen.blit(f1.render('мужицкий дождь', 1, (0, 0, 0)), (EcrX - 200, 125))
    return 0


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
    :param r: коэффициент размера, примерно 1/3 высоты
    :return:
    """
    ellipse(screen, futbolka, (x - 35 * r // 100, y, 7 * r // 10, 18 * r // 10))
    line(screen, cherny, (x - 15 * r // 100, y + 17 * r // 10), (x - 55 * r // 100, y + 25 * r // 10), r // 20)
    line(screen, cherny, (x + 15 * r // 100, y + 17 * r // 10), (x + 55 * r // 100, y + 25 * r // 10), r // 20)
    line(screen, cherny, (x - 25 * r // 100, y + 4 * r // 10), (x - 75 * r // 100, y + 12 * r // 10), r // 20)
    line(screen, cherny, (x + 25 * r // 100, y + 4 * r // 10), (x + 75 * r // 100, y + 12 * r // 10), r // 20)
    roja(x, y, 3 * r // 10)


def morojenoe(x=60, y=250, r=10, fi=0):
    """

    :param x: координата х точки острия вафельного стаканчика
    :param y: координата у точки острия вафельного стаканчика
    :param r: коэффициент размера, равен радиусу шариков
    :param fi: угол поворота мороженого от горизонтали
    :return: ))0)
    """
    polygon(screen, platye,
            [[x, y], [x - 4 * r * np.sin(fi) - 2 * r * np.cos(fi), y - 4 * r * np.cos(fi) + 2 * r * np.sin(fi)],
             [x - 4 * r * np.sin(fi) + 2 * r * np.cos(fi), y - 4 * r * np.cos(fi) - 2 * r * np.sin(fi)]])
    circle(screen, krasny,
           [int(round(x - 4.25 * r * np.sin(fi) - r * np.cos(fi))),
            int(round(y - 4.25 * r * np.cos(fi) + r * np.sin(fi)))], r)
    circle(screen, zhelty,
           [int(round(x - 4.25 * r * np.sin(fi) + r * np.cos(fi))),
            int(round(y - 4.25 * r * np.cos(fi) - r * np.sin(fi)))], r)
    circle(screen, beliy, [int(round(x - 5.5 * r * np.sin(fi))), int(round(y - 5.5 * r * np.cos(fi)))], r)


def pocanessa(x=300, y=130, r=100):
    """
    рисует поцанессу
    :param x: координата х центра головы
    :param y: координата у центра головы
    :param r: коэффициент размера, примерно 1/3 высоты
    :return:
    """
    line(screen, cherny, (x - r // 10, y + 17 * r // 10), (x - 6 * r // 10, y + 25 * r // 10), r // 20)
    line(screen, cherny, (x + 2 * r // 10, y + 17 * r // 10), (x + 7 * r // 10, y + 25 * r // 10), r // 20)
    line(screen, cherny, (x - 1 * r // 10, y + 4 * r // 10), (x - 9 * r // 10, y + 12 * r // 10), r // 20)
    line(screen, cherny, (x + 1 * r // 10, y + 4 * r // 10), (x + 5 * r // 10, y + 8 * r // 10), r // 20)
    line(screen, cherny, (x + 5 * r // 10, y + 8 * r // 10), (x + 9 * r // 10, y + 8 * r // 10), r // 20)
    polygon(screen, platye, [(x - 6 * r // 10, y + 17 * r // 10), (x + 6 * r // 10, y + 17 * r // 10), (x, y)])
    roja(x, y, r // 4)


def sharik():
    line(screen, (128, 128, 128), (390, 210), (450, 95), 2)
    ellipse(screen, (255, 0, 0), (440, 50, 40, 50))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

fon(0.6)
muzica(0)

while not finished:
    clock.tick(FPS)
    time = time + 1
    fon(0.6)
    sun(30, 30, 30, 2)
    morojenoe(60, 250, 10, 7)
    pocan(140, 130, 100)
    pocanessa(300, 130, 100)
    sharik()
    music_box(zakryto)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                cursor_pos = event.pos
                if (cursor_pos[0] > EcrX - 20) and (cursor_pos[1] < 20):
                    zakryto = zakryto + 1
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
