import random

# ask how many dice
dice = int(input("How many dice to roll: "))

total = 0

# roll dice one by one
for i in range(dice):
    roll = random.randint(1, 6)   # random number between 1 and 6
    total = total + roll

print("The sum of the dice is", total)
