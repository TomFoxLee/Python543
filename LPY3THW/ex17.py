# Exercise 17 of "Learn Python3 the Hard Way"
# More Files
#
# use exist() to check if file alrady there.
# "w" overwrite only; "a+" append and read
# len()  # length of a string

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()
# indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# out_file = open(to_file, "w")
out_file = open(to_file, "a+")
out_file.write(indata)

print("Allrihgt, all done.")

out_file.close()
in_file.close()
