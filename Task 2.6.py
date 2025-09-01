import random

# Generate a 3-digit code (numbers 0–9)
code1 = [random.randint(0, 9) for _ in range(3)]

# Generate a 4-digit code (numbers 1–6)
code2 = [random.randint(1, 6) for _ in range(4)]

# Print the results
print("3-digit lock code:", code1)
print("4-digit lock code:", code2)
