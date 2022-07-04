# Ch.01.4.3 Some mini samples

# 1. Circle Area
#
print("Circle Area: ")
radius = 25
area = 3.1415 * radius * radius
print(area)
print("{:.2f}".format(area))
print("")


# 2. Name Interaction
#
print("Name Interaction: ")
name = input("Enter Name: ")
print("{} guy, Python for Future! ".format(name))
print("{} man, Python for Success! ".format(name[0]))
print("{} bro, Python for Love! ".format(name[1:]))
print("")


# 3. Fibonacci Sequence
#
print("Fibonacci Sequence: ")
a, b = 0, 1

while a < 1000:
    print(a, end=", ")
    a, b = b, a + b

print("\n")


# 5. Output Local Date & Time
#
print("Output Local Date & Time: ")
from datetime import datetime

now = datetime.now()
print(now)
print(now.strftime("%x"))
print(now.strftime("%X"))
print("")


# 4. Draw Tangent Circles
#

import turtle
from turtle import *

print("Draw Tangent Circles")
turtle.pensize(2)
turtle.circle(10)
# turtle.circle(20)
turtle.circle(40)
turtle.circle(80)
turtle.circle(160)
done()
print("")
