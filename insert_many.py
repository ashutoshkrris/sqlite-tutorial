from faker import Faker
import sqlite3

# Initialize Faker
fake = Faker(['en_IN'])

# Use 'with' to open and close the connection automatically
with sqlite3.connect('my_database.db') as connection:
    cursor = connection.cursor()

    # Insert a record into the Students table
    insert_query = '''
    INSERT INTO Students (name, age, email) 
    VALUES (?, ?, ?);
    '''
    students_data = [(fake.name(), fake.random_int(
        min=18, max=25), fake.email()) for _ in range(5)]

    # Execute the query for multiple records
    cursor.executemany(insert_query, students_data)

    # Commit the changes
    connection.commit()

    # Print confirmation message
    print("Fake student records inserted successfully!")
