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
muzlo = 0
vybor = 0

FPS = 10
screen = pygame.display.set_mode((EcrX, EcrY))

pygame.font.SysFont('arial', 36)
f1 = pygame.font.Font(None, 20)


def muzica(n):
    """
    включает выбранную музыку
    :param n: задаёт конкретный файл песни
    :return: none
    """
    file0 = 'Russkaya_narodnaya.mp3'
    file1 = 'Pelennor_Fields.mp3'
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


def music_box(tip, cursor=(1000, 1000)):
    """
    если тип = 1, показывает кликабельную ноту в углу экрана, иначе показывает кликабельный список песен
    :param tip: выбирает, что показывать – ноту или список
    :param cursor: положение курсора в момент нажатия
    :return: номер песни из списка
    """
    v = 0
    if tip % 2 == 0:
        lines(screen, krasny, False, [[EcrX - 6, 12], [EcrX - 3, 9], [EcrX - 3, 6], [EcrX - 9, 0], [EcrX - 9, 21]])
        polygon(screen, krasny,
                [[EcrX - 9, 21], [EcrX - 9, 18], [EcrX - 12, 15], [EcrX - 15, 15], [EcrX - 18, 18], [EcrX - 18, 21],
                 [EcrX - 15, 24], [EcrX - 12, 24]])
        return 0
    if tip % 2 == 1:
        polygon(screen, [255, 210, 95], [[EcrX - 200, 0], [EcrX, 0], [EcrX, 250], [EcrX - 200, 250]])
        line(screen, krasny, [EcrX - 20, 0], [EcrX, 20])
        line(screen, krasny, [EcrX, 0], [EcrX - 20, 20])
        screen.blit(f1.render('русская народная', 1, (0, 0, 0)), (EcrX - 200, 0))
        screen.blit(f1.render('пеленнорские поля', 1, (0, 0, 0)), (EcrX - 200, 25))
        screen.blit(f1.render('гачимучи', 1, (0, 0, 0)), (EcrX - 200, 50))
        screen.blit(f1.render('Where is my mind', 1, (0, 0, 0)), (EcrX - 200, 75))
        screen.blit(f1.render('Titanic', 1, (0, 0, 0)), (EcrX - 200, 100))
        screen.blit(f1.render('strength of a thousand men', 1, (0, 0, 0)), (EcrX - 200, 125))
        screen.blit(f1.render('Shingeki no koyjin', 1, (0, 0, 0)), (EcrX - 200, 150))
        screen.blit(f1.render('Witcher 3', 1, (0, 0, 0)), (EcrX - 200, 175))
        screen.blit(f1.render('Far Cry 3', 1, (0, 0, 0)), (EcrX - 200, 200))
        screen.blit(f1.render('TES V', 1, (0, 0, 0)), (EcrX - 200, 225))
        if cursor[1] < 25:
            v = 0
        if (cursor[1] > 25) and (cursor[1] < 50):
            v = 1
        if (cursor[1] > 50) and (cursor[1] < 75):
            v = 2
        if (cursor[1] > 75) and (cursor[1] < 100):
            v = 3
        if (cursor[1] > 100) and (cursor[1] < 125):
            v = 4
        if (cursor[1] > 125) and (cursor[1] < 150):
            v = 5
        return v


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


