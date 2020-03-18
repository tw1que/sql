# Training for UPDATE and DELETE statements

import sqlite3

with sqlite3.connect('new.db') as connection:

	c = connection.cursor()

	try:
		c.execute("UPDATE population SET population = 9000000 WHERE city = 'New York City'")

	except sqlite3.OperationalError as e:
		print(e)

	try:
		c.execute("DELETE FROM population WHERE city='Boston'")

	except sqlite3.OperationalError as e:
		print(e)

	print("\n NEW DATA: \n")

	try:
		c.execute("SELECT * FROM population")

		rows = c.fetchall()

		for r in rows:

			print(r[0], r[1], r[2])

	except sqlite3.OperationalError:
		print("Oops! Something went wrong.")

