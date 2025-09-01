numbers = []

# keep asking until the user enters empty string
num = input("Enter a number: ")

while num != "":
    numbers.append(float(num))
    num = input("Enter a number: ")

# only check if list has numbers
if len(numbers) > 0:
    print("Smallest number is", min(numbers))
    print("Largest number is", max(numbers))
else:
    print("No numbers were entered")
