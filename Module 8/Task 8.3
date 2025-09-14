import mysql.connector
from geopy.distance import geodesic

# Connect to MariaDB
conn = mysql.connector.connect(
    host="localhost",
    user="appuser",
    password="app_pass_123",
    database="flight_game"
)

cur = conn.cursor()

# Ask for two ICAO codes
icao1 = input("Enter first ICAO code: ").upper().strip()
icao2 = input("Enter second ICAO code: ").upper().strip()

# Get coordinates for the first airport
cur.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident=%s", (icao1,))
row1 = cur.fetchone()

# Get coordinates for the second airport
cur.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident=%s", (icao2,))
row2 = cur.fetchone()

if row1 and row2:
    coords1 = (row1[0], row1[1])
    coords2 = (row2[0], row2[1])

    distance = geodesic(coords1, coords2).kilometers
    print(f"Distance between {icao1} and {icao2} is {distance:.2f} km")
else:
    print("One or both ICAO codes not found in the database.")

cur.close()
conn.close()
