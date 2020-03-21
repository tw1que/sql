import sqlite3

with sqlite3.connect('new.db') as connection:

	c = connection.cursor()

	c.execute("""SELECT * FROM cars""")

	cars = c.fetchall()

	for car in cars:

		print(f"{car[0]} - {car[1]}")
		print(f"{car[2]}")

		c.execute("""SELECT count(order_date) FROM orders WHERE make = ? AND model = ?""", (car[0], car[1]))

		order_count = c.fetchone()

		print(f"{order_count[0]}")

		c.execute("""SELECT cars.make, cars.model, cars.quantity, count(orders.make) FROM cars, orders WHERE
					cars.make = orders.make AND cars.model = orders.model""")

	# c.execute("SELECT * FROM cars")

	# rows = c.fetchall()

	# for r in rows:

	# 	print(r[0], r[1], "\n", r[2])

	# 	c.execute("SELECT count(order_date) FROM orders WHERE make=? AND model=?", 
	# 		(r[0], r[1]))

	# 	order_count = c.fetchone()[0]

	# 	print(order_count)