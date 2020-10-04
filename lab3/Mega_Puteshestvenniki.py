import pygame
from pygame.draw import *
import numpy as np

pygame.init()

# размеры экрана, через них всё задаётся
EcrX = 900
EcrY = 700

# KTO? (WHO?) – Цвета (Colors)
zhelty = (255, 255, 0)
futbolka = (128, 128, 128)
cherny = (0, 0, 0)
koja = (255, 165, 0)
platye = (128, 0, 0)
krasny = (255, 0, 0)
beliy = (255, 255, 255)

# названия файлов импортированных песен и изображений
if 0 == 0:  # просто чтобы свернуть можно было
    file0 = 'Russkaya_narodnaya.mp3'
    file1 = 'Pelennor_Fields.mp3'
    file2 = 'Gachi.mp3'
    file3 = 'Where_Is_My_Mind.mp3'
    file4 = 'My_Heart_Will_Go_On.mp3'
    file5 = 'Strength_of_a_Thousand_Men.mp3'
    file6 = 'Doukei_to_Shikabane_no_Michi.mp3'
    file7 = 'Hunt or Be Hunted.mp3'
    file8 = 'Make_It_Bun_Dem.mp3'
    file9 = 'Skyrim_OST.mp3'
    file10 = 'The_Godfather_Theme.mp3'
    file11 = 'JoJo.mp3'
    file12 = 'Юность в сапогах.mp3'
    file13 = 'Battle_Without_Honor.mp3'
    file14 = 'Ievan_Polkka.mp3'
    file15 = 'Privet_Morrikone.mp3'
    file16 = 'He_is_a_pirate.mp3'
    file17 = 'All_Star.mp3'
    file18 = 'Terminator.mp3'
    file19 = 'Imperial_March.mp3'
    file20 = 'Let_It_Go.mp3'
    file21 = 'Back_to_the_Future.mp3'
    file22 = 'Mission_Impossible.mp3'
    file23 = 'See_You_Again.mp3'
    file24 = 'Circle_Of_Life.mp3'
    file25 = 'Interstellar.mp3'
    file26 = 'Vremya_vpered.mp3'
    file27 = 'We_Will_Rock_You.mp3'
    file28 = 'Serbia_strong.mp3'
    file29 = 'YA_kalendar.mp3'
    file30 = 'Mortal_Combat.mp3'
    file31 = 'deja-vu.mp3'
    file32 = 'For_the_Damaged_Coda.mp3'
    file33 = 'CHjornyjj_Bumer.mp3'
    file34 = 'mine diamonds.mp3'
    file35 = 'HardbASS.mp3'
    file36 = 'прыжок со школы.mp3'
    file37 = 'Big Enough.mp3'
    file38 = 'OT_VINTA.mp3'
    file39 = 'Crab_Rave.mp3'
    file40 = 'Sanya_ty_v_poryadke.mp3'
    file41 = 'TRAKTOR.mp3'
    file42 = 'Giorno Giovanna.mp3'
    file43 = 'Gorod_Omsk.mp3'
    surf0 = pygame.image.load('Berezki.jpg')
    surf1 = pygame.image.load('Пеленнорские поля.jpg')
    surf2 = pygame.image.load('Гачи.jpg')
    surf3 = pygame.image.load('Бойцовский клуб.jpeg')
    surf4 = pygame.image.load('Титаник.jpg')
    surf5 = pygame.image.load('Сила.jpg')
    surf6 = pygame.image.load('Атака титанов.jpg')
    surf7 = pygame.image.load('Дикая охота.jpg')
    surf8 = pygame.image.load('Огнемет.jpg')
    surf9 = pygame.image.load('Скайрим.jpg')
    surf10 = pygame.image.load('Крестный.jpg')
    surf11 = pygame.image.load('джоджо.jpg')
    surf12 = pygame.image.load('Солдаты.jpg')
    surf13 = pygame.image.load('Убить билла.jpg')
    surf14 = pygame.image.load('полька.jpg')
    surf15 = pygame.image.load('Бумер.jpg')
    surf16 = pygame.image.load('pirates-of-caribbean.jpg')
    surf17 = pygame.image.load('Шрек.png')
    surf18 = pygame.image.load('Terminator_2.jpg')
    surf19 = pygame.image.load('Star_Wars.jpg')
    surf20 = pygame.image.load('Холодное сердце.jpg')
    surf21 = pygame.image.load('Назад в будущее.jpg')
    surf22 = pygame.image.load('mission-impossible.jpg')
    surf23 = pygame.image.load('Форсаж.jpg')
    surf24 = pygame.image.load('Король лев.jpg')
    surf25 = pygame.image.load('matthew-mcconaughey.jpg')
    surf26 = pygame.image.load('Индустриализация.jpg')
    surf27 = pygame.image.load('Queen.jpg')
    surf28 = pygame.image.load('Сербия.jpg')
    surf29 = pygame.image.load('Я календарь.jpg')
    surf30 = pygame.image.load('мортал комбат.jpg')
    surf31 = pygame.image.load('Дежа ву.jpg')
    surf32 = pygame.image.load('Морти.jpg')
    surf33 = pygame.image.load('Черный бумер.jpg')
    surf34 = pygame.image.load('мои алмазы.jpg')
    surf35 = pygame.image.load('Хардбасс.jpg')
    surf36 = pygame.image.load('Прыжок.jpg')
    surf37 = pygame.image.load('Большой достаточно.jpg')
    surf38 = pygame.image.load('Ат винта.jpg')
    surf39 = pygame.image.load('Краб.jpg')
    surf40 = pygame.image.load('Саня.jpg')
    surf41 = pygame.image.load('Трактор.jpg')
    surf42 = pygame.image.load('Джорно.jpg')
    surf43 = pygame.image.load('Омск.jpg')

