import sqlite3

# Use 'with' to connect to the SQLite database
with sqlite3.connect('my_database.db') as connection:

    # Create a cursor object
    cursor = connection.cursor()

    # Write the SQL command to select all records from the Students table
    select_query = "SELECT * FROM Students;"

    # Execute the SQL command
    cursor.execute(select_query)

    # Fetch all records
    all_students = cursor.fetchall()

    # Display results in the terminal
    print("All Students:")
    for student in all_students:
        print(student)
