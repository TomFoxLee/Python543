# Ch.02 Exercise 2.3
# Draw Colorful Python based on e2.1

import turtle

turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
# turtle.pencolor("purple")
turtle.seth(-40)
colorlist = ["green", "blue", "yellow", "red", "purple", "violet"]
# turtle.colormode(255)

for i in range(4):
    turtle.pencolor(colorlist[i])
    # turtle.pencolor((i * 10), (i * 20), (i * 30))
    turtle.circle(40, 80)
    # turtle.pencolor((i * 10), (i * 20), (i * 30))
    turtle.circle(-40, 80)

turtle.pencolor(colorlist[-1])
turtle.circle(40, 80 / 2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2 / 3)

turtle.done()
