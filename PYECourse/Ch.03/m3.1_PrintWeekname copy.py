# Ch.03.5.2 Print Weekday Name

weekstr = "MonTueWedThrFriSatSun"

weekid = eval(input("Please Enter Weekday Number (1-7): "))
pos = (weekid - 1) * 3

print(weekstr[pos : pos + 3])
