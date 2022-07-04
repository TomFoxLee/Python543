# Ch.04.6 PI calculation

""" from random import random
from math import sqrt
from time import clock """

# time.clock() is replaced by time.process_time()
import random, math, time

DARTS = 10000
# hits = 0.0
hits = 0
time.process_time()

for i in range(1, DARTS + 1):
    x, y = random.random(), random.random()
    # print(x, y)
    dist = math.sqrt(x**2 + y**2)
    if dist < 1.0:
        hits = hits + 1

pi = 4 * (hits / DARTS)

print("PI value: {}".format(pi))
print("Process time: {:5.5} sec".format(time.process_time()))
