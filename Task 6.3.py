# function to convert gallons to liters
def gallons_to_liters(gallons):
    return gallons * 3.78541   # 1 gallon = 3.78541 liters

# main program
gallons = float(input("Enter gallons (negative number to stop): "))

while gallons >= 0:
    liters = gallons_to_liters(gallons)
    print(gallons, "gallons is", liters, "liters")
    gallons = float(input("Enter gallons (negative number to stop): "))

print("Program ended")
