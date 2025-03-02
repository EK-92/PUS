import sqlite3

connection = sqlite3.connect("../../links.db")
cursor = connection.cursor()

connection.execute('''CREATE TABLE IF NOT EXISTS links(
ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
HASH TEXT, 
URL TEXT);''')
connection.commit()
