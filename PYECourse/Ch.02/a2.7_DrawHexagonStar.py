# Ch.02 Exercise 2.7
# Draw Hexagon Star

import turtle


def drawTriangle():
    for i in range(3):
        turtle.fd(240)
        turtle.right(120)


turtle.setup(600, 600, 200, 200)
turtle.pensize(5)
turtle.pencolor("violet")

turtle.penup()
turtle.fd(-150)
turtle.seth(30)
turtle.pendown()

drawTriangle()

turtle.penup()
turtle.seth(0)
turtle.fd(280)
turtle.seth(-150)
turtle.pendown()

drawTriangle()

turtle.penup()
turtle.seth(0)
turtle.fd(-280)
turtle.seth(30)
turtle.fd(80)

turtle.done()
