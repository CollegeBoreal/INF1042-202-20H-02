# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:21:40 2020

Conception d'un jeu dela tortue avec Python Turtle Graphics

@author: zacks
"""

import turtle
import random

zack = turtle.Turtle()
# Utilisation des variables

zack = turtle.Turtle()
zack.color("red")  
zack.pensize(5)
zack.shape("turtle")


zack.forward(100)
zack.left(90)
zack.forward(100)
zack.left(90)
zack.forward(100)
zack.left(90)
zack.forward(100)


zack = turtle.Turtle()
zack.speed(5) 

zack = turtle.Turtle()
zack.color("red", "blue")  # le bleu est la couleur de remplissage

zack.width(5)

colors = ["red", "blue","green", "purple", "yellow", "orange", "black"]

for x in range(5):
    randColor = random.randrange(0, len(colors))
    rand1 = random.randrange(-300,300)
    rand2 = random.randrange(-300,300)
   
    zack.color(colors[randColor], colors[random.randrange(0, len(colors))])

    zack.penup()
    zack.setpos((rand1, rand2))
    zack.pendown()

zack.begin_fill()
zack.circle(50)
zack.end_fill()

from turtle import Turtle
from turtle import Screen

screen = Screen()
t = Turtle("turtle")

def dragging(x, y):  
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)

def clickRight():
    t.clear()

def main():  # fonction pour faire marcher le programme
    turtle.listen()
    
    t.ondrag(dragging)  # permet de faire bouger la tortue
    turtle.onscreenclick(clickRight, 3)

    screen.mainloop()  

main()





