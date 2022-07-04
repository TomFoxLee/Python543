# Ch.02 Exercise 2.2
# USD / RMB Currency Exchange; USD:RMB = 1:6

print("Amout Example: USD 1 as U1, or RMB 1 as R1.")
AmountStr = input("Please enter amount with currency sign: ")

if AmountStr[0] in ["U", "u"]:
    R = eval(AmountStr[1:]) * 6
    print("RMB amount is RMB{:.2f}".format(R))
elif AmountStr[0] in ["R", "r"]:
    U = eval(AmountStr[1:]) / 6
    print("USD amount is USD{:.2f}".format(U))
else:
    print("Wrong input!")
