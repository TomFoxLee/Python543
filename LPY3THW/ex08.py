# Exercise 08 of "Learn Python3 the Hard Way"
# print, print

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(
    formatter.format(
        "Try your", "Own text here", "Maybe a poem", "Or a song about fear"
    )
)
