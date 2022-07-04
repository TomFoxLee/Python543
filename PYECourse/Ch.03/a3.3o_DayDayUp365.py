# Ch.03 Exercise 3.3 Official Answer
# 7 Days cycle, Day1~3 flat, Day4~7 increase 1% per day.
# Rest 1 day per every 10 days.  If rest, then the increase reset.
# What's the performance of 365 days?

dayup = 1
dayfactor = 0.01
period = [4, 5, 6, 0]
decrease = 0

for j in range(1, 366):
    temp = j - decrease
    tom = temp % 7

    if j % 10 == 0:
        decrease += j - (tom - 1)
        tom = 1

    if tom in period:
        dayup = dayup * (1 + dayfactor)

print("%f the result is %.2f" % (dayfactor, dayup))
