import json
import sqlite3


def export_to_json(file_name):
    """Export data from the Customers table to a JSON file."""
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()

        # Execute a query to fetch all customer data
        cursor.execute("SELECT * FROM Customers;")
        customers = cursor.fetchall()

        # Convert data to a list of dictionaries
        customers_list = [{'ID': customer[0], 'Name': customer[1],
                           'Balance': customer[2]} for customer in customers]

        # Write data to JSON
        with open(file_name, 'w') as json_file:
            json.dump(customers_list, json_file, indent=4)

        print(f"Data exported successfully to {file_name}.")


# Example usage
export_to_json('customers.json')
