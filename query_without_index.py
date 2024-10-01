import sqlite3
import time


def query_without_index(search_name):
    """Query the Students table by name without an index and measure the time taken."""

    # Connect to the database using 'with'
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()

        # Measure the start time
        start_time = time.perf_counter_ns()

        # Perform a SELECT query to find a student by name
        cursor.execute('''
        SELECT * FROM Students WHERE name = ?;
        ''', (search_name,))

        # Fetch all results (there should be only one or a few in practice)
        results = cursor.fetchall()

        # Measure the end time
        end_time = time.perf_counter_ns()

        # Calculate the total time taken
        elapsed_time = (end_time - start_time) / 1000

        # Display the results and the time taken
        print(f"Query completed in {elapsed_time:.5f} microseconds.")
        print("Results:", results)


# Example: Searching for a student by name
query_without_index('Ojasvi Dhawan')
