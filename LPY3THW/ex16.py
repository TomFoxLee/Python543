# Exercise 16 of "Learn Python3 the Hard Way"
# Reading and Writing Files
#
# close(), read(), readline(), truncate(), write("stuff"), seek(0)
# open mode: r, r+, w, w+, a, a+
# seek(0) moving the file handle position to the beginning of the file.

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit Ctrl-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, "w")

print("Truncating the file.  Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()

# Practice
print("\n# Practice #")
# target = open(filename, "r+")
# txt1 = target2.read()  ## wrong statement
target = open(filename, "a+")
# seek(0) moving the file handle position to the beginning of the file.
target.seek(0)
print("\nRead Again!\n{}".format(target.read()))

lines = (
    "  === below are added by Practice===\n  "
    + line1
    + "\n  "
    + line2
    + "\n  "
    + line3
    + "\n  "
)
target.write(lines)

target.seek(0)
print("\nRead One More Time!\n{}".format(target.read()))

target.close()
