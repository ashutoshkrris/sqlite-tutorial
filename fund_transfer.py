import sqlite3


def transfer_funds(from_customer, to_customer, amount):
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()

        try:
            # Start a transaction
            cursor.execute("BEGIN;")

            # Deduct amount from the sender
            cursor.execute(
                "UPDATE Customers SET balance = balance - ? WHERE name = ?;", (amount, from_customer))
            # Add amount to the receiver
            cursor.execute(
                "UPDATE Customers SET balance = balance + ? WHERE name = ?;", (amount, to_customer))

            # Commit the changes
            connection.commit()
            print(
                f"Transferred {amount} from {from_customer} to {to_customer}.")

        except Exception as e:
            # If an error occurs, rollback the transaction
            connection.rollback()
            print(f"Transaction failed: {e}")


# Example usage
transfer_funds('Ashutosh', 'Krishna', -80.0)
