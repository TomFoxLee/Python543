# Ch.02 Exercise 2.8 Official Answer
# Draw Square Spiral

import turtle

turtle.left(90)

length = 5
speed = 20

for i in range(31):
    turtle.fd(length)
    turtle.left(90)
    # turtle.fd(length)
    # turtle.left(90)
    length += 5
    # turtle.fd(length)

turtle.done()
