# states_of_the_world

States of the world is a python project that crawls Wikipedia pages of countries of the world and retrieves information such as: name, capital/s name, population, density, area, neighbors, languages (official, national, widely spoken, minority, regional), time zones, type of political regime (democratic, monarchy, etc) and stores it in a database (MySQL)
Additionally, it builds an API (fastAPI) over the database which has multiple routes that can be called with the GET method.


install

pip install mysql-connector-python

pip install pandas

pip install fastapi

pip install uvicorn

# start the server

python .\wikipedia_api.py

# run the client

python .\client.py
