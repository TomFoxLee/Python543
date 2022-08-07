# Ch.07.4.3 get CSV data to List

fo = open(".\\PYECourse\\Ch.07\\price2016.csv", "r", encoding="utf-8")
ls = []

for line in fo:
    line = line.replace("\n", "")
    ls.append(line.split(","))

print(ls)
fo.close()
