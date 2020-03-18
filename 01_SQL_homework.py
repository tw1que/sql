import sqlite3

with sqlite3.connect("new.db") as connection:

	c = connection.cursor()

	#
	# INSERT assignment
	#

	# sample data for INSERT practice
	cars = [
		('Ford', 'M001', 1),
		('Ford', 'M002', 2),
		('Ford', 'M002', 3),
		('Honda', 'M001', 4),
		('Honda', 'M002', 4)
	]

	# execute INSERT sample data
	c.executemany("INSERT INTO cars (make, model, quantity) VALUES (?, ?, ?)", cars)

	# SELECT inserted data
	c.execute("SELECT * FROM cars")

	# print selected data
	rows = c.fetchall()
	print("\n INSERTED DATA: \n")
	for r in rows:
		print(r[0],r[1],r[2])

	#
	# UPDATE assignment
	#

	c.execute("UPDATE cars SET quantity = 3 WHERE make = 'Honda'")

	c.execute("SELECT * FROM cars")

	rows = c.fetchall()

	print("\n UPDATED DATA: \n")
	for r in rows:
		print(r[0],r[1],r[2])

	#
	# FILTER assignment
	#

	c.execute("SELECT * from cars WHERE make = 'Ford'")

	rows = c.fetchall()

	print("\n FILTERED DATA: \n")
	for r in rows:
		print(r[0],r[1],r[2])

		