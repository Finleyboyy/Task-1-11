# function to remove odd numbers
def remove_odds(numbers):
    evens = []
    for n in numbers:
        if n % 2 == 0:   # check if even
            evens.append(n)
    return evens

# main program
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = remove_odds(my_list)

print("Original list:", my_list)
print("Even numbers only:", new_list)
