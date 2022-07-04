# Ch.05 Exercise 5.7 Official Answer
# Tower of Hanoi


def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move Disk 1 from source", source, "to destination", destination)
        return

    TowerOfHanoi(n - 1, source, auxiliary, destination)

    print("Move Disk", n, "from source", source, "to destination", destination)

    TowerOfHanoi(n - 1, auxiliary, destination, source)


n = eval(input("Please enter level of the Tower of Hanoi: "))
TowerOfHanoi(n, "A", "B", "C")
