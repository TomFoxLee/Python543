# Ch.07.4.3 write D2 to CSV

fr = open(".\\PYECourse\\Ch.07\\price2016.csv", "r", encoding="utf-8")
fw = open(".\\PYECourse\\Ch.07\\price2016out.csv", "w", encoding="utf-8")
ls = []

for line in fr:
    line = line.replace("\n", "")
    ls.append(line.split(","))

for i in range(len(ls)):
    for j in range(len(ls[i])):
        if ls[i][j].replace(".", "").isnumeric():
            ls[i][j] = "{:.2}%".format(float(ls[i][j]) / 100)

for row in ls:
    print(row)
    fw.write(",".join(row) + "\n")

fr.close()
fw.close()
