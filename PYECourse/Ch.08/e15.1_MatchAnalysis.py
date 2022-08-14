# Ch.08.3 Simulate a ball game result
# 2 Players, need to input winning ratio for each player, and how many games/rounds to simulate
# Player 1 serving first.  The player who did not hit ball is losing the round.
# If the player who is serving lost the round, next round will serve by the other player.
# The player who serve and win the round, get the point.
# The player who get 15 points first win the game.

from random import random


def printIntro():
    print("The program simulates a game for 2 Players A and B.")
    print("The program needs winning ratio of A and B.")


def getInputs():
    a = eval(input("Please enter winning ratio of A (0-1): "))
    b = eval(input("Please enter winning ratio of B (0-1): "))
    n = eval(input("How many games to simulate: "))

    return a, b, n


def gameOver(a, b):
    return a == 15 or b == 15


def simOneGame(probA, probB):
    scoreA, scoreB = 0, 0
    serving = "A"

    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"

    return scoreA, scoreB


def simNGames(n, probA, probB):
    winsA, winsB = 0, 0

    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)

        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1

    return winsA, winsB


def printSummary(winsA, winsB):
    n = winsA + winsB

    print("{} games are simulated.".format(n))
    print("Player A wins {} games, as {:0.1%}".format(winsA, winsA / n))
    print("Player B wins {} games, as {:0.1%}".format(winsB, winsB / n))


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)


main()
