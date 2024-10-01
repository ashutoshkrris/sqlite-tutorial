import sqlite3


def explain_query(search_name):
    """Explain the query execution plan for a SELECT query without an index."""

    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()

        # Use EXPLAIN QUERY PLAN to analyze how the query is executed
        cursor.execute('''
        EXPLAIN QUERY PLAN
        SELECT * FROM Students WHERE name = ?;
        ''', (search_name,))

        # Fetch and display the query plan
        query_plan = cursor.fetchall()

        print("Query Plan:")
        for step in query_plan:
            print(step)


# Example: Analyzing the query plan for searching by name
explain_query('Ojasvi Dhawan')
