# Ch.04 Exercise 4.2 Official Answer
# Count charater from input string
# a~z, 0~9, space, others

stri = input("Please enter your string: ")

kong = 0
alpha = 0
chi = 0
num = 0
other = 0

for i in stri:
    if i == " ":
        kong += 1
    elif "0" <= i <= "9":
        num += 1
    elif i >= "\u4e00" and i <= "\u9fa5":
        chi += 1
    elif True == i.isalpha():
        alpha += 1
    else:
        other += 1

print(
    "Space: {}, Numbers: {}, Chinese: {}, Characters: {}, Others: {}".format(
        kong, num, chi, alpha, other
    )
)
