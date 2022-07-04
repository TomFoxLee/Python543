# Ch.01.4.3 Some mini samples

# 5. Output Local Date & Time
#
print("Output Local Date & Time: ")
from datetime import datetime

now = datetime.now()
print(now)
print(now.strftime("%x"))
print(now.strftime("%X"))
# print("")
