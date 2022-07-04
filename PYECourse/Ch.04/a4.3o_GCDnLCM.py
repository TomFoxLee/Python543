# Ch.04 Exercise 4.3 Official Answer
# Calculate GCD (Greatest Common Divisor) and LCM (Least Common Multiple)

a, b = eval(input("Please input 2 numbers for GCD & LCM, divided by ',': "))

c = a * b

if a < b:
    a, b = b, a

while False == (a in [0, 1]):
    b, a = a, b % a

c = c / b

print("GCD: {}, LCM: {}".format(b, c))
