# Ch.03.7.1 Text Progress Bar

import time

scale = 10

print("------Ready_Go------")

for i in range(scale + 1):
    a, b = "**" * i, ".." * (scale - i)
    c = (i / scale) * 100
    print("{:>3.0f}% [{}->{}]".format(c, a, b))
    time.sleep(0.5)

print("------Complete------")
