# Ch.05.6.2 Calculate Factorial


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


num = eval(input("Please input a integer: "))

print(fact(abs(int(num))))
