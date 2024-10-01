import sqlite3
import time


def create_index():
    """Create an index on the name column of the Students table."""
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()

        # SQL command to create an index on the name column
        create_index_query = '''
        CREATE INDEX IF NOT EXISTS idx_name ON Students (name);
        '''

        # Measure the start time
        start_time = time.perf_counter_ns()

        # Execute the SQL command to create the index
        cursor.execute(create_index_query)

        # Measure the start time
        end_time = time.perf_counter_ns()

        # Commit the changes
        connection.commit()

        print("Index on 'name' column created successfully!")
        
        # Calculate the total time taken
        elapsed_time = (end_time - start_time) / 1000

        # Display the results and the time taken
        print(f"Query completed in {elapsed_time:.5f} microseconds.")


# Call the function to create the index
create_index()
