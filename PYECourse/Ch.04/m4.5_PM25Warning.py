# Ch.04.2.2 PM2.5 Warning
# PM<35: Excellent, 35<=PM<75: Gooe. 75<=PM: Bad.

PM = eval(input("Please Enter PM2.5 value: "))

if PM < 0:
    print("Wrong Input!")

""" if 0 <= PM < 35:
    print("Excellent Air! ^o^")
if 35 <= PM < 75:
    print("Good Air! 0.0") """

""" if 75 <= PM:
    print("Bad Air! x_x")
else:
    print("OK Air! O.o") """

print("{} Air!".format("OK" if PM < 75 else "Bad"))
