from fastapi import FastAPI
from  db.queries import *
from db.queries import *
app = FastAPI()

@app.get("/top_10_countries_by_population")
def top_10_by_population():
  return get_top_10_by_property("population")

@app.get("/top_10_countries_by_area")
def top_10_by_area():
  return get_top_10_by_property("area")

@app.get("/top_10_countries_by_density")
def top_10_by_density():
  return get_top_10_by_property("density")