import sqlite3

db = sqlite3.connect("contacts.sqlite")
name = input("Enter search name: ")
#sql = "SELECT * FROM contacts WHERE"

for row in db.execute("SELECT * FROM contacts WHERE name = ?", (name,)):
    print(row)

db.close()