import mysql.connector
from mysql.connector import Error

def create_server_connection():
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
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        cursor.close()
    except Error as err:
        print(f"Error at execute_insert: '{err}'")

def execute_select(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    except Error as err:
        print(f"Error at execute_select: '{err}'")

