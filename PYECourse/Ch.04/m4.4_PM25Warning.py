# Ch.04.2.1 PM2.5 Warning
# PM<35: Excellent, 35<=PM<75: Gooe. 75<=PM: Bad.

PM = eval(input("Please Enter PM2.5 value: "))

if PM < 0:
    print("Wrong Input!")
# if 0 <= PM < 35:
elif 0 <= PM < 35:
    print("Excellent Air! ^o^")
# if 35 <= PM < 75:
elif 35 <= PM < 75:
    print("Good Air! 0.0")
# if 75 <= PM:
else:
    print("Bad Air! x_x")
