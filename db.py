import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="statesdb"
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def execute_query(connection, query,country):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        cursor.close()
    except Error as err:
        print(f"Error at country {country}: '{err}'")

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
        execute_query(connection,query,country)
    connection.close()

def populate_capitals(countries,capitals):
    connection = create_server_connection()
    for index,country in enumerate(countries):
        if capitals[country]==None:
            capitals[country] = "NULL"
        if capitals[country].find("'")!=-1:
            capitals[country] = capitals[country].replace("'","\\'")
        query = f"INSERT INTO capitals (ID,NAME) VALUES ({index}, '{capitals[country]}')"
        execute_query(connection,query,country)
    connection.close()

def populate_neighbouring_countries(countries,neighbouring_countries):
    connection = create_server_connection()
    for index,country in enumerate(countries):
        if neighbouring_countries[country]==None:
            neighbouring_countries[country] = "NULL"
        query = f"INSERT INTO neighbouring_countries (ID1,ID2) VALUES ({index}, '{countries}')"
        execute_query(connection,query,country)