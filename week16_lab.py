#!/usr/bin/env python
import sqlite3

db = sqlite3.connect('week16.db')

cursor = db.cursor()
cursor.execute(''' 
	CREATE TABLE movies( id INTEGER PRIMARY KEY, name TEXT, movie TEXT)
''')

inputName = raw_input("What is your name?")
inputMovie = raw_input("What is your favorite movie? ")

cursor.execute('''INSERT INTO movies(name, movie) VALUES(?,?)''', (inputName, inputMovie))
print('Added to database!')

db.commit()
db.close()