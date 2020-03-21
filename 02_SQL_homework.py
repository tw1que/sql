import sqlite3

with sqlite3.connect('new.db') as connection:

	c = connection.cursor()

	c.execute("""CREATE TABLE orders (make TEXT, model TEXT, order_date TEXT)""")

	orders = [
		('Ford', 'M001', '2020-01-01'),
		('Ford', 'M001', '2020-01-02'),
		('Ford', 'M001', '2020-01-03'),
		('Ford', 'M002', '2020-01-04'),
		('Ford', 'M002', '2020-01-05'),
		('Ford', 'M002', '2020-01-06'),
		('Ford', 'M003', '2020-01-07'),
		('Ford', 'M003', '2020-01-08'),
		('Ford', 'M003', '2020-01-09'),
		('Honda', 'M004', '2020-02-01'),
		('Honda', 'M004', '2020-02-02'),
		('Honda', 'M004', '2020-02-03'),
		('Honda', 'M005', '2020-02-04'),
		('Honda', 'M005', '2020-02-05'),
		('Honda', 'M005', '2020-02-06'),
	]

	c.executemany("""INSERT INTO orders (make, model, order_date) 
				VALUES (?, ?, ?)""", orders)

	c.execute("""SELECT cars.make, cars.model, cars.quantity, orders.order_date FROM cars 
				INNER JOIN orders ON cars.model = orders.model""")

	rows = c.fetchall()
	print(rows)
	for r in rows: 
		print(f"Make & Model: {r[0]} - {r[1]}")
		print(f"Quantity: {r[2]}")
		print(f"Order date(s):  {r[3]}")
