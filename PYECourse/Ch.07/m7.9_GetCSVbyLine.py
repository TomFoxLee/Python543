# Ch.07.4.3 get CSV data by Line

fo = open(".\\PYECourse\\Ch.07\\price2016.csv", "r", encoding="utf-8")
ls = []

for line in fo:
    line = line.replace("\n", "")
    ls = line.split(",")
    lns = ""

    for s in ls:
        lns += "{}\t".format(s)

    print(lns)

fo.close()
