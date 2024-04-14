import csv
import sqlite3

filename = "customers.csv"

rows = []

with open(filename, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        rows.append(row)

conn = sqlite3.connect('customers.sqlite')

c = conn.cursor()
query = "delete from Customer;"
c.execute(query)
for row in rows[1:]:
    c.execute(f"INSERT INTO Customer (firstName, lastName, companyName, address, city, state, zip) VALUES ('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}', '{row[6]}');")
conn.commit()
conn.close()
