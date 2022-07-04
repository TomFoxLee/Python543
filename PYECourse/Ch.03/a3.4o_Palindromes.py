# Ch.03 Exercise 3.4 Official Answer
# Check if a Palindromes Number

while 1:
    hui = input("Please input a 5-digit number, or e to exit: ")
    if len(hui) == 5:
        if eval(hui) == eval(hui[-1:] + hui[3:4] + hui[2:3] + hui[1:2] + hui[0:1]):
            print("This is a Palindromes Number.")
        else:
            print("This is NOT a Palindromes Number.")
    elif hui[-1:] in ["e", "E"]:
        break
    else:
        print("Wrong Input!")
