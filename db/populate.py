from .db import *

def replace_NONE_with_NULL(data):
    for country in data:
        if data[country]==None:
            data[country] = "NULL"
    return data

def populate_states(countries,population,area,density,constitutional_form):
    connection = create_server_connection()
    population = replace_NONE_with_NULL(population)
    area = replace_NONE_with_NULL(area)
    density = replace_NONE_with_NULL(density)
    constitutional_form = replace_NONE_with_NULL(constitutional_form)
    for index,country in enumerate(countries):
        query = f"INSERT INTO states (ID,NAME,POPULATION,AREA,DENSITY,CONSTITUTIONAL_FORM) VALUES ({index}, '{country}', {population[country]}, {area[country]}, {density[country]}, '{constitutional_form[country]}')"
        execute_insert(connection,query)
    connection.close()
    print("States populated successfully!")

def populate_capitals(countries,capitals):
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
    print("Capitals populated successfully!")

def populate_neighbouring_countries(countries,neighbouring_countries):
    connection = create_server_connection()
    for index,country in enumerate(countries):
        if not neighbouring_countries[country]:
            continue
        for neighbour_country in neighbouring_countries[country]:
            query = f"INSERT INTO neighbouring_countries (ID1,ID2) VALUES ({index}, '{countries.index(neighbour_country)}')"
            execute_insert(connection,query)
    connection.close()
    print("Neighbouring countries populated successfully!")

def populate_time_zones(countries,time_zones):
    connection = create_server_connection()
    for index,country in enumerate(countries):
        if not time_zones[country]:
            continue
        for time_zone in time_zones[country]:
            query = f"INSERT INTO time_zones (ID,TIME_ZONE) VALUES ({index}, '{time_zone}')"
            execute_insert(connection,query)
    connection.close()
    print("Time zones populated successfully!")

def populate_languages(countries,languages,table_name):
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
