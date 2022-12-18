from crawler import crawl
from db import *


def populate_db(countries, capitals, population, 
                area, density, neigbouring_countries, 
                time_zones, constitutional_form, official_languages,
                regional_languages, minority_languages, national_languages, 
                widely_spoken_languages):
    # populate_states(countries, population, area, density, constitutional_form)
    # populate_capitals(countries, capitals)
    # populate_neigbouring_countries(countries, neigbouring_countries)
    pass
        
   
if __name__ == "__main__":
     populate_db(*crawl())
    