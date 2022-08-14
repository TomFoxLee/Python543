# Ch.07.8 Convert JSON to CSV

import json

fr = open(".\\PYECourse\\Ch.07\\price2016.json", "r", encoding="utf-8")
ls = json.load(fr)
data = [list(ls[0].keys())]

for item in ls:
    data.append(list(item.values()))

fr.close()

fw = open(".\\PYECourse\\Ch.07\\price2016_from_json.csv", "w", encoding="utf-8")

for item in data:
    fw.write(",".join(item) + "\n")

fw.close()
