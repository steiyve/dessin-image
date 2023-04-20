#creer par nicolas
#creer le 2023-04-18
#dessine une foret

import turtle as t
import random as r


def sapin():
    for i in range(3):
        t.fd(10)
        t.left(90)
        t.fd(30)
        t.left(90)
    
    t.up()
    t.fd(20)
    t.down()
    t.left(-120)
    for j in range(3):
        for x in range(3):
            t.fd(30)
            t.right(120)
        
        t.fd(30)
        t.up()
        t.left(120)
        t.fd(15)
        t.down()
        t.right(120)
    
    t.right(60)

nb_sapin = 4
for i in range(nb_sapin):
    t.up()
    t.goto(r.randint(-300,300), r.randint(-300,300))
    t.down()
    sapin()


while True:
    pass
        