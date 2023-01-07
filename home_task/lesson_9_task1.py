import sqlite3 as sq

users = [{'name': 'Anton', 'age': 16},
         {'name': 'Oleg', 'age': 25},
         {'name': 'Alex', 'age': 16},
         {'name': 'Ivan', 'age': 27},
         {'name': 'Bogdan', 'age': 33},
         {'name': 'Taras', 'age': 18},
         ]
lst_name_min_age = []
lst_name_long_len = []
middle_age = 0
with sq.connect("name_age.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS ppl
                        (name TEXT, 
                        age INTEGER)
                        """)
    con.commit()
    for i in users:
        user = list(i.values())
        cur.execute(
            """
            INSERT INTO ppl (name,age) VALUES (?,?);
            """,
            user
        )
        con.commit()
cur.execute("""
            SELECT name FROM ppl WHERE age = (SELECT MIN(age) FROM ppl)
            """)

for name in cur.fetchall():
    lst_name_min_age.append(*name)
print('Самі молоді: ', *lst_name_min_age)

cur.execute("""
            SELECT name FROM ppl ORDER BY LENGTH(name) DESC LIMIT 1 
            """)
for name in cur.fetchall():
    lst_name_long_len.append(*name)
print("Найдовше ім'я: ", *lst_name_long_len)
cur.execute("""
            SELECT AVG(age) FROM ppl
            """)
middle_age = cur.fetchone()
print("Середній вік: ", *middle_age)
cur.execute("""DELETE from ppl""", )
con.commit()
cur.close()
