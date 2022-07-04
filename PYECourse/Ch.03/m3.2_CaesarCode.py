# Ch.03.5.2 Caesar Code

plaincode = input("Please Enter Plain Code: ")

for p in plaincode:
    if ord("a") <= ord(p) <= ord("z"):
        print(chr(ord("a") + (ord(p) - ord("a") + 3) % 26), end="")
    else:
        print(p, end="")
