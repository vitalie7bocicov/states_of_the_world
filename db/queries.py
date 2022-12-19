from .db import *

def create_response(query_result):
    response = ""
    for result in query_result:
        for index,value in enumerate(result):
            response += f"{value}"
            if index < len(result) - 1:
                response += ","
            else:
                response += "\n"
    return response


def get_top_10_by_property(column):
    connection = create_server_connection()
    query = f"SELECT NAME,{column} FROM states ORDER BY {column} DESC LIMIT 10"
    response = f"Top 10 countries by {column}:\n"
    response += create_response(execute_select(connection,query))
    connection.close()
    return response

def get_all_countries():
    connection = create_server_connection()
    query = "SELECT NAME,POPULATION,AREA,DENSITY,CONSTITUTIONAL_FORM FROM states"
    response = f"NAME,POPULATION,AREA,DENSITY,CONSITUTIONAL FORM:\n"
    response += create_response(execute_select(connection,query))
    connection.close()
    return response

def get_all_capitals():
    connection = create_server_connection()
    query = "SELECT states.NAME,capitals.NAME FROM states JOIN capitals on states.ID=capitals.ID;"
    response = f"NAME,CAPITAL:\n"
    response += create_response(execute_select(connection,query))
    connection.close()
    return response

def get_all_by_property(property,order):
    connection = create_server_connection()
    query = f"SELECT NAME,{property} FROM states  ORDER BY {property} {order};"
    response = f"NAME,{property}:\n"
    response += create_response(execute_select(connection,query))
    connection.close()
    return response

def get_all_neighbouring_countries():
    connection = create_server_connection()
    query = "SELECT states.NAME, (select states.NAME from states where ID=neighbouring_countries.ID2) from states JOIN neighbouring_countries ON neighbouring_countries.ID1=states.ID;"
    response = f"NAME,NEIGHBOURING COUNTRIES:\n"
    response += create_response(execute_select(connection,query))
    connection.close()
    return response

def get_all_languages(table):
    connection = create_server_connection()
    query = f"SELECT states.NAME, {table}.LANGUAGE FROM states JOIN {table} on states.ID={table}.ID;"
    response = f"NAME,{table.upper()}:\n"
    response += create_response(execute_select(connection,query))
    connection.close()
    return response