def morojenoe(x=60, y=250, r=10, fi=7):
    """
    рисует мороженное
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


def sharik(x=390, y=210, r=100, fi=-13):
    """
    рисует шарик
    :param x: координата х точки, за которую держат нитку
    :param y: координата у точки, за которую держат нитку
    :param r: коэффициент размера, численно равен длине нитки
    :param fi: угол наклона всей этой штуки
    :return:
    """
    line(screen, (128, 128, 128), (x, y), (int(round(x - r * np.sin(fi))), int(round(y - r * np.cos(fi)))), 2)
    polygon(screen, krasny,
            [[x - r * np.sin(fi), y - r * np.cos(fi)],
             [x - r * np.sin(fi) - 0.4 * r * np.sin(fi) - 0.2 * r * np.cos(fi),
              y - r * np.cos(fi) - 0.4 * r * np.cos(fi) + 0.2 * r * np.sin(fi)],
             [x - r * np.sin(fi) - 0.4 * r * np.sin(fi) + 0.2 * r * np.cos(fi),
              y - r * np.cos(fi) - 0.4 * r * np.cos(fi) - 0.2 * r * np.sin(fi)]])
    circle(screen, krasny,
           [int(round(x - r * np.sin(fi) - 0.425 * r * np.sin(fi) - 0.1 * r * np.cos(fi))),
            int(round(y - r * np.cos(fi) - 0.425 * r * np.cos(fi) + 0.1 * r * np.sin(fi)))], r // 10)
    circle(screen, krasny,
           [int(round(x - r * np.sin(fi) - 0.425 * r * np.sin(fi) + 0.1 * r * np.cos(fi))),
            int(round(y - r * np.cos(fi) - 0.425 * r * np.cos(fi) - 0.1 * r * np.sin(fi)))], r // 10)


def fon(sootnosheniye=0.4, tip=0):
    """рисует вон в зависимости от переданного типа
    :param tip: задает вид фона
    :param sootnosheniye: высота земли к высоте неба
    :return:
    """
    if tip == 0:
        rect(screen, siniy, (0, EcrY * (1 - sootnosheniye), EcrX, EcrY * sootnosheniye))
        rect(screen, zeleny, (0, 0, EcrX, EcrY * (1 - sootnosheniye)))
    if tip == 1:
        rect(screen, siniy, (0, EcrY * (1 - sootnosheniye), EcrX, EcrY * sootnosheniye))
        rect(screen, zeleny, (0, 0, EcrX, EcrY * (1 - sootnosheniye)))
    if tip == 2:
        rect(screen, siniy, (0, EcrY * (1 - sootnosheniye), EcrX, EcrY * sootnosheniye))
        rect(screen, zeleny, (0, 0, EcrX, EcrY * (1 - sootnosheniye)))
    if tip == 3:
        rect(screen, siniy, (0, EcrY * (1 - sootnosheniye), EcrX, EcrY * sootnosheniye))
        rect(screen, zeleny, (0, 0, EcrX, EcrY * (1 - sootnosheniye)))
    if tip == 4:
        rect(screen, siniy, (0, EcrY * (1 - sootnosheniye), EcrX, EcrY * sootnosheniye))
        rect(screen, zeleny, (0, 0, EcrX, EcrY * (1 - sootnosheniye)))
    if tip == 5:
        rect(screen, siniy, (0, EcrY * (1 - sootnosheniye), EcrX, EcrY * sootnosheniye))
        rect(screen, zeleny, (0, 0, EcrX, EcrY * (1 - sootnosheniye)))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

muzica(muzlo)

while not finished:
    clock.tick(FPS)
    time = time + 1
    fon(0.4, vybor)  # фон меняется в зависимости от песни
    sun(30, 30, 30, 2)
    morojenoe(70, 250, 10, 7)
    pocan(140, 130, 100)
    pocanessa(300, 130, 100)
    sharik(390, 210, 100, -13)
    music_box(zakryto)
    if not (vybor == muzlo):  # если номер выбранной песни не совпадает с текущим, поменять
        muzlo = vybor
        muzica(muzlo)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                cursor_pos = event.pos  # считывает позицию курсора, если нажать пкм
                if (cursor_pos[0] > EcrX - 20) and (cursor_pos[1] < 20):
                    zakryto = zakryto + 1  # открывает/закрывает список песен
                if (zakryto % 2 == 1) and (cursor_pos[0] < EcrX - 20) and (cursor_pos[0] > EcrX - 200):
                    vybor = music_box(zakryto, cursor_pos)  # в переменную записывает песню, на которую кликнули
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
