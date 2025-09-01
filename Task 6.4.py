# function that adds numbers in a list
def sum_list(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total

# main program
my_list = [1, 2, 3, 4, 5]

answer = sum_list(my_list)

print("The sum of the list is", answer)
