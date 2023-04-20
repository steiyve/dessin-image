#creer par nicolas
#creer le 2023-04-18
#dessine une foret

import turtle as t
import random as r

nb_sapin = 1

def sapin(nbSapin):
    for i in range(nbSapin):
        t.penup()
        x=r.randint(-200, 200)
        y=r.randint(-200, 200)
        t.goto(x,y)
        t.pendown()
        t.fd(40)
        t.left(90)
        posXY = t.pos()
        print(posXY)
        t.fd(100)
        t.left(90)
        t.fd(40)
        t.left(90)
        t.fd(100)
        t.left(90)
        t.penup()
        x-=40
        y+=100
        t.goto(x,y)
        t.pendown()
        for x in range(3):
            t.fd(120)
            t.left(120)
        t.penup()
        t.goto(x,y)
        y+=93.23
        t.goto(x,y)
        t.pendown()
        for x in range(3):
            t.fd(120)
            
            t.left(120)
        t.penup()
        y+=100
        t.goto(x,y)
        t.pendown()
        for x in range(3):
            t.fd(120)
            
            t.left(120)
        t.penup()
        y+=100
        t.goto(x, y)
        t.pendown()



sapin(nb_sapin)

while True:
    pass
        