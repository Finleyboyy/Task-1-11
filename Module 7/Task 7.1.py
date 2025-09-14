# save seasons in a tuple
seasons = ("winter", "spring", "summer", "autumn")

month = int(input("Give month number (1-12): "))

if month == 12 or month == 1 or month == 2:
    print(seasons[0])  # winter
elif month == 3 or month == 4 or month == 5:
    print(seasons[1])  # spring
elif month == 6 or month == 7 or month == 8:
    print(seasons[2])  # summer
elif month == 9 or month == 10 or month == 11:
    print(seasons[3])  # autumn
else:
    print("Invalid month")
