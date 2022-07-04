# Ch.01 Exercise 1.4
# Calculate sum of 1+2!+3!+...+10!

sum, tmp = 0, 1
for i in range(1, 11):
    tmp += i
    sum += tmp

print("Result: ", format(sum))
