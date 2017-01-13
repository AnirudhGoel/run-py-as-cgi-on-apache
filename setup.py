#!/usr/bin/python3

# 
# 
# This files makes a DB and adds some data to it but currently it doesn't print data from it. It just prints some dummy data.
# 
# 

import sqlite3
import json

response = {}
conn = sqlite3.connect("store.db")
# print("Connected to database")

try:
    conn.execute("CREATE TABLE IF NOT EXISTS STORE (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NAME TEXT NOT NULL, QUANTITY INT NOT NULL DEFAULT 0, DESCRIPTION TEXT, CATEGORY TEXT)")
    # print("Created Table STORE")
except Exception as e:
    print(e)

#
# Check if Table is Empty
#
cursor = conn.execute("SELECT EXISTS(SELECT 1 FROM STORE)")
for value in cursor:
    number_of_rows = value[0]

#
# Adding sample data if Table is Empty
#
if number_of_rows == 0:
    try:
        values_to_insert = [('Apple', 450, 'California', 'Mobile'), ('Mouse', 370, 'Wireless + Bluetooth', 'Computer Peripheral'), ('Bru Classic', 500, 'Classic Coffee', 'Food Items')]
        conn.executemany("""INSERT INTO STORE (NAME, QUANTITY, DESCRIPTION, CATEGORY) VALUES (?, ?, ?, ?)""", values_to_insert)
        conn.commit()
    except Exception as e:
        print(e)

#
# Display data of Table
#
# try:
#     cursor = conn.execute("SELECT * FROM STORE")
#     for row in cursor:
#         print("ID = ", row[0])
#         print("Name = ", row[1])
#         print("Quantity = ", row[2])
#         print("Description = ", row[3])
#         print("Category = ", row[4], "\n")
#     conn.close()
# except Exception as e:
#     print(e)


response["Name"] = "Luke"
response["Country"] = "Canada"

print("Content-Type: application/json\n")

print(json.dumps(response, ensure_ascii=False))
