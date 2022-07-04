# Ch.03.7.3 Text Progress Bar at same line with refresh

import time

scale = 50

print("Ready_Go".center(scale // 2, "-"))

# t = time.clock()
t = time.process_time()
# print(t)

for i in range(scale + 1):
    a = "*" * i
    b = "-" * (scale - i)
    c = (i / scale) * 100
    # t -= time.clock()
    t -= time.process_time()
    # t = t - time.process_time()

    # print(" {} ".format(t))

    if c > 0:
        print("\r{:>3.0f}% [{}->{}] {:.2f}s".format(c, a, b, -t), end="")

    time.sleep(0.05)

print("\n" + "Complete".center(scale // 2, "-"))
