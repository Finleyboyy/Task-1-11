numbers = []

# keep asking until empty string
num = input("Enter a number: ")
while num != "":
    numbers.append(int(num))
    num = input("Enter a number: ")

# sort numbers from biggest to smallest
numbers.sort(reverse=True)

# print only the top 5
print("The five greatest numbers are:")
print(numbers[:5])
