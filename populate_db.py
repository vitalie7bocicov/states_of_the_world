from crawler.crawler import crawl
from db.db import *
from db.populate import *
from wikipedia_api import *

def populate_db(countries, capitals, population, 
                area, density, neighbouring_countries, 
                time_zones, constitutional_form, official_languages,
                regional_languages, minority_languages, national_languages, 
                widely_spoken_languages):
    """
    Populate the MySQL database with data from the given dictionaries.

    :param countries: A list of countries.
    :type countries: list
    :param capitals: A dictionary with keys representing countries and values representing lists of capital cities.
    :type capitals: dict
    :param population: A dictionary with keys representing countries and values representing population data.
    :type population: dict
    :param area: A dictionary with keys representing countries and values representing area data.
    :type area: dict
    :param density: A dictionary with keys representing countries and values representing density data.
    :type density: dict
    :param neighbouring_countries: A dictionary with keys representing countries and values representing lists of neighbouring countries.
    :type neighbouring_countries: dict
    :param time_zones: A dictionary with keys representing countries and values representing lists of time zones.
    :type time_zones: dict
    :param constitutional_form: A dictionary with keys representing countries and values representing constitutional form data.
    :type constitutional_form: dict
    :param official_languages: A dictionary with keys representing countries and values representing lists of official languages.
    :type official_languages: dict
    :param regional_languages: A dictionary with keys representing countries and values representing lists of regional languages.
    :type regional_languages: dict
    :param minority_languages: A dictionary with keys representing countries and values representing lists of minority languages.
    :type minority_languages: dict
    :param national_languages: A dictionary with keys representing countries and values representing lists of national languages.
    :type national_languages: dict
    :param widely_spoken_languages: A dictionary with keys representing countries and values representing lists of widely spoken languages.
    :type widely_spoken_languages: dict
    :raises Error: If there is an error inserting data into the database.
    """
    populate_states(countries, population, area, density, constitutional_form)
    populate_capitals(countries, capitals)
    populate_neighbouring_countries(countries, neighbouring_countries)
    populate_time_zones(countries, time_zones)
    populate_languages(countries, official_languages, "official_languages")
    populate_languages(countries, regional_languages, "regional_languages")
    populate_languages(countries, minority_languages, "minority_languages")
    populate_languages(countries, national_languages, "national_languages")
    populate_languages(countries, widely_spoken_languages, "widely_spoken_languages")
   
if __name__ == "__main__":
     populate_db(*crawl())