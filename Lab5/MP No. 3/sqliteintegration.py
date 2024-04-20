import sqlite3

conn = sqlite3.connect('ColonialAdventureToursDB.db')

cursor = conn.cursor()

cursor.execute("SELECT * FROM CUSTOMER;")
rows = cursor.fetchall()
for row in rows:
    print(row)

print('\t\tFigure 1. CUSTOMERS Table from ColonialAdventureToursDB')