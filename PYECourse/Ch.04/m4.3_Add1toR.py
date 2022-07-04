# Ch.04.1.3 Add value from 1 to R

R = eval(input("Please Enter Positive Number: "))

i, S = 0, 0

if R < 0:
    print("Not a Postive Number!")
else:
    while i <= R:
        S = S + i
        i = i + 1

    print("Add valus from 1 to the Number: ", S)
