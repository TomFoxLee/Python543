# Ch.02 Exercise 2.2 Official Answer
# USD / RMB Currency Exchange; USD:RMB = 1:6

try:
    while 1:
        money = input("Please enter amount, for example: U2 / R6. E for exit: ")
        mode = money[0]

        if mode in ["U", "u"]:
            val = eval(money[1:])
            trans = val * 6
            print("{} ->> R{}".format(money, trans))
        elif mode in ["R", "r"]:
            val = eval(money[1:])
            trans = val / 6
            print("{} ->> U{}".format(money, trans))
        elif mode in ["E", "e"]:
            break
        else:
            print("Wrong input!")
except:
    print("Wrong input!")
