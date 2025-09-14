import mysql.connector

# Connect to MariaDB (use your working creds)
conn = mysql.connector.connect(
    host="localhost",
    user="appuser",
    password="app_pass_123",
    database="flight_game"
)

code = input("Enter area code (e.g. FI): ").upper().strip()

cur = conn.cursor()
cur.execute("""
    SELECT type, COUNT(*) 
    FROM airport
    WHERE iso_country = %s
    GROUP BY type
    ORDER BY type
""", (code,))

rows = cur.fetchall()

if not rows:
    print("No airports found for that country code.")
else:
    print(f"Airports in {code} by type:")
    for t, n in rows:
        # make the type a bit nicer to read
        pretty = t.replace("_", " ")
        print(f"- {pretty}: {n}")

cur.close()
conn.close()
