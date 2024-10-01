import sqlite3
from faker import Faker

# Initialize the Faker library
fake = Faker(['en_IN'])


def insert_fake_students(num_records):
    """Generate and insert fake student data into the Students table."""
    fake_data = [(fake.name(), fake.random_int(min=18, max=25),
                  fake.email()) for _ in range(num_records)]

    # Use 'with' to handle the database connection
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()

        # Insert fake data into the Students table
        cursor.executemany('''
        INSERT INTO Students (name, age, email) 
        VALUES (?, ?, ?);
        ''', fake_data)

        connection.commit()

    print(f"{num_records} fake student records inserted successfully.")


# Insert 10,000 fake records into the Students table
insert_fake_students(10000)
