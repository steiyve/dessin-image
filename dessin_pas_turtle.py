#creer par nicolas
#creer le 2023-04-18
#dessine une foret

import turtle as t
import random as r


t.screensize(300,300)

def sapin():
    t.colormode(255)
    couleur = "brown"
    t.color(couleur)
    t.begin_fill()
    for i in range(3):
        t.fd(10)
        t.left(90)
        t.fd(30)
        t.left(90)
    t.end_fill()

    t.up()
    t.fd(20)
    t.down()
    t.left(-120)
    for j in range(3):
        t.color(120, 194, 64)
        t.begin_fill()
        for x in range(3):
            t.fd(30)
            t.right(120)
        t.end_fill()

        t.fd(30)
        t.up()
        t.left(120)
        t.fd(15)
        t.down()
        t.right(120)
    
    t.right(60)

while True:
    try:
        nb_sapin = int(input("combien de sapin voulez vous:"))
        break
    except:
        print("entrer un chiffre")



def bg():
    t.speed(0)
    t.bgcolor("blue")
    t.pencolor("green")
    t.color("green")
    t.begin_fill()
    t.goto(-1000, 0)
    t.goto(-1000,-1000)
    t.goto(1000, -1000)
    t.goto(1000, 0)
    t.goto(0,0)
    t.end_fill()


def nuage():
    t.penup()
    t.goto(0, 350)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(35)
    t.end_fill()
    t.penup()
    t.goto(0, 350)
    t.goto(25,350)
    t.pendown()
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.penup()
    t.goto(0, 350)
    t.goto(-25, 350)
    t.pendown()
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    

def lac():
    t.penup()
    t.goto(-0,-500)
    t.color("blue")
    t.begin_fill()
    t.circle(100)
    t.end_fill()


bg()
nuage()
lac()
AllX=[]
AllY=[]
for i in range(nb_sapin):
    t.up()
    x=r.randint(-500,500)
    y=r.randint(-300,0)
    AllX.append(x)
    AllY.append(y)
    t.goto(x,y)
    t.down()
    sapin()



