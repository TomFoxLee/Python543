# Ch.07.8 Convert CSV to JSON

import json

fr = open(".\\PYECourse\\Ch.07\\price2016.csv", "r", encoding="utf-8")
ls = []

for line in fr:
    line = line.replace("\n", "")
    ls.append(line.split(","))

fr.close()

fw = open(".\\PYECourse\\Ch.07\\price2016.json", "w", encoding="utf-8")

for i in range(1, len(ls)):
    ls[i] = dict(zip(ls[0], ls[i]))

# json.dump(ls[1:], fw, sort_keys=True, indent=4)
json.dump(ls[1:], fw, sort_keys=True, indent=4, ensure_ascii=False)

fw.close()
