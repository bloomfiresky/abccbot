import sqlite3
import os

db_name = "def.db"

if db_name in os.listdir():
    print("removing the user_base.db and creating a fresh copy of it")
    os.system("rm def.db")

print("Creating the database")
conn = sqlite3.connect(db_name)
cur = conn.cursor()

user_table = "CREATE TABLE users(name TEXT,email TEXT,password TEXT)"

new_users = (
    ('datta','admin@gmail.com','banking'),
    ('dattasai','fork@gmail.com','digital')
)

cur.execute(user_table)
print("table created")
cur.executemany('INSERT INTO users VALUES(?, ?, ?)', new_users)
conn.commit()
print("default users created \n\ndisplaying them")

cur.execute('SELECT * FROM users')
print(cur.fetchall())
