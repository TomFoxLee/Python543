# Exercise 13 of "Learn Python3 the Hard Way"
# Parameters, Unpacking, Variables
#
# "from sys import argv" to use arguments
# need to run throught terminal (command prompt) with proper (enough) arguments

from sys import argv

# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
