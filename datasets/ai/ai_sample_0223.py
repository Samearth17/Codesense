import sqlite3

conn = sqlite3.connect("example.db")
cur = conn.cursor()

sql = "SELECT name FROM sqlite_master WHERE type='table';"
cur.execute(sql)
tables = cur.fetchall()

count = 0
for table in tables:
    sql = f"SELECT COUNT(*) FROM {table[0]};"
    cur.execute(sql)
    count += cur.fetchone()[0]

print(f"Number of entries: {count}")