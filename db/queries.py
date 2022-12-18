from .db import *

def get_top_10_by_property(column):
    connection = create_server_connection()
    query = f"SELECT NAME,{column} FROM states ORDER BY {column} DESC LIMIT 10"
    response = f"Top 10 countries by {column}:\n"
    for result in execute_select(connection,query):
        response += f"{result[0]}: {result[1]}\n"
    connection.close()
    return response
