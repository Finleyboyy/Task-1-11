# # import sqlite3
# #
# # # connect to the database (change filename if needed)
# # connection = sqlite3.connect("airports.db")
# #
# # icao = input("Enter ICAO code: ")
# #
# # # make a cursor to run commands
# # cursor = connection.cursor()
# #
# # # fetch airport name and town with the ICAO code
# # cursor.execute("SELECT name, municipality FROM airport WHERE ident = ?", (icao,))
# # row = cursor.fetchone()
# #
# # if row:
# #     print("Airport name:", row[0])
# #     print("Location:", row[1])
# # else:
# #     print("No airport found with that ICAO code.")
# #
# # # close the connection
# #
# # connection.close()
# import mysql.connector
#
# DB = {
#     "host": "localhost",
#     "user": "appuser",
#     "password": "app_pass_123",
#     "database": "flight_game",
# }
#
# icao = input("Enter ICAO code: ").upper().strip()
#
# conn = mysql.connector.connect(**DB)
# cur = conn.cursor()
# cur.execute("SELECT name, municipality FROM airport WHERE ident=%s", (icao,))
# row = cur.fetchone()
# cur.close(); conn.close()
#
# if row:
#     print("Airport name:", row[0])
#     print("Location (town):", row[1])
# else:
#     print("No airport found with that ICAO code.")
import mysql.connector

# connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="appuser",
    password="app_pass_123",
    database="flight_game"
)

icao = input("Enter ICAO code: ").upper().strip()

cur = conn.cursor()
cur.execute("SELECT name, municipality FROM airport WHERE ident = %s", (icao,))
row = cur.fetchone()

if row:
    print("Airport name:", row[0])
    print("Location (town):", row[1])
else:
    print("No airport found with that ICAO code.")

cur.close()
conn.close()
