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

def get_all_time_zones():
    connection = create_server_connection()
    query = "SELECT states.NAME, time_zones.TIME_ZONE FROM states JOIN time_zones on states.ID=time_zones.ID;"
    response = f"NAME,TIME ZONES:\n"
    response += create_response(execute_select(connection,query))
    connection.close()
    return response

def get_country(country):
    connection = create_server_connection()
    query = f"SELECT NAME,POPULATION,AREA,DENSITY,CONSTITUTIONAL_FORM FROM states WHERE NAME='{country}'"
    response = f"NAME,POPULATION,AREA,DENSITY,CONSTITUTIONAL FORM:\n"
    response += create_response(execute_select(connection,query))
    connection.close()
    return response

def get_countries_by_time_zone(time_zone):
    connection = create_server_connection()
    query = f"SELECT states.NAME,time_zones.TIME_ZONE FROM states JOIN time_zones on states.ID=time_zones.ID WHERE time_zones.TIME_ZONE='{time_zone}'"
    response = f"NAME,TIME_ZONE:\n"
    response += create_response(execute_select(connection,query))
    connection.close()
    return response

def get_countries_by_language(table_name,language):
    connection = create_server_connection()
    query = f"SELECT states.NAME, {table_name}.LANGUAGE FROM states JOIN {table_name} on states.ID={table_name}.ID WHERE {table_name}.LANGUAGE='{language}'"
    response = f"NAME,{table_name.upper()}:\n"
    response += create_response(execute_select(connection,query))
    connection.close()
    return response

def get_countries_by_constitutional_form(constitutional_form):
    connection = create_server_connection()
    query = f"SELECT NAME,CONSTITUTIONAL_FORM FROM states WHERE CONSTITUTIONAL_FORM='{constitutional_form}'"
    response = f"NAME,CONSTITUTIONAL_FORM:\n"
    response += create_response(execute_select(connection,query))
    connection.close()
    return response

def get_countries_with_more_than_1_capital():
    connection = create_server_connection()
    query = "SELECT states.NAME,capitals.NAME FROM states JOIN capitals ON capitals.ID=states.ID where states.ID IN (SELECT capitals.ID FROM capitals group by capitals.ID  HAVING COUNT(capitals.ID)>1);"
    response = f"NAME,CAPITAL: (Countries with more than 1 capital)\n"
    response += create_response(execute_select(connection,query))
    connection.close()
    return response
