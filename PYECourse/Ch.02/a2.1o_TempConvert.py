# Ch.02 Exercise 2.1 Official Answer
# Celsius / Fabrenheit Temperature Convert, output as integer

temp = eval(input("Please input Fabrenheit Temperature: "))
C = (temp - 32) / 1.8
print("Converted Celsius Temperature is: {}C".format(int(C)))

print("")

temp = eval(input("Please input Celsius Temperature: "))
F = 1.8 * temp + 32
print("Converted Fabrenheit Temperature is: {}F".format(int(F)))
