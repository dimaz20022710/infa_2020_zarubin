import turtle as t


def f(n, s):
    if n == 0:
        f0(s)
    if n == 1:
        f1(s)
    if n == 2:
        f2(s)
    if n == 3:
        f3(s)
    if n == 4:
        f4(s)
    if n == 5:
        f5(s)
    if n == 6:
        f6(s)
    if n == 7:
        f7(s)
    if n == 8:
        f8(s)
    if n == 9:
        f9(s)


def gor(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x + 100, y)


def ver(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y - 100)


def f0(n):
    gor(n * 150, 0)
    gor(n * 150, -200)
    ver(n * 150 + 100, 0)
    ver(n * 150 + 100, -100)
    ver(n * 150, 0)
    ver(n * 150, -100)


def f1(n):
    ver(n * 150 + 100, 0)
    ver(n * 150 + 100, -100)


def f2(n):
    gor(n * 150, 0)
    gor(n * 150, -100)
    gor(n * 150, -200)
    ver(n * 150 + 100, 0)
    ver(n * 150, -100)


def f3(n):
    gor(n * 150, 0)
    gor(n * 150, -100)
    gor(n * 150, -200)
    ver(n * 150 + 100, 0)
    ver(n * 150 + 100, -100)


def f4(n):
    gor(n * 150, -100)
    ver(n * 150, 0)
    ver(n * 150 + 100, 0)
    ver(n * 150 + 100, -100)


def f5(n):
    gor(n * 150, 0)
    gor(n * 150, -100)
    gor(n * 150, -200)
    ver(n * 150, 0)
    ver(n * 150 + 100, -100)


def f6(n):
    gor(n * 150, 0)
    gor(n * 150, -100)
    gor(n * 150, -200)
    ver(n * 150 + 100, -100)
    ver(n * 150, 0)
    ver(n * 150, -100)


def f7(n):
    gor(n * 150, 0)
    ver(n * 150 + 100, 0)
    ver(n * 150 + 100, -100)


def f8(n):
    gor(n * 150, 0)
    gor(n * 150, -100)
    gor(n * 150, -200)
    ver(n * 150 + 100, 0)
    ver(n * 150 + 100, -100)
    ver(n * 150, 0)
    ver(n * 150, -100)


def f9(n):
    gor(n * 150, 0)
    gor(n * 150, -100)
    gor(n * 150, -200)
    ver(n * 150 + 100, 0)
    ver(n * 150 + 100, -100)
    ver(n * 150, 0)


t.shape('circle')
t.screensize(3000, 2000)
inp = open('C:/Users/dimaz/Documents/Phystech python/test.txt', 'r')
num = list(inp.read().split())
for i in range(len(num)):
    num[i] = int(num[i])
for i in range(len(num)):
    f(num[i], i)
t.hideturtle()
t.done()
