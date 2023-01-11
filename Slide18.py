from random import *
import random


def main():
    points = 0
    wrong = 0
    while wrong < 3:
        result = play()
        if result == 0:
            wrong += 1
        else:
            points += 1

    print("You earned", points, "Total points.")


def play():
    operands = random.randint(2, 5)
    sum = random.randint(1, 10)
    print(sum, end="")

    for i in range(2, operands+1):
        n = random.randint(1, 10)
        sum += n
        print(" +", n, end="")
    print(" = ", end="")

    guess = int(input())
    if guess == sum:
        return 1
    else:
        print("Wrong! The answer was", sum)
        return 0

main()