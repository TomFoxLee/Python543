# Ch.04 Exercise 4.6 Official Answer
# Goat Car Door Question
# 3 doors (1 door: car, 2 door: goat)
# Player choose a door first, then host will open another door with goat
# Then player can change the choisen door.  Will the winning ratio increased if player change the door?

import random

times = eval(input("Please enter the times you want to simulate: "))

pick_first_n = 0
pick_change_n = 0

for i in range(times):
    car = random.randint(0, 2)
    pick_first = random.randint(0, 2)

    if pick_first == car:
        pick_first_n += 1
    else:
        pick_change_n += 1

pick_first_persent = pick_first_n / times
pick_change_persent = pick_change_n / times

print(
    "The winning ratio for stay with first choose: {:.2f}%".format(
        pick_first_persent * 100
    )
)
print(
    "The winning ratio for change the choice: {:.2f}%".format(pick_change_persent * 100)
)
