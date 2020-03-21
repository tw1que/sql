import sqlite3

with sqlite3.connect('new.db') as connection:

	c = connection.cursor()

	#
	# Original
	#


	# c.execute("""SELECT population.city, population.population, 
	# 			regions.region FROM population, regions 
	# 			WHERE population.city = regions.city""")

	# rows = c.fetchall()

	# for r in rows:
	# 	print(r[0], r[1], r[2])

	#
	# Compact version
	#

	c.execute("""SELECT population.city, population.population, 
			regions.region FROM population, regions WHERE
			population.city = regions.city ORDER BY population.city""")

	rows = c.fetchall()
	print(rows)
	for r in rows:
		print('City: ' + r[0])
		print('Population: ' + str(r[1]))
		print('Region: ' + r[2])
		print("")


		print(f"{r}") 
