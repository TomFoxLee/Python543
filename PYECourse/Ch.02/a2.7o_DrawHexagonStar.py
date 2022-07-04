# Ch.02 Exercise 2.7 Official Answer
# Draw Hexagon Star

import turtle

turtle.penup()
turtle.setpos(-150, 20)
turtle.pendown()
turtle.left(30)
turtle.fd(100)
turtle.left(60)

for i in range(5):
    turtle.fd(100)
    turtle.right(120)
    turtle.fd(100)
    turtle.left(60)

turtle.fd(100)
turtle.right(120)
turtle.fd(100)

for i in range(6):
    turtle.fd(100)
    turtle.right(60)

turtle.done()
