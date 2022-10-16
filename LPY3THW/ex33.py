# Exercise 33 of "Learn Python3 the Hard Way"
# While Loops

i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numebers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)

# Practice
numbers2 = []
numbers3 = []


def while_test(times, inc):
    j = 0

    while j < (times * inc):
        print(f"\tAt the top j is {j}")
        numbers2.append(j)

        j = j + inc
        print("\tNumebers2 now: ", numbers2)
        print(f"\tAt the bottom j is {j}")


def for_test(times, inc):
    for k in range(0, times):
        print(f"\tAt the top k is {k}")
        numbers3.append(k * inc)
        print("\tNumebers3 now: ", numbers3)
        print(f"\tAt the bottom k is {k}")


times = int(input("\nPlease enter how many elements you want: "))
inc = int(input("Please enter the value you want to increment: "))
print("\n")

print("Processing Numbers2: ")
while_test(times, inc)
print("The Numbers2: ", numbers2, "\n")

print("Processing Numbers3: ")
for_test(times, inc)
print("The numbers3: ", numbers3, "\n")
