import sqlite3

with sqlite3.connect('new.db') as connection:

	c = connection.cursor()
	try:

		c.execute("INSERT INTO populations VALUES ('New York City', \
		'NY', 8400000)")

		c.execute("INSERT INTO populations VALUES ('San Fransisco', \
		'CA', 800000)")
	

	except sqlite3.OperationalError:

		print("Oops! Something went wrong. Try again...")