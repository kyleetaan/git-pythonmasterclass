import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
#db.execute("INSERT INTO contacts(name, phone, email) VALUES('Kyle', 85854, 'kyle@email.com')")
#db.execute("INSERT INTO contacts VALUES('Luiz', 994494, 'luiz@email.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")
for row in cursor:
    print(row)

cursor.close()
db.commit()
db.close()