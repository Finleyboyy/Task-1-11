cabin = input("Enter cabin class (LUX, A, B, C): ")

if cabin == "LUX":
    print("Upper deck cabin with a balcony.")
elif cabin == "A":
    print("Cabin above the car deck with a window.")
elif cabin == "B":
    print("Cabin above the car deck without a window.")
elif cabin == "C":
    print("Cabin below the car deck without a window.")
else:
    print("Invalid cabin class.")
