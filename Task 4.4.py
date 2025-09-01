import random

# computer picks a number once
secret = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

# keep asking until correct
while guess != secret:
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    guess = int(input("Guess again: "))

print("Correct! The number was", secret)
