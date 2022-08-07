# Ch.07.4.3 write D1 to CSV

fo = open(".\\PYECourse\\Ch.07\\price2016bj.csv", "w", encoding="utf-8")
ls = ["北京", "101.5", "120.7", "121.4"]
fo.write(",".join(ls) + "\n")
fo.close()
