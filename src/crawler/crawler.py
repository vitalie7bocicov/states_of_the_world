import requests
from bs4 import BeautifulSoup
from .helpers import *

def get_other_capitals(capitals, tr, td, countries):
    """
    Get a list of capital cities for a given list of countries.

    :param capitals: A list of capital cities for a given country.
    :type capitals: list
    :param tr: A BeautifulSoup object representing a table row.
    :type tr: BeautifulSoup
    :param td: A BeautifulSoup object representing a table cell.
    :type td: BeautifulSoup
    :param countries: A list of strings representing the names of the countries.
    :type countries: list
    :returns: A list of capital cities for a given country.
    :rtype: list
    """
    tr_sibling = tr.find_next_sibling("tr")
    if not tr_sibling:
        return capitals
    tds = tr_sibling.find_all("td")
    if len(tds)>2: 
        return capitals
    td = tds[0]
    anchors = td.select("a[href]")
    if not anchors_are_valid(anchors): 
        return capitals
    anchor = anchors[0]
    if anchor.get("title") in countries: 
        return capitals
    capitals.append(anchor.text)
    return capitals
        
def get_capitals(countries):
    """
    Get a list of capital cities for a given list of countries.

    :param countries: A list of strings representing the names of the countries.
    :type countries: list
    :returns: A dictionary mapping each country to a list of its capital cities.
    :rtype: dict
    """
    url = "https://en.wikipedia.org/wiki/List_of_national_capitals"
    code = requests.get(url)
    plain = code.text
    soup = BeautifulSoup(plain, "html5lib")
    capitals = dict((country, []) for country in countries)
    for tr in soup.find_all("tr"):
        tds = tr.find_all("td")
        if len(tds) < 2: continue
        country_td = tds[1]
        anchors = country_td.select("a[href]")
        if not anchors_are_valid(anchors): continue
        anchor = anchors[0]
        country = anchor.get("title")
        if country not in countries: continue
        country_td = anchor.find_parent("td")
        capital_td = country_td.find_previous_sibling("td")
        if not capital_td:
            print("No capital information found for {}".format(country))
            continue
        try:
            # first capital
            capitals[country].append(capital_td.select("a[href]")[0].text)
            capitals[country] = get_other_capitals(capitals[country], tr, capital_td, countries)
            # special case for South Africa
            if country == "South Africa":
                capitals[country] = get_other_capitals(capitals[country],
                 tr.find_next_sibling("tr"), capital_td, countries)   
        except Exception as e:
            print(e)
            print("No capital information found for {}".format(country))
    # special case for State of Palestine
    capitals["State of Palestine"] = capitals["Israel"]
    return capitals

def get_demographics_info(column, countries):
    """
    Get demographic information for a list of countries from Wikipedia.

    :param column: The column number or name for the desired information on the Wikipedia page.
    :type column: int or str
    :param countries: A list of strings representing the names of the countries.
    :type countries: list
    :returns: A dictionary mapping each country to its demographic information as an integer.
    :rtype: dict
    """
    url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population_density"
    code = requests.get(url)
    plain = code.text
    soup = BeautifulSoup(plain, "html5lib")
    demographics = dict((country, None) for country in countries)
    for th in soup.find_all("th"):
        anchor = th.a
        if not anchor: continue
        if not anchor.get("title"): continue
        title = anchor.get("title")
        country = clean_title(title)
        # special case for Ireland
        if country=="Ireland": country = "Republic of Ireland"

        if country not in countries: continue
        td_info = anchor.find_parent("th")
        column_number = get_column_number(column)
        while column_number > 0:
            td_info = td_info.find_next_sibling("td")
            column_number -= 1
        if not td_info:
            print ("No info for {}, on column {}".format(country, column))
        try:
            demographics[country] = int(td_info.text.replace(",", ""))
        except Exception as e:
            print(e)
            print ("No info for {}, on column {}".format(country, column))
    return demographics

