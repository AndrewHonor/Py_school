import sqlite3 as sq

with sq.connect("name_age.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS ppl
                        (name TEXT, 
                        age INTEGER)
                        """)

data = [{'name': 'Anton', 'age': 16},
        {'name': 'Oleg', 'age': 25},
        {'name': 'Alex', 'age': 16},
        {'name': 'Ivan', 'age': 27},
        {'name': 'Bogdan', 'age': 33},
        {'name': 'Taras', 'age': 18},
        ]
for bd_name in data:
    print(bd_name)