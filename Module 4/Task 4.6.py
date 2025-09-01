import random

# ask user how many points
points = int(input("How many random points to generate: "))

inside = 0
total = 0

# make points one by one
while total < points:
    x = random.uniform(-1, 1)   # random x between -1 and 1
    y = random.uniform(-1, 1)   # random y between -1 and 1
    total = total + 1

    # check if point is inside circle
    if x*x + y*y < 1:
        inside = inside + 1

# formula pi ~ 4 * inside / total
pi_value = 4 * inside / total

print("Approximation of pi is", pi_value)
