# Exercise 14 of "Learn Python3 the Hard Way"
# Prompting and Passing
#
# need to run throught terminal (command prompt) with proper (enough) arguments

from sys import argv

script, user_name = argv
prompt = "> "

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to as you a few quetions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(
    f"""
Alright, so you said {likes} about liking me.
You live in {lives}.  Not sure where that is.
And you have a {computer} computer.  Nice.
"""
)
