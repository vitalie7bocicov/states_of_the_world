import mysql.connector
from mysql.connector import Error

def create_server_connection():
    """
    Create a connection to the MySQL server.

    :returns: A MySQL connection object.
    :rtype: mysql.connector.connect
    :raises Error: If there is an error connecting to the MySQL server.
    """
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="statesdb"
        )
    except Error as err:
        print(f"Error in create_server_connection: '{err}'")

    return connection

def execute_insert(connection, query):
    """
    Execute an INSERT statement on the given connection.

    :param connection: A MySQL connection object.
    :type connection: mysql.connector.connect
    :param query: The INSERT statement to be executed.
    :type query: str
    :raises Error: If there is an error executing the INSERT statement.
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        cursor.close()
    except Error as err:
        print(f"Error at execute_insert: '{err}'")

def execute_select(connection, query):
    """
    Execute a SELECT statement on the given connection and return the result.

    :param connection: A MySQL connection object.
    :type connection: mysql.connector.connect
    :param query: The SELECT statement to be executed.
    :type query: str
    :returns: A list of tuples representing the rows returned by the SELECT statement.
    :rtype: list
    :raises Error: If there is an error executing the SELECT statement.
    """
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    except Error as err:
        print(f"Error at execute_select: '{err}'")

