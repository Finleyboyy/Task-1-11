import random

# function to roll a dice with given sides
def roll_dice(sides):
    return random.randint(1, sides)

# main program
sides = int(input("How many sides does the dice have? "))

result = 0

while result != sides:
    result = roll_dice(sides)
    print("You rolled:", result)
