from .db import *

def replace_None_with_NULL(data):
    """
    Replace all occurrences of `None` in the given dictionary with the string 'NULL'.

    :param data: A dictionary with keys representing countries and values representing data.
    :type data: dict
    :returns: The updated dictionary.
    :rtype: dict
    """
    for country in data:
        if data[country]==None:
            data[country] = "NULL"
    return data

def populate_states(countries,population,area,density,constitutional_form):
    """
    Populate the 'states' table in the MySQL database with data from the given dictionaries.

    :param countries: A list of countries.
    :type countries: list
    :param population: A dictionary with keys representing countries and values representing population data.
    :type population: dict
    :param area: A dictionary with keys representing countries and values representing area data.
    :type area: dict
    :param density: A dictionary with keys representing countries and values representing density data.
    :type density: dict
    :param constitutional_form: A dictionary with keys representing countries and values representing constitutional form data.
    :type constitutional_form: dict
    :raises Error: If there is an error inserting data into the 'states' table.
    """
    connection = create_server_connection()
    population = replace_None_with_NULL(population)
    area = replace_None_with_NULL(area)
    density = replace_None_with_NULL(density)
    constitutional_form = replace_None_with_NULL(constitutional_form)
    for index,country in enumerate(countries):
        query = f"INSERT INTO states (ID,NAME,POPULATION,AREA,DENSITY,CONSTITUTIONAL_FORM) VALUES ({index}, '{country}', {population[country]}, {area[country]}, {density[country]}, '{constitutional_form[country]}')"
        execute_insert(connection,query)
    connection.close()
    print("states populated successfully!")

def populate_capitals(countries,capitals):
    """
    Populate the 'capitals' table in the MySQL database with data from the given dictionary.

    :param countries: A list of countries.
    :type countries: list
    :param capitals: A dictionary with keys representing countries and values representing lists of capital cities.
    :type capitals: dict
    :raises Error: If there is an error inserting data into the 'capitals' table.
    """
    connection = create_server_connection()
    for index,country in enumerate(countries):
        for capital in capitals[country]:
            if capital==None:
                capital = "NULL"
            if capital.find("'")!=-1:
               capital = capital.replace("'","\\'")
            query = f"INSERT INTO capitals (ID,NAME) VALUES ({index}, '{capital}')"
            execute_insert(connection,query)
    connection.close()
    print("capitals populated successfully!")

def populate_neighbouring_countries(countries,neighbouring_countries):
    """
    Populate the 'neighbouring_countries' table in the MySQL database with data from the given dictionary.

    :param countries: A list of countries.
    :type countries: list
    :param neighbouring_countries: A dictionary with keys representing countries and values representing lists of neighbouring countries.
    :type neighbouring_countries: dict
    :raises Error: If there is an error inserting data into the 'neighbouring_countries' table.
    """
    connection = create_server_connection()
    for index,country in enumerate(countries):
        if not neighbouring_countries[country]:
            continue
        for neighbour_country in neighbouring_countries[country]:
            query = f"INSERT INTO neighbouring_countries (ID1,ID2) VALUES ({index}, '{countries.index(neighbour_country)}')"
            execute_insert(connection,query)
    connection.close()
    print("neighbouring_countries populated successfully!")

def populate_time_zones(countries,time_zones):
    """
    Populate the 'time_zones' table in the MySQL database with data from the given dictionary.

    :param countries: A list of countries.
    :type countries: list
    :param time_zones: A dictionary with keys representing countries and values representing lists of time zones.
    :type time_zones: dict
    :raises Error: If there is an error inserting data into the 'time_zones' table.
    """
    connection = create_server_connection()
    for index,country in enumerate(countries):
        if not time_zones[country]:
            continue
        for time_zone in time_zones[country]:
            query = f"INSERT INTO time_zones (ID,TIME_ZONE) VALUES ({index}, '{time_zone}')"
            execute_insert(connection,query)
    connection.close()
    print("time_zones populated successfully!")

def populate_languages(countries,languages,table_name):
    """
    Populate the given table in the MySQL database with data from the given dictionary.

    :param countries: A list of countries.
    :type countries: list
    :param languages: A dictionary with keys representing countries and values representing lists of languages.
    :type languages: dict
    :param table_name: The name of the table to be populated.
    :type table_name: str
    :raises Error: If there is an error inserting data into the given table.
    """
    connection = create_server_connection()
    for index,country in enumerate(countries):
        if not languages[country]:
            continue
        for language in languages[country]:
            if language.find("'")!=-1:
                language = language.replace("'","\\'")
            query = f"INSERT INTO {table_name} (ID,LANGUAGE) VALUES ({index}, '{language}')"
            execute_insert(connection,query)
    connection.close()
    print(f"{table_name} populated successfully!")
