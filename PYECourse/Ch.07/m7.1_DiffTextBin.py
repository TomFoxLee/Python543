# Ch.07.1.1 Difference of open file by Text and Binary

# textFile = open(".\\PYECourse\\Ch.07\\7.1.txt", "rt")
textFile = open(".\\PYECourse\\Ch.07\\7.1.txt", "rt", encoding="utf-8")
print(textFile.readline())
textFile.close()

binFile = open(".\\PYECourse\\Ch.07\\7.1.txt", "rb")
print(binFile.readline())
binFile.close()
