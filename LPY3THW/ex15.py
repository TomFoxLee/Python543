# Exercise 15 of "Learn Python3 the Hard Way"
# Reading Files
#
# need to run throught terminal (command prompt) with proper (enough) arguments
# file need to open(), read(), close()

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the file name again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

# Practice
file_input = input("Type the file name one more time: ")

txt_input = open(file_input)

print(txt_input.read())

txt.close()
txt_again.close()
txt_input.close()
