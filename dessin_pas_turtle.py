#creer par nicolas
#creer le 2023-04-18
#dessine une foret

import turtle as t
import random as r


def sapin():
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
        couleur = "green"
        t.color(couleur)
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


AllX=[]
AllY=[]
for i in range(nb_sapin):
    t.up()
    x=r.randint(-300,300)
    y=r.randint(-300,300)
    AllX.append(x)
    AllY.append(y)
    t.goto(x,y)
    t.down()
    sapin()



