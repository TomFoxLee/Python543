# Ch.05 Exercise 5.5 Official Answer
# Check if a string is prime number and return True / False
# need to handle exception


def isPrime(num):
    import math

    try:
        if type(num) == type(0.0):
            raise TypeError
        r = int(math.floor(math.sqrt(num)))
    except TypeError:
        print(("It is not a valid integer!"))
        return None

    if num == 1:
        return False

    for i in range(2, r + 1):
        if num % i == 0:
            return False

    return True


print(isPrime(2))
print(isPrime(44))
print(isPrime("str"))
print(isPrime(1))
print(isPrime(3.3))
print(isPrime(0x18))
