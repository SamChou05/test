import random

num1 = random.randrange(1,101)

gameWon = False

while not gameWon:
    guess = int(input("Guess a number: "))
    if (guess > num1):
        print("lower")
    elif (guess < num1):
        print("higher")
    else:
        print("You win!")
        gameWon = True


