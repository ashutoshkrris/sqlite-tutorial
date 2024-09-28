import sqlite3


def add_customer_with_error_handling(name, balance):
    """Add a new customer with error handling."""
    try:
        with sqlite3.connect('my_database.db') as connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO Customers (name, balance) VALUES (?, ?);", (name, balance))
            connection.commit()
            print(f"Added customer: {name} with balance: {balance}")

    except sqlite3.IntegrityError as e:
        print(f"Error: Integrity constraint violated - {e}")

    except sqlite3.OperationalError as e:
        print(f"Error: Operational issue - {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
add_customer_with_error_handling('Vishakha', 100.0)  # Valid
add_customer_with_error_handling('Vishakha', 150.0)  # Duplicate entry
