from .db import *
from .hepers import *

def get_top_10_by_property(column):
    """
    Get the top 10 countries by the given property.

    :param column: The name of the property to be used for ranking.
    :type column: str
    :returns: A string with the top 10 countries by the given property.
    :rtype: str
    :raises Error: If there is an error executing the SELECT query.
    """
    connection = create_server_connection()
    query = f"SELECT NAME,{column} FROM states ORDER BY {column} DESC LIMIT 10"
    response = f"Top 10 countries by {column}:\n"
    response += create_response(execute_select(connection,query))
    connection.close()
    return response

def get_all_countries(save):
    """
    Get a list of all countries from the 'states' table.

    :param save: Whether to save the list of countries to a file.
    :type save: bool
    :returns: A string with the name, population, area, density and constitutional form of all countries.
    :rtype: str
    :raises Error: If there is an error executing the SELECT query.
    """
    connection = create_server_connection()
    query = "SELECT NAME,POPULATION,AREA,DENSITY,CONSTITUTIONAL_FORM FROM states"
    response = f"NAME,POPULATION,AREA,DENSITY,CONSTITUTIONAL FORM:\n"
    response += create_response(execute_select(connection,query))
    connection.close()
    if save:
        save_to_file("countries",response)
    return response

def get_all_capitals():
    """
    Get the name and capital of all countries from the 'states' and 'capitals' tables.

    :returns: A string with the name and capitals of all countries.
    :rtype: str
    :raises Error: If there is an error executing the SELECT query.
    """
    connection = create_server_connection()
    query = "SELECT states.NAME,capitals.NAME FROM states JOIN capitals on states.ID=capitals.ID;"
    query_result = execute_select(connection,query)
    result = format_query_result(query_result)
    response = f"NAME,CAPITAL:\n"
    response += create_response(result)
    connection.close()
    return response

def get_all_by_property(property,order):
    """
    Get the name and value of a property for all countries from the 'states' table, sorted in the specified order.

    :param property: The name of the property to be retrieved.
    :type property: str
    :param order: The order in which the results should be sorted. Either 'ASC' for ascending or 'DESC' for descending.
    :type order: str
    :returns: A string with the name and value of the specified property for all countries, sorted in the specified order.
    :rtype: str
    :raises Error: If there is an error executing the SELECT query.
    """
    connection = create_server_connection()
    query = f"SELECT NAME,{property} FROM states  ORDER BY {property} {order};"
    response = f"NAME,{property}:\n"
    response += create_response(execute_select(connection,query))
    connection.close()
    return response

def get_all_neighbouring_countries():
    """
    Get the name and neighbouring countries of all countries from the 'states' and 'neighbouring_countries' tables.

    :returns: A string with the name and neighbouring countries of all countries.
    :rtype: str
    :raises Error: If there is an error executing the SELECT query.
    """
    connection = create_server_connection()
    query = "SELECT states.NAME, (select states.NAME from states where ID=neighbouring_countries.ID2) from states JOIN neighbouring_countries ON neighbouring_countries.ID1=states.ID;"
    query_result = format_query_result(execute_select(connection,query))
    response = f"NAME,NEIGHBOURING COUNTRIES:\n"
    response += create_response(query_result)
    connection.close()
    return response

def get_all_languages(table):
    """
    Get the name and language of all countries from the 'states' and the given table.

    :param table: The name of the table to be used for retrieving the language.
    :type table: str
    :returns: A string with the name and language of all countries.
    :rtype: str
    :raises Error: If there is an error executing the SELECT query.
    """
    connection = create_server_connection()
    query = f"SELECT states.NAME, {table}.LANGUAGE FROM states JOIN {table} on states.ID={table}.ID;"
    query_result = format_query_result(execute_select(connection,query))
    response = f"NAME,{table.upper()}:\n"
    response += create_response(query_result)
    connection.close()
    return response

