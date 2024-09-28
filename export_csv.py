import sqlite3
import csv


def export_to_csv(file_name):
    """Export data from the Customers table to a CSV file."""
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()

        # Execute a query to fetch all customer data
        cursor.execute("SELECT * FROM Customers;")
        customers = cursor.fetchall()

        # Write data to CSV
        with open(file_name, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['ID', 'Name', 'Balance'])  # Writing header
            csv_writer.writerows(customers)  # Writing data rows

        print(f"Data exported successfully to {file_name}.")


# Example usage
export_to_csv('customers.csv')
