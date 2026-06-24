import random

secret_number = random.randint(1,100)

attempts = 0

print("Welcome to Number Guessuing Game")

while True:
    guess = int(input("Enter your guess number:"))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print("Correct! you guessed the number.")
        print("Number of attempts:", attempts)
        break
    