# make empty set
names = set()

# keep asking until empty
name = input("Enter a name: ")

while name != "":
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
    name = input("Enter a name: ")

# print all names
print("The names entered were:")
for n in names:
    print(n)
