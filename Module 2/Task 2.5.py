# Ask the user for input
talents = float(input("Enter talents:\n"))
pounds = float(input("Enter pounds:\n"))
lots = float(input("Enter lots:\n"))

# Conversion constants
GRAMS_IN_LOT = 13.3
LOTS_IN_POUND = 32
POUNDS_IN_TALENT = 20

# Convert everything to grams
total_grams = (talents * POUNDS_IN_TALENT * LOTS_IN_POUND * GRAMS_IN_LOT) \
            + (pounds * LOTS_IN_POUND * GRAMS_IN_LOT) \
            + (lots * GRAMS_IN_LOT)

# Convert grams to kilograms and grams
kilograms = int(total_grams // 1000)  # full kilos
grams = total_grams % 1000            # remainder grams

# Print the result
print("The weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")
