import sqlite3

# Step 1: Connect to a database (or create one)
connection = sqlite3.connect('my_database.db')

# Step 2: Create a cursor object to interact with the database
cursor = connection.cursor()

print("Database created and connected successfully!")

# Step 4: Close the connection when done
connection.close()
