import turtle as t
import numpy as np
from random import randint as ran


number_of_turtles = 34
steps_of_time_number = 500
r = 300

j = 0
cor = np.zeros((number_of_turtles - 4) * 2).reshape(number_of_turtles - 4, 2)
ang = []
t.screensize(1000, 1000)
pool = [t.Turtle(shape='turtle') for i in range(number_of_turtles)]
i = 0
for unit in pool:
    if i < 4:
        if i == 0:
            unit.penup()
            unit.goto(-r, -r)
            unit.pendown()
            unit.forward(2 * r)
        if i == 1:
            unit.penup()
            unit.goto(-r, r)
            unit.pendown()
            unit.forward(2 * r)
        if i == 2:
            unit.penup()
            unit.goto(r, -r)
            unit.pendown()
            unit.left(90)
            unit.forward(2 * r)
        if i == 3:
            unit.penup()
            unit.goto(-r, -r)
            unit.pendown()
            unit.left(90)
            unit.forward(2 * r)
        unit.penup()
        unit.hideturtle()
        i += 1
    else:
        unit.penup()
        unit.shape('circle')
        unit.speed(0)
        unit.goto(ran(-r, r), ran(-r, r))
        ang.append(ran(0, 360))
        unit.left(ang[j])
        cor[j] = unit.pos()
        j += 1

for i in range(steps_of_time_number):
    j = 0
    co = 0
    for unit in pool:
        if co > 3:
            unit.forward(number_of_turtles // 10)
            cor[j] = unit.pos()
            if cor[j][0] > r:
                direction = ang[j]
                wallInclination = 90
                wallAngle = 90 + wallInclination
                ballAngle = 180 + direction
                diff = wallAngle - ballAngle
                angle = ballAngle + 2 * diff + 360 * 5
                angle %= 360
                unit.left(angle - ang[j])
                ang[j] = angle
            if cor[j][0] < -r:
                direction = ang[j]
                wallInclination = 90
                wallAngle = 90 + wallInclination
                ballAngle = 180 + direction
                diff = wallAngle - ballAngle
                angle = ballAngle + 2 * diff + 360 * 5
                angle %= 360
                unit.left(angle - ang[j])
                ang[j] = angle
            if cor[j][1] < -r:
                direction = ang[j]
                wallInclination = 0
                wallAngle = 90 + wallInclination
                ballAngle = 180 + direction
                diff = wallAngle - ballAngle
                angle = ballAngle + 2 * diff + 360 * 5
                angle %= 360
                unit.left(angle - ang[j])
                ang[j] = angle
            if cor[j][1] > r:
                direction = ang[j]
                wallInclination = 0
                wallAngle = 90 + wallInclination
                ballAngle = 180 + direction
                diff = wallAngle - ballAngle
                angle = ballAngle + 2 * diff + 360 * 5
                angle %= 360
                unit.left(angle - ang[j])
                ang[j] = angle

            j += 1
        else:
            co += 1
