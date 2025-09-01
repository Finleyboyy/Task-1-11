gender = input("Enter gender (male/female): ")
hemo = int(input("Enter hemoglobin value (g/l): "))

if gender == "female":
    if hemo < 117:
        print("Low value")
    elif hemo > 155:
        print("High value")
    else:
        print("Normal value")
elif gender == "male":
    if hemo < 134:
        print("Low value")
    elif hemo > 167:
        print("High value")
    else:
        print("Normal value")
else:
    print("Invalid gender")
