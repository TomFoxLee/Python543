# Ch.01 Exercise 1.8
# Draw Sun Flower

from turtle import *

color("red", "yellow")
begin_fill()

while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break

end_fill()
done()
