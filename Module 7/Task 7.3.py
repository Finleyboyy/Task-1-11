# dictionary to store airports
airports = {}

while True:
    choice = input("Do you want to enter new, fetch, or quit?: ")

    if choice == "new":
        icao = input("Enter ICAO code: ")
        name = input("Enter airport name: ")
        airports[icao] = name
        print("Airport saved.")

    elif choice == "fetch":
        icao = input("Enter ICAO code: ")
        if icao in airports:
            print("Airport name:", airports[icao])
        else:
            print("No airport found with that ICAO code.")

    elif choice == "quit":
        print("Program ended.")
        break

    else:
        print("Invalid choice, type new, fetch, or quit.")
