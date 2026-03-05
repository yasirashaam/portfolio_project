import sqlite3

conn = sqlite3.connect('database.db')

cur = conn.cursor()

cur.execute("""
CREATE TABLE contact(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT,
subject TEXT,
message TEXT
)
""")

conn.commit()
conn.close()