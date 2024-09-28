import sqlite3

# Use 'with' to open and close the connection automatically
with sqlite3.connect('my_database.db') as connection:
    cursor = connection.cursor()

    # Insert a record into the Students table
    insert_query = '''
    INSERT INTO Students (name, age, email) 
    VALUES (?, ?, ?);
    '''
    student_data = ('Jane Doe', 23, 'jane@example.com')

    cursor.execute(insert_query, student_data)

    # Commit the changes automatically
    connection.commit()

    # No need to call connection.close(); it's done automatically!
    print("Record inserted successfully!")
