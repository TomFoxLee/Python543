# Ch.05 Exercise 5.2 Official Answer
# Check if a string is odd number


def isOdd(num):
    try:
        if type(num) == type(0.0):
            raise TypeError

        if num % 2 == 0:
            return False
        else:
            return True
    except TypeError:
        print("It is not a valid integer! ", end="")


print(isOdd(4))
print(isOdd(3))
print(isOdd(-1))
print(isOdd("str"))
print(isOdd(3.0))
