# handlers/get_users.py

from flask import jsonify
from app import mysql

def get_data():
    # Perform a query to fetch data from your database
    connection = mysql.connect()
    cursor = connection.cursor()

    try:
        query = "SELECT * FROM users;"
        cursor.execute(query)
        data = cursor.fetchall()
    except Exception as e:
        # Handle any exceptions that may occur during the query
        print("Error:", str(e))
        data = []
    finally:
        # Close the cursor and connection in the 'finally' block to ensure cleanup
        cursor.close()
        connection.close()

    # Process and return the data as JSON
    return jsonify(data)
