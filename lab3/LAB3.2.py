import random as rnd
import numpy as np
import pygame
import pygame.draw as d
from PIL import Image

pygame.init()

FPS = 15
screen_width = 500
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

# color definition
brown = (75, 45, 0)
pale_transparent = (215, 215, 255, 210)
black = (0, 0, 0)
white = (255, 255, 255)
window_color = (40, 70, 50)
dark_gray = (20, 22, 20)
yellow = (255, 255, 0)

# ground & sky
d.rect(screen, (100, 100, 100), (0, 0, screen_width, 3 * screen_height // 7))
d.rect(screen, black, (0, 300, screen_width, 4 * screen_height // 7))


# returns a series of ones & zeros with equal probability with custom length
def coinflip(length):
    A = []
    for i in range(length):
        if (rnd.random() - 0.5) > 0:
            A.append(1)
        else:
            A.append(0)
    return A


# function takes only the shape of the ghost from image, else is done via pygame tools
def ghost(x, y, scale=1.0, orientation=True):
    if scale > 1:
        print('error: scale <= 1')
    else:
        s = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        pixAr = pygame.PixelArray(s)
        A = []
        B = []
        im = Image.open("ghostimage.png")
        width, height = im.size
        for x_pix in range(width):
            for y_pix in range(height):
                r, g, b, a = im.getpixel((x_pix, y_pix))
                if r >= 10 and g >= 10 and b >= 10:
                    A.append(x + int(x_pix * scale))
                    B.append(y + int(y_pix * scale))
        for i in range(len(A)):
            pixAr[A[i]][B[i]] = pale_transparent
        del pixAr
        d.circle(s, (130, 130, 255), (x + int(75 * scale), y + int(35 * scale)), int(8 * scale))
        d.circle(s, (130, 130, 255), (x + int(108 * scale), y + int(30 * scale)), int(8 * scale))
        d.circle(s, black, (x + int(73 * scale), y + int(35 * scale)), int(4 * scale))
        d.circle(s, black, (x + int(106 * scale), y + int(30 * scale)), int(4 * scale))
        p = pygame.Surface((10, 4), pygame.SRCALPHA)
        d.ellipse(p, white, (0, 0, 10 * scale, 4 * scale))
        p = pygame.transform.rotate(p, 30)
        s.blit(p, (x + int(73 * scale), y + int(28 * scale)))
        s.blit(p, (x + int(106 * scale), y + int(23 * scale)))
        if not orientation:
            s = pygame.transform.flip(s, True, False)
        pygame.transform.scale(s, (int(screen_width * scale), int(screen_height * scale)))
        screen.blit(s, (0, 0))


# function that draws a moon centred on (x, y)
def moon(x, y, R=75):
    d.circle(screen, (240, 240, 240), (x, y), R)
    for i in range(R // 3):
        randx = x + 1.2 * (rnd.random() - 0.5) * R
        randx = int(round(randx))
        randy = y + 1.2 * (rnd.random() - 0.5) * R
        randy = int(round(randy))
        d.circle(screen, (175, 175, 175), (randx, randy), 5 + int(round(5 * rnd.random())))


# function that draws spider webs on houses centred on (x, y)
def cobweb(x, y, scale=1.0):
    R = 50 * scale
    for i in range(8):
        ymod = round(y + (R * np.sin(i * np.pi / 4)))
        xmod = round(x + (R * np.cos(i * np.pi / 4)))
        ymod_next = round(y + (R * np.sin((i - 1) * np.pi / 4)))
        xmod_next = round(x + (R * np.cos((i - 1) * np.pi / 4)))
        d.line(screen, (200, 255, 200), (x, y), (xmod, ymod))
        d.line(screen, (200, 255, 200), (xmod_next, ymod_next), (xmod, ymod))
        d.line(screen, (200, 255, 200), ((xmod + x) // 2, (ymod + y) // 2),
               ((xmod_next + x) // 2, (ymod_next + y) // 2))


# function draws a house with (x, y) coordinates of top left corner
def house(x, y, scale=1.0):
    width = int(220 * scale)
    height = int(130 * scale)
    windows(x, y, width, height)
    top_windows(x, y, width, height)
    vertical_beams(x, y, width, height, scale)
    tubes(x, y, width, height)
    d.rect(screen, brown, (x, y, width, height))
    d.rect(screen, dark_gray, (x - int(20 * scale), y + 5, int(width + 40 * scale), height // 8))
    d.rect(screen, dark_gray, (x - int(20 * scale), y + 5 - height // 4, int(width + 40 * scale), height // 12))
    d.rect(screen, dark_gray, (x, y - height, width, height // 6))
    d.polygon(screen, dark_gray, ((x - int(30 * scale), y - height + height // 6),
                                  (x, y - height + height // 6), (x, y - height)))
    d.polygon(screen, dark_gray, ((x + width + int(30 * scale), y - height + height // 6),
                                  (x + width, y - height + height // 6), (x + width, y - height)))
    cords = [(x + int(22 * scale), y + int(35 * scale)), (x + int(195 * scale), y + int(105 * scale)),
             (x + int(40 * scale), y - int(90 * scale)), (x + int(180 * scale), y - int(50 * scale))]
    probs = coinflip(4)
    for i in range(len(cords)):
        if probs[i] == 1:
            a, b = cords[i]
            cobweb(a, b, 0.45 * scale)


# function that draws a cloud with left top corner (x, y) with color scaling by grayness parameter [0, 1]
def cloud(x, y, grayness=0.0, scale=1.0):
    s = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
    d.ellipse(s, (255 * grayness, 255 * grayness, 255 * grayness, 100),
              (x, y, 120 * scale, 25 * scale))
    d.circle(s, (255 * grayness, 255 * grayness, 255 * grayness, 100),
             (x + int(120 * 0.8 * scale) // 3, y + int(25 * scale) // 3), 40)
    d.circle(s, (255 * grayness, 255 * grayness, 255 * grayness, 100),
             (x + int(120 * 1.5 * scale) // 3, y + int(25 * 0.8 * scale) // 3), 40)
    d.circle(s, (255 * grayness, 255 * grayness, 255 * grayness, 100),
             (x + int(120 * 2.4 * scale) // 3, y + int(25 * 1.2 * scale) // 3), 40)
    d.circle(s, (255 * grayness, 255 * grayness, 255 * grayness, 100),
             (x + int(120 * 0.95 * scale) // 3, y + int(25 * 2 * scale) // 3), 40)
    d.circle(s, (255 * grayness, 255 * grayness, 255 * grayness, 100),
             (x + int(120 * 1.7 * scale) // 3, y + int(25 * 1.7 * scale) // 3), 40)
    d.circle(s, (255 * grayness, 255 * grayness, 255 * grayness, 100),
             (x + int(120 * 2.8 * scale) // 3, y + int(25 * 1.3 * scale) // 3), 40)
    d.circle(s, (255 * grayness, 255 * grayness, 255 * grayness, 100),
             (x + 25, y + int(12 * scale)), 45)
    screen.blit(s, (0, 0))


def windows(x, y, width, height):
    flp = coinflip(3)
    for i in range(3):
        if flp[i] == 1:
            clr = yellow
        else:
            clr = window_color
        d.rect(screen, clr, (x + width * (2 * i + 1) // 7, y + height // 3, width // 7, height // 3))


def top_windows(x, y, width, height):
    for i in range(11):
        if i % 2 == 0:
            clr = brown
        else:
            clr = window_color
        d.rect(screen, clr, (x + i * width // 11, y - height, width // 11, height))


def vertical_beams(x, y, width, height, scale):
    for i in range(7):
        d.rect(screen, dark_gray, (x - int(20 * scale) + int((width + 40 * scale) * (2 * i + 0.25) / 13),
                                   y + 5 - height // 4, width // 26, height // 4))


def tubes(x, y, width, height):
    for i in range(int(6 * rnd.random())):
        d.rect(screen, (40, 42, 40), (x + int(width * rnd.random()), y - height + int(0.12 * height * rnd.random()),
                                      int(width / 10 * rnd.random()) + 3, -int(height / 3 * rnd.random()) - 20))


moon(420, 100, R=60)
cloud(270, 200, grayness=0.65, scale=2.5)
house(330, 280, scale=0.7)
house(150, 370, scale=0.7)
house(30, 500, scale=0.7)
cloud(150, 280, grayness=0.85, scale=2.4)
cloud(40, 350, grayness=0.55, scale=2.1)
cloud(150, 80, grayness=0.2, scale=2.8)
cloud(160, 430, grayness=0.7, scale=2.6)
cloud(90, 120, grayness=0.45, scale=2.2)
cloud(50, 190, grayness=0.75, scale=2.7)
ghost(305, 545, 0.35)
ghost(330, 550, 0.65)
ghost(370, 400, 0.45)
ghost(375, 430, 0.45)
ghost(340, 520, 0.45, False)
ghost(370, 560, 0.45, False)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
