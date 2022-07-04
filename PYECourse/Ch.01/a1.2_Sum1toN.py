# Ch.01 Exercise 1.2
# Sum or 1+2+3...+N

n = input("Please enter an integer N: ")
sum = 0
for i in range(int(n)):
    sum += i + 1

print("Sum from 1 to N: ", sum)