# рабочие переменные, лучше не трогать
time = 0
zakryto = 0
muzlo = 0
vybor = 0
scroll = 0

FPS = 30
screen = pygame.display.set_mode((EcrX, EcrY))

pygame.font.SysFont('arial', 36)
f1 = pygame.font.Font(None, 20)


def muzica(n):
    """
    включает выбранную музыку

    :param n: задаёт конкретный файл песни
    :return: none
    """
    pygame.init()
    pygame.mixer.init()
    eval('pygame.mixer.music.load(file' + str(n) + ')')
    pygame.mixer.music.play(-1)


def music_box(tip, h=0, cursor=(0, 0)):
    """
    если тип = 1, показывает кликабельную ноту в углу экрана, иначе показывает кликабельный список песен

    :param tip: выбирает, что показывать – ноту или список
    :param h: дополнительная (может и отрицательная) высота, чтобы можно было скроллить список
    :param cursor: положение курсора в момент нажатия
    :return: номер песни из списка
    """
    if tip % 2 == 0:
        lines(screen, krasny, False, [[EcrX - 6, 12], [EcrX - 3, 9], [EcrX - 3, 6], [EcrX - 9, 0], [EcrX - 9, 21]])
        polygon(screen, krasny,
                [[EcrX - 9, 21], [EcrX - 9, 18], [EcrX - 12, 15], [EcrX - 15, 15], [EcrX - 18, 18], [EcrX - 18, 21],
                 [EcrX - 15, 24], [EcrX - 12, 24]])
    if tip % 2 == 1:
        polygon(screen, [255, 210, 95],
                [[EcrX - 200, h], [EcrX, h], [EcrX, h + 1100], [EcrX - 200, h + 1100]])
        polygon(screen, [2, 0, 0],
                [[EcrX - 200, h], [EcrX, h], [EcrX, h + 1100], [EcrX - 200, h + 1100]], 3)
        line(screen, krasny, [EcrX - 20, 0], [EcrX, 20])
        line(screen, krasny, [EcrX, 0], [EcrX - 20, 20])
        screen.blit(f1.render('русская народная', 1, (0, 0, 0)), (EcrX - 180, h + 0))
        screen.blit(f1.render('пеленнорские поля', 1, (0, 0, 0)), (EcrX - 180, h + 25))
        screen.blit(f1.render('гачимучи', 1, (0, 0, 0)), (EcrX - 180, h + 50))
        screen.blit(f1.render('Where is my mind', 1, (0, 0, 0)), (EcrX - 180, h + 75))
        screen.blit(f1.render('Titanic', 1, (0, 0, 0)), (EcrX - 180, h + 100))
        screen.blit(f1.render('strength of a thousand men', 1, (0, 0, 0)), (EcrX - 180, h + 125))
        screen.blit(f1.render('Shingeki no koyjin', 1, (0, 0, 0)), (EcrX - 180, h + 150))
        screen.blit(f1.render('Witcher 3', 1, (0, 0, 0)), (EcrX - 180, h + 175))
        screen.blit(f1.render('Far Cry 3', 1, (0, 0, 0)), (EcrX - 180, h + 200))
        screen.blit(f1.render('TES V', 1, (0, 0, 0)), (EcrX - 180, h + 225))
        screen.blit(f1.render('Godfather', 1, (0, 0, 0)), (EcrX - 180, h + 250))
        screen.blit(f1.render('JoJo', 1, (0, 0, 0)), (EcrX - 180, h + 275))
        screen.blit(f1.render('Юность в сапогах', 1, (0, 0, 0)), (EcrX - 180, h + 300))
        screen.blit(f1.render('Убить (де)Билла', 1, (0, 0, 0)), (EcrX - 180, h + 325))
        screen.blit(f1.render('Полька', 1, (0, 0, 0)), (EcrX - 180, h + 350))
        screen.blit(f1.render('Бумер', 1, (0, 0, 0)), (EcrX - 180, h + 375))
        screen.blit(f1.render('Пираты Карибского моря', 1, (0, 0, 0)), (EcrX - 180, h + 400))
        screen.blit(f1.render('Шрек', 1, (0, 0, 0)), (EcrX - 180, h + 425))
        screen.blit(f1.render('Терминатор', 1, (0, 0, 0)), (EcrX - 180, h + 450))
        screen.blit(f1.render('Звездные войны', 1, (0, 0, 0)), (EcrX - 180, h + 475))
        screen.blit(f1.render('Холодное сердце', 1, (0, 0, 0)), (EcrX - 180, h + 500))
        screen.blit(f1.render('Назад в будущее', 1, (0, 0, 0)), (EcrX - 180, h + 525))
        screen.blit(f1.render('Миссия невыполнима', 1, (0, 0, 0)), (EcrX - 180, h + 550))
        screen.blit(f1.render('See you again', 1, (0, 0, 0)), (EcrX - 180, h + 575))
        screen.blit(f1.render('Король лев', 1, (0, 0, 0)), (EcrX - 180, h + 600))
        screen.blit(f1.render('Interstellar', 1, (0, 0, 0)), (EcrX - 180, h + 625))
        screen.blit(f1.render('Время вперёд', 1, (0, 0, 0)), (EcrX - 180, h + 650))
        screen.blit(f1.render('We will rock you', 1, (0, 0, 0)), (EcrX - 180, h + 675))
        screen.blit(f1.render('Serbia strong', 1, (0, 0, 0)), (EcrX - 180, h + 700))
        screen.blit(f1.render('Шуфутинский', 1, (0, 0, 0)), (EcrX - 180, h + 725))
        screen.blit(f1.render('Mortal combat', 1, (0, 0, 0)), (EcrX - 180, h + 750))
        screen.blit(f1.render('Deja vu', 1, (0, 0, 0)), (EcrX - 180, h + 775))
        screen.blit(f1.render('Rick and Morty', 1, (0, 0, 0)), (EcrX - 180, h + 800))
        screen.blit(f1.render('Чёрный бумер', 1, (0, 0, 0)), (EcrX - 180, h + 825))
        screen.blit(f1.render('My diamonds', 1, (0, 0, 0)), (EcrX - 180, h + 850))
        screen.blit(f1.render('Хардбасс', 1, (0, 0, 0)), (EcrX - 180, h + 875))
        screen.blit(f1.render('Прыжок со школы', 1, (0, 0, 0)), (EcrX - 180, h + 900))
        screen.blit(f1.render('Bolshoy dostatochno', 1, (0, 0, 0)), (EcrX - 180, h + 925))
        screen.blit(f1.render('AT VINTA', 1, (0, 0, 0)), (EcrX - 180, h + 950))
        screen.blit(f1.render('Crab rave', 1, (0, 0, 0)), (EcrX - 180, h + 975))
        screen.blit(f1.render('Sanya are you okey', 1, (0, 0, 0)), (EcrX - 180, h + 1000))
        screen.blit(f1.render('Синий трактор', 1, (0, 0, 0)), (EcrX - 180, h + 1025))
        screen.blit(f1.render('Тема джорно', 1, (0, 0, 0)), (EcrX - 180, h + 1050))
        screen.blit(f1.render('Город Омск', 1, (0, 0, 0)), (EcrX - 180, h + 1075))
    v = (-h + cursor[1]) // 25
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
    :param r: размер - радиуc рожи
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


