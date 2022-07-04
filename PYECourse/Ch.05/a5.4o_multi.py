# Ch.05 Exercise 5.4 Official Answer
# multiple all parameters


def multi(*args):
    sum = 1
    count = 1

    for i in args:
        if (type(i) is type(1)) or (type(i) is type(1.0)):
            sum *= i
        else:
            print("The {}th parameter is not a valid number!".format(count))

        count += 1

    return sum


print(multi(2, 3, 1.0, 5, 4.99))
print(multi(2, 1, "str"))
print(multi())
