# Exercise 11 of "Learn Python3 the Hard Way"
# Asking Questions
#
# input()
# x = int(input()); cannot input a non-integer string

from re import X


print("How old are you?", end=" ")
age = input()
print("How tall are you?", end=" ")
height = input()
print("How much do you weight?", end=" ")
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# Practice
print("\n# Practice #")
x = int(input("Please input a integer: "))
print(x)