def get_multiple_info(url, countries,column):
    """
    Get specific information for each country in the given list from the given Wikipedia page.

    :param url: The URL of the Wikipedia page to scrape.
    :type url: str
    :param countries: A list of strings representing the names of countries.
    :type countries: list
    :param column: The column number or name for the desired information on the Wikipedia page.
    :type column: int or str
    :returns: A dictionary mapping country names to the desired information.
    :rtype: dict
    """
    code = requests.get(url)
    plain = code.text
    soup = BeautifulSoup(plain, "html5lib")
    data = dict((country, None) for country in countries)
    for tr in soup.find_all("tr"):
        tds = tr.find_all("td")
        if len(tds) < 2: continue
        if column == "Neigbouring countries": country_td = tds[1]
        else: country_td = tds[0]
        anchors = country_td.select("a[href]")
        if not anchors_are_valid(anchors): continue
        anchor = anchors[0]
        country = anchor.get("title")
        if country not in countries: continue
        td_info = anchor.find_parent("td")
        column_number = get_column_number(column)
        while column_number > 0:
            td_info = td_info.find_next_sibling("td")
            column_number -= 1
        if not td_info:
            print("No multiple info for {}".format(country))
            continue
        try:
            anchors = td_info.select("a[href]")
            if column == "Neigbouring countries":
                data[country] = [anchor.get("title") for anchor in anchors if anchor.get("title") and anchor.get("title") in countries]
            elif column == "Time zones":
                data[country] = [anchor.get("title") for anchor in anchors if anchor.get("title") and anchor.get("title").startswith("UTC")]
            elif column == "Constitutional form":
                data[country] = td_info.text.strip()
        except Exception as e:
            print(e)
            print("No multiple info for {} with {}".format(country,column))
    return data

def get_languages(column, countries):
    """
    Get a list of languages by given column for each country in the given list.

    :param column: The column number for the language information on the Wikipedia page.
    :type column: int
    :param countries: A list of strings representing the names of countries.
    :type countries: list
    :returns: A dictionary mapping country names to lists of official languages.
    :rtype: dict
    """
    url = "https://en.wikipedia.org/wiki/List_of_official_languages_by_country_and_territory"
    code = requests.get(url)
    plain = code.text
    soup = BeautifulSoup(plain, "html5lib")
    countries = dict((country, []) for country in countries)
    for tr in soup.find_all("tr"):
        tds = tr.find_all("td")
        if len(tds) < 2: continue
        country_td = tds[0]
        anchors = country_td.select("a[href]")
        if not anchors_are_valid(anchors): continue
        anchor = anchors[0]
        country = anchor.text
        if country not in countries:
            country = normalize_country_name(country)
            if country not in countries: continue
        td_info = anchor.find_parent("td")

        column_number = get_column_number(column)
        while column_number > 0:
            td_info = td_info.find_next_sibling("td")
            column_number -= 1
        if not td_info:
            continue
        try:
            countries[country] = get_languages_from_td(td_info, country, countries)
            countries[country] = format_languages(countries[country])
        except Exception as e:
            print(e)
            print("No language info for {} with {}".format(country,column))
    return countries

def init_countries():
    """
    Initialize a list of countries by scraping Wikipedia.

    :returns: A list of strings representing the names of countries.
    :rtype: list
    """
    url = "https://en.wikipedia.org/wiki/List_of_sovereign_states"
    code = requests.get(url)
    plain = code.text
    soup = BeautifulSoup(plain, "html5lib")
    anchors = soup.select("td > b > a[href]")
    countries = []
    for anchor in anchors:
        country = anchor.get("title")
        # special case
        if country == "Kingdom of the Netherlands" : country = "Netherlands"
        countries.append(country)
    return countries

def crawl():
    """
    Crawl the Wikipedia websites for the data on the countries and their properties.

    :returns: A list with the countries, capitals, population, area, density, neighbouring countries, time zones,
            constitutional form, official languages, regional languages, minority languages, national languages, and
            widely spoken languages.
    :rtype: list
    """
    countries = init_countries()
    capitals = get_capitals(countries)
    population = get_demographics_info("Population", countries)
    area = get_demographics_info("Area", countries)
    density = get_demographics_info("Density", countries)
    neigbouring_countries = get_multiple_info("https://en.wikipedia.org/wiki/List_of_countries_and_territories_by_land_borders", countries, "Neigbouring countries")
    time_zones = get_multiple_info("https://en.wikipedia.org/wiki/List_of_time_zones_by_country", countries, "Time zones")
    constitutional_form = get_multiple_info("https://en.wikipedia.org/wiki/List_of_countries_by_system_of_government", countries, "Constitutional form")
    official_languages = get_languages( "Official languages",countries)
    regional_languages = get_languages( "Regional languages",countries)
    minority_languages = get_languages( "Minority languages",countries)
    national_languages = get_languages( "National languages",countries)
    widely_spoken_languages = get_languages( "Widely spoken languages",countries)

    return [countries, capitals, population, area, density, neigbouring_countries,
            time_zones, constitutional_form, official_languages, regional_languages,
            minority_languages, national_languages, widely_spoken_languages]
