# Ch.02 Exercise 2.6 Official Answer
# Draw Square without corner

import turtle

turtle.setup(500, 500)

for i in range(4):
    turtle.penup()
    turtle.fd(20)
    turtle.pendown()
    turtle.fd(160)
    turtle.penup()
    turtle.fd(20)
    turtle.right(90)

turtle.done()
