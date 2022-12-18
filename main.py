from crawler.crawler import crawl
from db.db import *
from db.populate_db import *
from wikipedia_api import *

def populate_db(countries, capitals, population, 
                area, density, neighbouring_countries, 
                time_zones, constitutional_form, official_languages,
                regional_languages, minority_languages, national_languages, 
                widely_spoken_languages):
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
     # populate_db(*crawl())
     pass