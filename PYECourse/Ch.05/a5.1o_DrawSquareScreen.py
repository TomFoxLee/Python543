# Ch.05 Exercise 5.1 Official Answer
# Draw Square Screen


def drawsq(n):
    line = 3 * n + 1

    for i in range(1, line + 1):
        if i % 3 == 1:
            print(n * "+-----", end="")
            print("+")
        else:
            print(n * "|     ", end="")
            print("|")


def main():
    n = eval(input("Please input square level: "))
    drawsq(n)


main()
