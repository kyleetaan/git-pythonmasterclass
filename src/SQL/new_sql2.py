import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = "anotherupdate@update.com"
phone = input("Please enter the phone number: ")

# update_sql = "UPDATE contacts SET email = '{}' WHERE contacts.phone = {}".format(new_email, phone)
# ? placeholder
update_sql = "UPDATE contacts SET email = ? WHERE contacts.phone = ?"
update_cursor = db.cursor()
# put place holder here at cursor
update_cursor.execute(update_sql, (new_email, phone))
print("{} row/s updated".format(update_cursor.rowcount))

#update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name, "\n", phone, "\n", email)
    print("-" * 20)
db.close()