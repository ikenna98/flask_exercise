import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO animes (name, year) VALUES (?, ?)",
            ('Bubble', 2022)
            )

cur.execute("INSERT INTO animes (name, year) VALUES (?, ?)",
            ('Blackover', 2017)
            )

cur.execute("INSERT INTO animes (name, year) VALUES (?, ?)",
            ('Blue Period', 2021)
            )

connection.commit()
connection.close()