def fon(tip=0):
    """рисует (импортирует) фон в зависимости от переданного типа

    :param tip: задает вид фона
    :return:
    """
    eval('screen.blit(surf' + str(tip) + ', [0, 0])')


pygame.display.update()
clock = pygame.time.Clock()
finished = False

muzica(muzlo)

while not finished:
    clock.tick(FPS)
    time = time + 1
    fon(vybor)  # фон меняется в зависимости от песни
    sun(EcrX // 20, EcrY // 20, (EcrX + EcrY) // 50, 2)
    morojenoe(7 * EcrX // 90, 57 * EcrY // 70, (EcrX + EcrY) // 160, 7)
    pocan(14 * EcrX // 90, 45 * EcrY // 70, (EcrX + EcrY) // 16)
    pocanessa(30 * EcrX // 90, 45 * EcrY // 70, (EcrX + EcrY) // 16)
    sharik(39 * EcrX // 90, 53 * EcrY // 70, (EcrX + EcrY) // 16, -13)
    music_box(zakryto, scroll)
    if not (vybor == muzlo):  # если номер выбранной песни не совпадает с текущим, поменять
        muzlo = vybor
        muzica(muzlo)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                scroll = scroll + 25
            if event.button == 5:
                scroll = scroll - 25
            if event.button == 1:
                cursor_pos = event.pos  # считывает позицию курсора, если нажать пкм
                if (cursor_pos[0] > EcrX - 25) and (cursor_pos[1] < 25):
                    zakryto = zakryto + 1  # открывает/закрывает список песен
                if (zakryto % 2 == 1) and (cursor_pos[0] < EcrX - 25) and (cursor_pos[0] > EcrX - 200) and (
                        -scroll + cursor_pos[1] < 1100):
                    vybor = music_box(zakryto, scroll, cursor_pos)  # в переменную записывает песню, на которую кликнули
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
