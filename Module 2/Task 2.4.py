# Ask the user for three numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Calculate sum, product, and average
sum_numbers = num1 + num2 + num3
product_numbers = num1 * num2 * num3
average_numbers = sum_numbers / 3

# Print the results
print(f"The sum of the numbers is {sum_numbers}")
print(f"The product of the numbers is {product_numbers}")
print(f"The average of the numbers is {average_numbers}")
