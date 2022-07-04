# Ch.03.4 Performace of Day Day Up 365
# Study: +0.005 per day
# Lazy: -0.005 per day

import math

dayup = math.pow((1.0 + 0.005), 365)
daydown = math.pow((1.0 - 0.005), 365)

print("Up: {:.2f}; Down: {:.2f}.".format(dayup, daydown))
