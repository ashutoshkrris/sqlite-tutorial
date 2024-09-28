import sqlite3

# Create the Customers table and add two customers
with sqlite3.connect('my_database.db') as connection:
    cursor = connection.cursor()

    # Create Customers table
    create_customers_table = '''
    CREATE TABLE IF NOT EXISTS Customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        balance REAL NOT NULL
    );
    '''
    cursor.execute(create_customers_table)

    # Insert two customers
    cursor.execute(
        "INSERT INTO Customers (name, balance) VALUES (?, ?);", ('Ashutosh', 100.0))
    cursor.execute(
        "INSERT INTO Customers (name, balance) VALUES (?, ?);", ('Krishna', 50.0))

    connection.commit()
