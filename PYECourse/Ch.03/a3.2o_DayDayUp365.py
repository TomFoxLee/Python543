# Ch.03 Exercise 3.2 Officail Answer
# 7 Days cycle, Day1~3 flat, Day4~7 increase 1% per day.  What's the performance of 365 days?

dayup = 1

dayfactor = 0.01

for j in range(1, 366):
    if j % 7 in [4, 5, 6, 0]:
        dayup = dayup * (1 + dayfactor)

print("%f the result is %.2f" % (dayfactor, dayup))
