# Ch.07.1.3 Print file by lines

fname = input("Please input file name to read: ")
fo = open(fname, "r")

# read complete file into a list then do processing
for line in fo.readlines():
    print(line)

# read 1 line per each time to do processing, save memory
for line in fo:
    print(line)

fo.close()
