import random

# function to roll a dice
def roll_dice():
    return random.randint(1, 6)

# main program
result = 0

while result != 6:
    result = roll_dice()
    print("You rolled:", result)
