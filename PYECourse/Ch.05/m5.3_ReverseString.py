# Ch.05.6.2 Reverse String


def reverse(s):
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]


str = input("Please input a string: ")

print(reverse(str))
