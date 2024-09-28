import sqlite3
import pandas as pd

# Use 'with' to connect to the SQLite database
with sqlite3.connect('my_database.db') as connection:
    # Write the SQL command to select all records from the Students table
    select_query = "SELECT * FROM Students;"

    # Use pandas to read SQL query directly into a DataFrame
    df = pd.read_sql_query(select_query, connection)

# Display the DataFrame
print("All Students as DataFrame:")
print(df)