def get_all_time_zones():
    """
    Get the name and time zone of all countries from the 'states' and 'time_zones' tables.

    :returns: A string with the name and time zone of all countries.
    :rtype: str
    :raises Error: If there is an error executing the SELECT query.
    """
    connection = create_server_connection()
    query = "SELECT states.NAME, time_zones.TIME_ZONE FROM states JOIN time_zones on states.ID=time_zones.ID;"
    query_result = format_query_result(execute_select(connection,query))
    response = f"NAME,TIME ZONES:\n"
    response += create_response(query_result)
    connection.close()
    return response

def get_country(country):
    """
    Get the properties of the given country from the 'states' table.

    :param country: The name of the country to be retrieved.
    :type country: str
    :returns: A string with the properties of the given country.
    :rtype: str
    :raises Error: If there is an error executing the SELECT query.
    """
    connection = create_server_connection()
    query = f"SELECT NAME,POPULATION,AREA,DENSITY,CONSTITUTIONAL_FORM FROM states WHERE NAME='{country}'"
    response = f"NAME,POPULATION,AREA,DENSITY,CONSTITUTIONAL FORM:\n"
    response += create_response(execute_select(connection,query))
    connection.close()
    return response

def get_countries_by_time_zone(time_zone):
    """
    Get the name and time zone of all countries from the 'states' and 'time_zones' tables that have the given time zone.

    :param time_zone: The time zone to be used for filtering.
    :type time_zone: str
    :returns: A string with the name and time zone of all countries that have the given time zone.
    :rtype: str
    :raises Error: If there is an error executing the SELECT query.
    """
    connection = create_server_connection()
    query = f"SELECT states.NAME,time_zones.TIME_ZONE FROM states JOIN time_zones on states.ID=time_zones.ID WHERE time_zones.TIME_ZONE='{time_zone}'"
    response = f"NAME,TIME_ZONE:\n"
    response += create_response(execute_select(connection,query))
    connection.close()
    return response

def get_countries_by_language(table_name,language):
    """
    Get the name and language of all countries from the 'states' and the given table that have the given language.

    :param table_name: The name of the table to be used for retrieving the language.
    :type table_name: str
    :param language: The language to be used for filtering.
    :type language: str
    :returns: A string with the name and language of all countries that have the given language.
    :rtype: str
    :raises Error: If there is an error executing the SELECT query.
    """
    connection = create_server_connection()
    query = f"SELECT states.NAME, {table_name}.LANGUAGE FROM states JOIN {table_name} on states.ID={table_name}.ID WHERE {table_name}.LANGUAGE='{language}'"
    response = f"NAME,{table_name.upper()}:\n"
    response += create_response(execute_select(connection,query))
    connection.close()
    return response

def get_countries_by_constitutional_form(constitutional_form):
    """
    Get the name and constitutional form of all countries from the 'states' table that have the given constitutional form.

    :param constitutional_form: The constitutional form to be used for filtering.
    :type constitutional_form: str
    :returns: A string with the name and constitutional form of all countries that have the given constitutional form.
    :rtype: str
    :raises Error: If there is an error executing the SELECT query.
    """
    connection = create_server_connection()
    query = f"SELECT NAME,CONSTITUTIONAL_FORM FROM states WHERE CONSTITUTIONAL_FORM='{constitutional_form}'"
    response = f"NAME,CONSTITUTIONAL_FORM:\n"
    response += create_response(execute_select(connection,query))
    connection.close()
    return response

def get_countries_with_more_than_1_capital():
    """
    Get the name and capital of all countries from the 'states' and 'capitals' tables that have more than 1 capital.

    :returns: A string with the name and capital of all countries that have more than 1 capital.
    :rtype: str
    :raises Error: If there is an error executing the SELECT query.
    """
    connection = create_server_connection()
    query = "SELECT states.NAME,capitals.NAME FROM states JOIN capitals ON capitals.ID=states.ID where states.ID IN (SELECT capitals.ID FROM capitals group by capitals.ID  HAVING COUNT(capitals.ID)>1);"
    query_result = format_query_result(execute_select(connection,query))
    response = f"NAME,CAPITAL: (Countries with more than 1 capital)\n"
    response += create_response(query_result)
    connection.close()
    return response
