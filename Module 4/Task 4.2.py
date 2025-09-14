inch = float(input("Enter inches (negative number to stop): "))

while inch >= 0:
    cm = inch * 2.54
    print(inch, "inches is", cm, "cm")
    inch = float(input("Enter inches (negative number to stop): "))

print("Program ended")
