import sqlite3

# connect to the database
connection = sqlite3.connect("airports.db")
print("✅ Database connected!")

# check tables
cursor = connection.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables in database:", cursor.fetchall())

connection.close()
