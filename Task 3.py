# Ask the user for the length of the fish
length = float(input("How long is the zander you caught (cm)?: "))

# Check if the fish is big enough
if length < 42:
    difference = 42 - length
    print(f"Too small! Throw it back, it's {difference:.1f} cm under the limit.")
else:
    print("Nice catch! It's big enough to keep.")
