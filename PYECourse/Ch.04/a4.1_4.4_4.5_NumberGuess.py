# Ch.04 Exercise 4.1, 4.4, & 4.5
# Guess a number from 0 to 100.
# Will show "Too Big" or "too small".
# will show the total guess time when get right number.
# Not-interger will ask to re-enter

import random, types

ans_num = random.randint(0, 100)
# print(ans_num)

guess_count = 0
# got_number = False

# while got_number == False:
while 1:
    try:
        guess_num = eval(input("Please enter a number between 0 to 100: "))

        if type(guess_num) == type(1):
            guess_count += 1

            if guess_num > ans_num:
                print("Too Big!")
            elif guess_num < ans_num:
                print("too small!")
            else:
                print("Number Correct! ", guess_num)
                print("Guess Time: ", guess_count)
                # got_number = True
                break

        else:
            print("Need to be an integer!")

    except:
        print("Wrong Input!")
