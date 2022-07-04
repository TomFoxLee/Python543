# Ch.03.4 Performace of Day Day Up 365
# Weekday: +0.01 per day
# Weekend: -0.01 per day

# import math

dayup, dayfactor = 1, 0.01

for i in range(365):
    if i % 7 in [6, 0]:
        dayup = dayup * (1 - dayfactor)
    else:
        dayup = dayup * (1 + dayfactor)

print("Up 5-Day Down 2-Day: {:.2f}.".format(dayup))
