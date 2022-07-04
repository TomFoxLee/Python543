# Ch.03.4 Performace of Day Day Up 365
# Study: +0.01 per day
# Lazy: -0.01 per day
# set as dayfactor

import math

dayfactor = 0.01

dayup = math.pow((1.0 + dayfactor), 365)
daydown = math.pow((1.0 - dayfactor), 365)

print("Up: {:.2f}; Down: {:.2f}.".format(dayup, daydown))
