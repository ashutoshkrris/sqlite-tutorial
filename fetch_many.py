import sqlite3

# Use 'with' to connect to the SQLite database
with sqlite3.connect('my_database.db') as connection:

    # Create a cursor object
    cursor = connection.cursor()

    # Write the SQL command to select all records from the Students table
    select_query = "SELECT * FROM Students;"

    # Execute the SQL command
    cursor.execute(select_query)

    # Fetch three records
    three_students = cursor.fetchmany(3)

    # Display results
    print("Three Students:")
    for student in three_students:
        print(student)
