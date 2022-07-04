# Ch.02 Exercise 2.9 Official Answer
# Draw Python

import turtle

# turtle.setup()
turtle.colormode(255)
turtle.pensize(20)
turtle.pencolor(255, 255, 255)
turtle.speed(100000)


def changedraw():
    penr = 254
    for i in range(100):
        turtle.circle(100, 1)
        penr -= 1
        turtle.pencolor((penr, penr - 1, penr - 2))
    for u in range(100):
        turtle.circle(-100, 1)
        penr -= 1
        turtle.pencolor((penr, penr - 1, penr - 2))


changedraw()

turtle.done()
