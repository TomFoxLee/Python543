# Ch.04 Exercise 4.2
# Count charater from input string
# a~z, 0~9, space, others

test_str = input("Please enter a string for testing: ")

count_char, count_num, count_space, count_others = 0, 0, 0, 0

for i in test_str:
    if "a" <= i <= "z":
        count_char += 1
    elif "A" <= i <= "Z":
        count_char += 1
    elif "0" <= i <= "9":
        count_num += 1
    elif i == " ":
        count_space += 1
    else:
        count_others += 1

print(
    "Characters: {}, Numbers: {}, Space: {}, Others: {}".format(
        count_char, count_num, count_space, count_others
    )
)
