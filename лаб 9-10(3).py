from turtle import *
import random

colors = ["yellow", "red", "green", "blue"]

shape("turtle")
def shest(side): 
    down()
    for i in range(6):
        color(random.choise(colors))
        forward(side)
        left(60)
    up()
up()
shest(20)
up()
goto(20,30)
shest(40)
done()
