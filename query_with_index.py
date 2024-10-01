import sqlite3
import time


def query_with_index(student_name):
    """Query the Students table using an index on the name column."""
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()

        # SQL command to select a student by name
        select_query = 'SELECT * FROM Students WHERE name = ?;'

        # Measure the execution time
        start_time = time.perf_counter_ns()  # Start the timer

        # Execute the query with the provided student name
        cursor.execute(select_query, (student_name,))
        result = cursor.fetchall()  # Fetch all results

        end_time = time.perf_counter_ns()  # End the timer

        # Calculate the elapsed time in microseconds
        execution_time = (end_time - start_time) / 1000

        # Display results and execution time
        print(f"Query result: {result}")
        print(f"Execution time with index: {execution_time:.5f} microseconds")


# Example: Searching for a student by name
query_with_index('Ojasvi Dhawan')
