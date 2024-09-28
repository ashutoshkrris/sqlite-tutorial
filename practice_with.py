import sqlite3

# Step 1: Use 'with' to connect to the database (or create one) and automatically close it when done
with sqlite3.connect('my_database.db') as connection:

    # Step 2: Create a cursor object to interact with the database
    cursor = connection.cursor()

    print("Database created and connected successfully!")

# No need to call connection.close(); it's done automatically!
