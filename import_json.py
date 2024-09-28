import json
import sqlite3


def import_from_json(file_name):
    """Import data from a JSON file into the Customers table."""
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()

        # Open the JSON file for reading
        with open(file_name, 'r') as json_file:
            customers_list = json.load(json_file)

            # Insert each customer into the Customers table
            for customer in customers_list:
                cursor.execute("INSERT INTO Customers (name, balance) VALUES (?, ?);", (customer['Name'], customer['Balance']))

        connection.commit()
        print(f"Data imported successfully from {file_name}.")


# Example usage
import_from_json('customer_data.json')
