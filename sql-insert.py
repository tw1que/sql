import sqlite3
import random

with sqlite3.connect('newnum.db') as connection:

	c = connection.cursor()

	# create a connection to "newnum.db"
	c.execute("""DROP TABLE IF EXISTS random_integers""")
	c.execute("""CREATE TABLE random_integers (random_integers INT)""")

	# generate a list of 100 random integers ranging from 0 to 100
	random_integer_list = [(random.randrange(0,101, 1), ) for iter in range(100)]
	
	# print(random_integer_list)
	# insert the list with 100 random integers into "newnum.db"
	# c.executemany("""INSERT INTO random_integers (random_integers) VALUES (?)""", random_integer_list )
	c.execute("""INSERT INTO random_integers (random_integers) VALUES (?)""", (random.randint(0,100), ) )

