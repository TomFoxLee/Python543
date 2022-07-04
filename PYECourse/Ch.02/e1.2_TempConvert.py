# Ch.02.2.10 Celsius / Fabrenheit Temperature Convert

TempStr = input("Please enter temperature with sign: ")

while TempStr[-1] not in ["N", "n"]:
    if TempStr[-1] in ["F", "f"]:
        C = (eval(TempStr[0:-1]) - 32) / 1.8
        print("Converted Temperature is {:.2f}C".format(C))
    elif TempStr[-1] in ["C", "c"]:
        F = 1.8 * (eval(TempStr[0:-1])) + 32
        print("Converted Temperature is {:.2f}F".format(F))
    else:
        print("Wrong Sign!")
    TempStr = input("Please enter temperature with sign: ")
