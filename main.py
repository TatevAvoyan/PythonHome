import random


def guessNum():
    num = random.randrange(1, 15)
    print(num)
    guess = int(input("Guess the number: "))
    count = 0

    while count < 100:
        count += 1
        if num == guess:
            print("Congratulations you did it in ", count, " try")
            break
        if num < guess:
            print("You guessed too high!")
            guess = int(input("Guess the number: "))
        if num > guess:
            print("You guessed too small!")
            guess = int(input("Guess the number: "))

guessNum()
