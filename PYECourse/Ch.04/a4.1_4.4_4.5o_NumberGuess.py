# Ch.04 Exercise 4.1, 4.4, & 4.5 Official Answer
# Guess a number from 0 to 100.
# Will show "Too Big" or "too small".
# will show the total guess time when get right number.
# Not-interger will ask to re-enter

# from random import randint
import random, types

random.seed(100)
num = random.randint(0, 100)
tim = 0

while 1:
    try:
        putnum = eval(input("Please enter the number you guess: "))

        if type(putnum) == type(1):
            tim += 1

            if putnum > num:
                print("Too Big!")
            elif putnum < num:
                print("too small!")
            elif putnum == num:
                print("Guess {} times, You got it!".format(tim))
                break

        else:
            print("Must be an integer!")

    except:
        print("Wrong Input!")
