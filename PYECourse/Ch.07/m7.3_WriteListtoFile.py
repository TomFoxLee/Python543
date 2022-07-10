# Ch.07.1.3 Print file by lines

fname = input("Please input file name to write: ")
fo = open(fname, "w+")

ls = ["Ryu", "Ken", "Guile"]
fo.writelines(ls)

fo.seek(0)
for line in fo:
    print(line)

fo.close()
