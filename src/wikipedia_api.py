from fastapi import FastAPI
from  db.queries import *
from db.queries import *
import uvicorn

app = FastAPI()
@app.get("/top_10_countries_by_population")
def top_10_by_population():
  """
  Get the top 10 countries by population.

  :returns: A string with the top 10 countries by population.
  :rtype: str
  """
  return get_top_10_by_property("POPULATION")

@app.get("/top_10_countries_by_area")
def top_10_by_area():
  """
  Get the top 10 countries by area.

  :returns: A string with the top 10 countries by area.
  :rtype: str
  """
  return get_top_10_by_property("AREA")

@app.get("/top_10_countries_by_density")
def top_10_by_density():
  """
  Get the top 10 countries by density.

  :returns: A string with the top 10 countries by density.
  :rtype: str
  """
  return get_top_10_by_property("DENSITY")

@app.get("/countries")
def countries(save=False):
  """
  Get a list of all countries.

  :param save: Whether to save the list of countries to a file.
  :type save: bool
  :return: A list of countries.
  :rtype: list[str]
  """
  return get_all_countries(save)
 
@app.get("/countries/capitals")
def countries_capitals():
  """
  Get the name and capital of all countries.

  :returns: A string with the name and capital of all countries.
  :rtype: str
  """
  return get_all_capitals()

@app.get("/countries/population")
def countries_by_population(order="DESC"):
  """
  Get all countries and their population.

  :param order: The order in which the countries should be returned.
  :type order: str
  :returns: A string with all countries and their population.
  :rtype: str
  """
  return get_all_by_property("POPULATION",order)

@app.get("/countries/area")
def countries_by_area(order="DESC"):
  """
  Get all countries and their area.

  :param order: The order in which the countries should be returned.
  :type order: str
  :returns: A string with all countries and their area.
  :rtype: str
  """
  return get_all_by_property("AREA",order)

@app.get("/countries/density")
def countries_by_density(order="DESC"):
  """
  Get all countries and their density.

  :param order: The order in which the countries should be returned.
  :type order: str
  :returns: A string with all countries and their density.
  :rtype: str
  """
  return get_all_by_property("DENSITY",order)

@app.get("/countries/constitutional_form")
def countries_by_constitutional_form(order="ASC"):
  """
  Get all countries and their constitutional form.

  :param order: The order in which the countries should be returned.
  :type order: str
  :returns: A string with all countries and their constitutional form.
  :rtype: str
  """
  return get_all_by_property("constitutional_form",order)

@app.get("/countries/neighbouring_countries")
def countries_by_neighbouring_countries():
  """
  Get all countries and their neighbouring countries.
  
  :returns: A string with all countries and their neighbouring countries.
  :rtype: str
  """
  return get_all_neighbouring_countries()

@app.get("/countries/languages/official")
def countries_by_official_languages():
  """
  Get all countries and their official languages.
  
  :returns: A string with all countries and their official languages.
  :rtype: str
  """
  return get_all_languages("official_languages")

@app.get("/countries/languages/national")
def countries_by_national_languages():
  """
  Get all countries and their national languages.
  
  :returns: A string with all countries and their national languages.
  :rtype: str
  """
  return get_all_languages("national_languages")

@app.get("/countries/languages/regional")
def countries_by_regional_languages():
  """
  Get all countries and their regional languages.

  :returns: A string with all countries and their regional languages.
  :rtype: str
  """
  return get_all_languages("regional_languages")

@app.get("/countries/languages/widely_spoken")
def countries_by_widely_spoken_languages():
  """
  Get all countries and their widely spoken languages.

  :returns: A string with all countries and their widely spoken languages.
  :rtype: str
  """
  return get_all_languages("widely_spoken_languages")

@app.get("/countries/languages/minority")
def countries_by_widely_spoken_languages():
  """
  Get all countries and their minority languages.

  :returns: A string with all countries and their minority languages.
  :rtype: str
  """
  return get_all_languages("minority_languages")

@app.get("/countries/time_zones")
def countries_by_time_zones():
  """
  Get all countries and their time zones.
  
  :returns: A string with all countries and their time zones.
  :rtype: str
  """
  return get_all_time_zones()

@app.get("/countries/time_zone/{time_zone}")
def countries_by_time_zone(time_zone):
  """
  Get all countries in the given time zone.

  :param time_zone: The time zone.
  :type time_zone: str
  :returns: A string with all countries in the given time zone.
  :rtype: str
  """
  return get_countries_by_time_zone(time_zone)

@app.get("/countries/language/official_languages/{language}")
def countries_by_official_language(language):
  """
  Get all countries with the given official language.
  
  :param language: The official language.
  :type language: str
  :returns: A string with all countries with the given official language.
  :rtype: str
  """
  return get_countries_by_language("official_languages",language)

@app.get("/countries/language/national_languages/{language}")
def countries_by_national_language(language):
  """
  Get all countries with the given national language.
  
  :param language: The national language.
  :type language: str
  :returns: A string with all countries with the given national language.
  :rtype: str
  """
  return get_countries_by_language("national_languages",language)

@app.get("/countries/language/regional_languages/{language}")
def countries_by_regional_language(language):
  """
  Get all countries with the given regional language.

  :param language: The regional language.
  :type language: str
  :returns: A string with all countries with the given regional language.
  :rtype: str
  """
  return get_countries_by_language("regional_languages",language)

@app.get("/countries/language/widely_spoken_languages/{language}")
def countries_by_widely_spoken_language(language):
  """
  Get all countries with the given widely spoken language.

  :param language: The widely spoken language.
  :type language: str
  :returns: A string with all countries with the given widely spoken language.
  :rtype: str
  """
  return get_countries_by_language("widely_spoken_languages",language)

@app.get("/countries/language/minority_languages/{language}")
def countries_by_minority_language(language):
  """
  Get all countries with the given minority language.

  :param language: The minority language.
  :type language: str
  :returns: A string with all countries with the given minority language.
  :rtype: str
  """
  return get_countries_by_language("minority_languages",language)

@app.get("/countries/constitutional_form/{constitutional_form}")
def countries_by_constitutional_form(constitutional_form):
  """
  Get all countries with the given constitutional form.

  :param constitutional_form: The constitutional form.
  :type constitutional_form: str
  :returns: A string with all countries with the given constitutional form.
  :rtype: str
  """
  return get_countries_by_constitutional_form(constitutional_form)

@app.get("/countries/capitals/more_than_1")
def countries_with_more_than_1_capital():
  """
  Get all countries with more than 1 capital.

  :returns: A string with all countries with more than 1 capital.
  :rtype: str
  """
  return get_countries_with_more_than_1_capital()

@app.get("/countries/{country}")
def country(country):
  """
  Get the properties of the given country.

  :param country: The name of the country.
  :type country: str
  :returns: A string with the properties of the given country.
  :rtype: str
  """
  return get_country(country)

if __name__ == "__main__":
  uvicorn.run("wikipedia_api:app", port=8000, log_level="info")