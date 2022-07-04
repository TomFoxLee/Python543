# Ch.03.4 Performace of Day Day Up 365
# Study: +0.001 per day
# Lazy: -0.001 per day

import math

dayup = math.pow((1.0 + 0.001), 365)
daydown = math.pow((1.0 - 0.001), 365)

print("Up: {:.2f}; Down: {:.2f}.".format(dayup, daydown))
