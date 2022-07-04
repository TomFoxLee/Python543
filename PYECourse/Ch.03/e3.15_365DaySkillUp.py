# Ch.03.4 Performace of 365 Day Skill Up
# Start with 1, only the first 10 days in every month has skill improve N, rest of the month are flat

# import math


def dayUP(df):
    dayup = 1

    for i in range(365):
        if i % 30 in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            dayup = dayup * (1 + df)
        else:
            dayup = dayup * (1)

    return dayup


# dayfactor = (0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10)
dayfactor = (0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009, 0.010)

print("365 Days, 6 contiune working day with skill up factor, rest 1 days are flat.")

for i in range(len(dayfactor)):
    # print("Factor {:.2f}: {:.2f}".format(dayfactor[i], dayUP(dayfactor[i])))
    print("Factor {:.3f}: {:.3f}".format(dayfactor[i], dayUP(dayfactor[i])))
