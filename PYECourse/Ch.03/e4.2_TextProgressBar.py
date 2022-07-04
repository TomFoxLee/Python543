# Ch.03.7.2 Text Progress % at same line

import time

for i in range(101):
    print("\r{:2}%".format(i), end="")
    time.sleep(0.05)
