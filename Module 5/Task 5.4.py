cities = []

# ask 5 times
for i in range(5):
    name = input("Enter city name: ")
    cities.append(name)

# print each city
print("The cities you entered are:")
for city in cities:
    print(city)
