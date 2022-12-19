from fastapi import FastAPI
from  db.queries import *
from db.queries import *
app = FastAPI()

@app.get("/top_10_countries_by_population")
def top_10_by_population():
  return get_top_10_by_property("POPULATION")

@app.get("/top_10_countries_by_area")
def top_10_by_area():
  return get_top_10_by_property("AREA")

@app.get("/top_10_countries_by_density")
def top_10_by_density():
  return get_top_10_by_property("DENSITY")

@app.get("/countries")
def countries():
  return get_all_countries()

@app.get("/countries/{country}")
def country(country):
  return get_country(country)

@app.get("/countries/capitals")
def countries_capitals():
  return get_all_capitals()

@app.get("/countries/population")
def countries_by_population(order="DESC"):
  return get_all_by_property("POPULATION",order)

@app.get("/countries/area")
def countries_by_area(order="DESC"):
  return get_all_by_property("AREA",order)

@app.get("/countries/density")
def countries_by_density(order="DESC"):
  return get_all_by_property("DENSITY",order)

@app.get("/countries/constitutional_form")
def countries_by_constitutional_form(order="ASC"):
  return get_all_by_property("constitutional_form",order)

@app.get("/countries/neighbouring_countries")
def countries_by_neighbouring_countries():
  return get_all_neighbouring_countries()

@app.get("/countries/languages/official")
def countries_by_official_languages():
  return get_all_languages("official_languages")

@app.get("/countries/languages/national")
def countries_by_national_languages():
  return get_all_languages("national_languages")

@app.get("/countries/languages/regional")
def countries_by_regional_languages():
  return get_all_languages("regional_languages")

@app.get("/countries/languages/widely_spoken")
def countries_by_widely_spoken_languages():
  return get_all_languages("widely_spoken_languages")

@app.get("/countries/languages/minority")
def countries_by_widely_spoken_languages():
  return get_all_languages("minority_languages")

@app.get("/countries/time_zones")
def countries_by_time_zones():
  return get_all_time_zones()

@app.get("/countries/time_zone/{time_zone}")
def countries_by_time_zone(time_zone):
  return get_countries_by_time_zone(time_zone)

@app.get("/countries/language/official_languages/{language}")
def countries_by_official_language(language):
  return get_countries_by_language("official_languages",language)

@app.get("/countries/language/national_languages/{language}")
def countries_by_national_language(language):
  return get_countries_by_language("national_languages",language)

@app.get("/countries/language/regional_languages/{language}")
def countries_by_regional_language(language):
  return get_countries_by_language("regional_languages",language)

@app.get("/countries/language/widely_spoken_languages/{language}")
def countries_by_widely_spoken_language(language):
  return get_countries_by_language("widely_spoken_languages",language)

@app.get("/countries/language/minority_languages/{language}")
def countries_by_minority_language(language):
  return get_countries_by_language("minority_languages",language)

@app.get("/countries/constitutional_form/{constitutional_form}")
def countries_by_constitutional_form(constitutional_form):
  return get_countries_by_constitutional_form(constitutional_form)

@app.get("/countries/capitals/more_than_1")
def countries_with_more_than_1_capital():
  return get_countries_with_more_than_1_capital()