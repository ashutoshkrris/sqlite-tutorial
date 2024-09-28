import csv
import sqlite3


def import_from_csv(file_name):
    """Import data from a CSV file into the Customers table."""
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()

        # Open the CSV file for reading
        with open(file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip the header row

            # Insert each row into the Customers table
            for row in csv_reader:
                cursor.execute(
                    "INSERT INTO Customers (name, balance) VALUES (?, ?);", (row[1], row[2]))

        connection.commit()
        print(f"Data imported successfully from {file_name}.")


# Example usage
import_from_csv('customer_data.csv')
