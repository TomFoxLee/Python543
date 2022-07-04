# Ch.03 Exercise 3.2
# 7 Days cycle, Day1~3 flat, Day4~7 increase 1% per day.  What's the performance of 365 days?

dayup = 1

for i in range(365):
    if (i + 1) % 7 in [1, 2, 3]:
        dayup = dayup * (1)
    else:
        dayup = dayup * (1 + 0.01)

print("7 Days cycle, Day1~3 flat, Day4~7 increase 1% per day.")
print("The perofrmance after 365 days is: {:.3f}.".format(dayup))
