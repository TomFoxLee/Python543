# Ch.06 Exercise 6.2, 6.3 Official Answer
# Enter a list and check if an element is duplicated

import random


def main():
    num = []
    n = input("Please input a set of numbers (or press Enter to finish): ")

    while n != "":
        num.append(eval(n))
        n = input("Please input a set of numbers (or press Enter to finish): ")
    else:
        print("Processing... Please Wait...")
        judge(num)


def judge(n):
    if len(n) == len(set(n)):
        print("No Duplication!")
    else:
        print("{} duplicate elements".format(len(n) - len(set(n))))


main()
