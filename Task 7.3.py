# # dictionary to store airports
# airports = {}
#
# while True:
#     choice = input("Do you want to enter new, fetch, or quit?: ")
#
#     if choice == "new":
#         icao = input("Enter ICAO code: ")
#         name = input("Enter airport name: ")
#         airports[icao] = name
#         print("Airport saved.")
#
#     elif choice == "fetch":
#         icao = input("Enter ICAO code: ")
#         if icao in airports:
#             print("Airport name:", airports[icao])
#         else:
#             print("No airport found with that ICAO code.")
#
#     elif choice == "quit":
#         print("Program ended.")
#         break
#
#     else:
#         print("Invalid choice, type new, fetch, or quit.")
# Dictionary to store airports
airports = {}

while True:
    print("\nChoose an option:")
    print("1 = Enter a new airport")
    print("2 = Fetch airport information")
    print("3 = Quit")

    choice = input("Your choice: ")

    if choice == "1":
        # Add new airport
        icao = input("Enter ICAO code: ").upper()
        name = input("Enter airport name: ")
        airports[icao] = name
        print("Airport saved!")

    elif choice == "2":
        # Fetch airport info
        icao = input("Enter ICAO code: ").upper()
        if icao in airports:
            print("Airport name:", airports[icao])
        else:
            print("No airport found with that ICAO code.")

    elif choice == "3":
        # Quit the program
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please select 1, 2, or 3.")
