# Ch.05.1.1 Happy Birthday


def happy():
    print("Happy Birthday to You!")


def happyB(name):
    happy()
    happy()
    print("Happy Birthday, Dear {}!".format(name))
    happy()


happyB("Mike")
print()
happyB("Lily")
