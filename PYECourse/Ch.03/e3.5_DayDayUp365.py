# Ch.03.4 Performace of Day Day Up 365
# find out the necessary 5 weekday improvement which can competite daily 0.01 up for 365 days (37.78)

# import math


def dayUP(df):
    dayup = 0.01

    for i in range(365):
        if i % 7 in [6, 0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)

    return dayup


dayfactor = 0.01

while dayUP(dayfactor) < (37.78):
    dayfactor += 0.001

print("The necessary weekday daily improvement: {:.3f}.".format(dayfactor))
