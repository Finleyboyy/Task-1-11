# Create an empty set to store names
names = set()

while True:
    # Ask the user to type a name
    name = input("Enter a name (or press Enter to stop): ")

    # If the user just presses Enter, stop the loop
    if name == "":
        break

    # Check if the name is already in the set
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)  # Add the name to the set

# After the loop, print all names
print("\nList of names:")
for n in names:
    print(n)
