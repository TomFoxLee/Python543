# Ch.06 Exercise 6.5 Official Answer
# Birthday Paradox
# if there are 23 or more people in a group, then the ratio of birthday duplication is higher than 50%

import random


def randbirth():
    mon = random.randint(1, 12)

    if mon in [1, 3, 5, 7, 8, 10, 12]:
        day = random.randint(1, 31)
    elif mon == 2:
        day = random.randint(1, 28)
    else:
        day = random.randint(1, 30)

    return mon * 100 + day


def main():
    ls = []

    for i in range(23):
        ls.append(randbirth())

    if len(ls) == len(set(ls)):
        return 1
    else:
        return 0


try:
    poss = 0
    n = eval(input("Please input headcount: "))

    for i in range(n):
        if main() == 1:
            poss += 1

    if (poss / n) >= 0.5:
        print(
            "When headcount is >= 23, the B-Day duplication ratio >= 50%, is {}%".format(
                poss * 100 / n
            )
        )
    else:
        print(
            "When headcount is 23, the B-Day duplication ratio < 50%, is {}%".format(
                poss * 100 / n
            )
        )

except:
    print("Wrong Input!")
