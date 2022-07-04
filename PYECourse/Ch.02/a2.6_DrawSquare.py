# Ch.02 Exercise 2.6
# Draw Square without corner

import turtle

turtle.setup(500, 500, 200, 200)
turtle.pensize(5)
turtle.pencolor("violet")

turtle.penup()
turtle.fd(-50)
turtle.seth(-270)
turtle.fd(-50)
turtle.seth(0)

for i in range(4):
    turtle.fd(25)
    turtle.pendown()
    turtle.fd(50)
    turtle.penup()
    turtle.fd(25)
    turtle.left(90)

turtle.left(90)
turtle.fd(25)
turtle.left(180)

""" turtle.seth(0)
turtle.fd(25)
turtle.pendown()
turtle.fd(50)
turtle.penup()
turtle.fd(25)

turtle.seth(90)
turtle.fd(25)
turtle.pendown()
turtle.fd(50)
turtle.penup()
turtle.fd(25)

turtle.seth(180)
turtle.fd(25)
turtle.pendown()
turtle.fd(50)
turtle.penup()
turtle.fd(25)

turtle.seth(270)
turtle.fd(25)
turtle.pendown()
turtle.fd(50)
# turtle.penup()
# turtle.fd(25)
 """
turtle.done()
