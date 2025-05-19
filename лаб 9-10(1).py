import turtle
import random

colors = ["yellow", "red", "green", "blue"]

def circleMy(r, x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(random.choice(colors))  
    turtle.circle(r)
    turtle.up()
    
circleMy(30, 0, 0)
circleMy(60, 70, 60)
circleMy(100, 200, 100)
turtle.done()