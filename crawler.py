import requests
from bs4 import BeautifulSoup

def get_capitals(url, countries):
    code = requests.get(url)
    plain = code.text
    soup = BeautifulSoup(plain, "html5lib")
    capitals = dict((country, None) for country in countries)
    for tr in soup.find_all("tr"):
        tds = tr.find_all("td")
        if len(tds) < 2: continue
        country_td = tds[1]
        anchors = country_td.select("a[href]")
        for anchor in anchors:
            if anchor.get("title") in countries:
                country = anchor.get("title")
                td_capital = anchor.find_parent("td").find_previous_sibling("td")
                if not td_capital:
                    print("No capital for {}".format(country))
                    continue
                try:
                    capitals[country] = td_capital.select("a[href]")[0].text
                except Exception as e:
                    print(e)
                    print("No capital for {}".format(country))
        if len(tds) == 1:
            # Palestine is a special case
            country_td = tds[0]
            anchor = country_td.a
            if not anchor:
                continue
            if anchor.get("title") in countries:
                country = anchor.get("title")
                try:
                    td_capital = anchor.find_parent("tr").find_previous_sibling("tr").find_all("td")[0]
                    capitals[country] = td_capital.select("a[href]")[0].text
                except Exception as e:
                    print(e)
                    print("No capital for {}".format(country))
    return capitals

def clean_title_helper(title):
    if title.startswith("Demographics of the") or title.startswith("Demography of the"):
        return title[title.find("the ")+4:]
    if title.startswith("Demograph"):
        return title[title.find("of ")+3:]
    if title.startswith("Population of"):
        return title[title.find("of ")+3:]
    return title

def get_col_number(column):
    if column == "Population" or column == "Constitutional form" or column == "Official languages":
        return 1
    if column == "Area" or column == "Time zones" or column == "Regional languages":
        return 2
    if column == "Minority languages":
        return 3
    if column == "Density" or column == "National languages":
        return 4
    if column == "Neigbouring countries" or column == "Widely spoken languages":
        return 5

def get_demographics_info(column, countries):
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
        country = clean_title_helper(title)

        # special case for Ireland
        if country=="Ireland": country = "Republic of Ireland"

        if country not in countries: continue
        td_info = anchor.find_parent("th")
        column_number = get_col_number(column)
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

def is_valid_anchor(anchors):
    if not anchors: 
        return False
    anchor = anchors[0]
    if not anchor: 
        return False
    if not anchor.get("title"):
        return False
    return True

def get_multiple_info(url, countries,column):
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
        if not is_valid_anchor(anchors): continue
        anchor = anchors[0]
        country = anchor.get("title")
        if country not in countries: continue
        td_info = anchor.find_parent("td")
        column_number = get_col_number(column)
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
                data[country] = td_info.text
        except Exception as e:
            print(e)
            print("No multiple info for {} with {}".format(country,column))
    return data

def format_country_name(country):
    if country == "Bahamas": return "The Bahamas"
    if country == "Bahamas": return "The Bahamas"
    if country == "Gambia": return "The Gambia"
    if country == "Georgia": return "Georgia (country)"
    if country == "Ireland": return "Republic of Ireland"
    if country == "Artsakh": return "Republic of Artsakh"
    return country

def format_languages(languages):
    if not languages: return []
    if languages[0].startswith("None") or languages[0].strip()=='':
        return []
    if languages[0].find("languages - ") != -1:
            multiple_languages = languages[0][languages[0].find("languages - ")+12:]
            languages = multiple_languages.split(", ")
    for i in range(len(languages)):
        languages[i] = languages[i].strip()
        if languages[i].find("[")!= -1:
           languages[i] = languages[i][:languages[i].find("[")]
        if languages[i].find("(") != -1:
            languages[i] = languages[i][:languages[i].find("(")]
        if languages[i].find("language") != -1:
            languages[i] = languages[i].replace(" language","")
        if languages[i].find(" and ") != -1:
            languages[i] = languages[i].replace(" and ","")
        if (languages[i].find("dialects") != -1
                or languages[i].find("see ") != -1 
                or languages[i].find("Languages of") != -1):
            del languages[i]
            continue
        if languages[i].find("in ") != -1:
            languages[i] = languages[i].replace("in ","")
        if languages[i].find(" people") != -1:
            languages[i] = languages[i].replace(" people","")
        languages[i] = languages[i].strip()
        if languages[i].find("\n") != -1:
            languages[i] = languages[i].replace("\n"," ")
    if not languages:
        return []
    if languages[0].strip()=='':
        return []
    if languages[0].find("Regional/State")!= -1:
        return []
    return languages

def get_languages_from_td(td, country, countries):
    ul = td.find("ul")
    if ul:
        for li in ul.find_all("li"):
            if li.text.startswith("None"): break
            if li.find("a[title]"):
                countries[country].append(li.a.get("title"))
            else:
                countries[country].append(li.text)
    else:
        if td.find("p"): 
            td = td.find("p")
        if td.next_element.name == "a":
                countries[country].append(td.next_element.get("title"))
        else:
            countries[country].append(td.next_element.text)
    return countries[country]

def get_languages(column, countries):
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
        if not is_valid_anchor(anchors): continue
        anchor = anchors[0]
        country = anchor.text
        if country not in countries:
            country = format_country_name(country)
            if country not in countries: continue
        td_info = anchor.find_parent("td")

        column_number = get_col_number(column)
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

def init_countries(url):
    code = requests.get(url)
    plain = code.text
    soup = BeautifulSoup(plain, "html5lib")
    anchors = soup.select("td > b > a[href]")
    countries = []
    for anchor in anchors:
        country = anchor.get("title")
        if country == "Kingdom of the Netherlands" : country = "Netherlands"
        countries.append(country)
    return countries

def crawl():
    countries = init_countries("https://en.wikipedia.org/wiki/List_of_sovereign_states")
    capitals = get_capitals("https://en.wikipedia.org/wiki/List_of_national_capitals", countries)
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



 
  