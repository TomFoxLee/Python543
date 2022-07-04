# Ch.04 Exercise 4.7 Official Answer
# Celsius / Fabrenheit Temperature Convert
# use try-excpet to handle all kinds of input

temp_str = input("Please enter Temperature with sign at end: ")

if temp_str[-1] in ["F", "f"]:
    try:
        c = (eval(temp_str[:-1]) - 32) / 1.8
        print("Converted temperature is: {:.2f}C".format(c))
    except:
        print("Wrong Input Format!")

elif temp_str[-1] in ["C", "c"]:
    try:
        f = 1.8 * (eval(temp_str[:-1])) + 32
        print("Converted temperature is: {:.2f}F".format(f))
    except:
        print("Wrong Input Format!")

else:
    print("Wrong Input Format!")
