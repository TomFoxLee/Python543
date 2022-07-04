# Ch.02 Exercise 2.8
# Draw Square Spiral

import turtle

turtle.setup(600, 600, 200, 200)
turtle.pencolor("violet")
turtle.pendown()

for i in range(40):
    turtle.fd(i * 5)
    turtle.left(90)

turtle.done()
