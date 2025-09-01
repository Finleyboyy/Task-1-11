import sqlite3

# connect to the database (change filename if needed)
connection = sqlite3.connect("airports.db")

icao = input("Enter ICAO code: ")

# make a cursor to run commands
cursor = connection.cursor()

# fetch airport name and town with the ICAO code
cursor.execute("SELECT name, municipality FROM airport WHERE ident = ?", (icao,))
row = cursor.fetchone()

if row:
    print("Airport name:", row[0])
    print("Location:", row[1])
else:
    print("No airport found with that ICAO code.")

# close the connection

connection.close()
