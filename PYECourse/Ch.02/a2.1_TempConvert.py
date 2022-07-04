# Ch.02 Exercise 2.1
# Celsius / Fabrenheit Temperature Convert, output as integer

TempStr = input("Please enter temperature with sign: ")

if TempStr[-1] in ["F", "f"]:
    C = (eval(TempStr[0:-1]) - 32) / 1.8
    # print("Converted Temperature is {:.2f}C".format(C))
    print("Converted Temperature is {}C".format(int(C)))
elif TempStr[-1] in ["C", "c"]:
    F = 1.8 * (eval(TempStr[0:-1])) + 32
    # print("Converted Temperature is {:.2f}F".format(F))
    print("Converted Temperature is {}F".format(int(F)))
else:
    print("Wrong Sign!")
