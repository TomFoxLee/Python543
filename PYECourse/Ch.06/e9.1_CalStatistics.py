# Ch.06.3 Calculate Statistics

import math


def getNum():
    nums = []
    iNumStr = input("Please input number (press Enter as finish): ")

    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("Please input number (press Enter as finish): ")

    return nums


def mean(numbers):
    s = 0.0

    for num in numbers:
        s = s + num

    return s / len(numbers)


def dev(numbers, mean):
    sdev = 0.0

    for num in numbers:
        sdev = sdev + (num - mean) ** 2

    return math.sqrt(sdev / (len(numbers) - 1))


def median(numbers):
    # print(numbers)
    # sorted(numbers)
    numbers = sorted(numbers)
    # print(numbers)
    size = len(numbers)

    if size % 2 == 0:
        med = (numbers[size // 2 - 1] + numbers[size // 2]) / 2
    else:
        med = numbers[size // 2]

    return med


n = getNum()
m = mean(n)

print("Average: {}, Dev: {:.2}, Median: {}".format(m, dev(n, m), median(n)))
