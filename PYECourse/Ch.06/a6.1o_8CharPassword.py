# Ch.06 Exercise 6.1 Official Answer
# Randomly generate 10 password has 8 characters long
# using A~Z, a~z, 0~9

import random


def rancre():
    mi = ""

    for i in range(8):
        u = random.randint(0, 62)
        if u >= 10:
            if 90 < (u + 55) < 97:
                mi += chr(u + 62)
            else:
                mi += chr(u + 55)

            print("{} ".format(u + 55), end="")
        else:
            mi += "%d" % u

    return mi


def main():
    for i in range(1, 11):
        print("The {}th password is: {}".format(i, rancre()))


main()
