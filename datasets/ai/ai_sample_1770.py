import sqlite3

conn = sqlite3.connect('contacts.db')
c = conn.cursor()

c.execute("""CREATE TABLE contacts (
            first_name text,
            last_name text,
            phone_number text,
            email text
            )""")

c.execute("INSERT INTO contacts VALUES ('John', 'Doe', '1234567890', 'doe@example.com')")

conn.commit()
conn.close()