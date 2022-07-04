# Ch.02.2.11 Celsius / Fabrenheit Temperature Convert


def tempConvert(ValueStr):
    if ValueStr[-1] in ["F", "f"]:
        C = (eval(ValueStr[0:-1]) - 32) / 1.8
        print("Converted Temperature is {:.2f}C".format(C))
    elif ValueStr[-1] in ["C", "c"]:
        F = 1.8 * (eval(ValueStr[0:-1])) + 32
        print("Converted Temperature is {:.2f}F".format(F))
    else:
        print("Wrong Sign!")


TempStr = input("Please enter temperature with sign: ")
tempConvert(TempStr)
