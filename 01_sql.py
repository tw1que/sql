# Create a SQLite3 database and table


# Import the sqlite3 library
import sqlite3

# Create a new database if the database doesn't already exist
conn = sqlite3.connect('new.db')

# Get a cursor object used to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE population 
	(city TEXT, state TEXT, population INT)
	''')

# Close the database connection
conn.close()