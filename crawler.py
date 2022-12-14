import requests
from bs4 import BeautifulSoup

def get_capitals(url, countries):
    code = requests.get(url)
    plain = code.text
    soup = BeautifulSoup(plain, "html5lib")

    countries = dict((country, None) for country in countries)

    for tr in soup.find_all("tr"):
        tds = tr.find_all("td")
        if len(tds) < 2:
            continue
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
                    countries[country] = td_capital.select("a[href]")[0].text
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
                    countries[country] = td_capital.select("a[href]")[0].text
                except Exception as e:
                    print(e)
                    print("No capital for {}".format(country))
    return countries

def clean_title_helper(title):
    if title.startswith("Demographics of the") or title.startswith("Demography of the"):
        return title[title.find("the ")+4:]

    if title.startswith("Demograph"):
        return title[title.find("of ")+3:]
    if title.startswith("Population of"):
        return title[title.find("of ")+3:]
    return title

def get_col_number(column):
    if column == "Population":
        return 1
    if column == "Area" or column == "Time zones":
        return 2
    if column == "Density":
        return 4
    if column == "Neigbouring countries":
        return 5

def get_single_info(column, countries):
    url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population_density"
    code = requests.get(url)
    plain = code.text
    soup = BeautifulSoup(plain, "html5lib")

    countries = dict((country, None) for country in countries)

    for th in soup.find_all("th"):
        anchor = th.a

        if not anchor:
            continue
        if not anchor.get("title"):
            continue
        
        title = anchor.get("title")
        
        country = clean_title_helper(title)

        # special case for Ireland
        if country=="Ireland": country = "Republic of Ireland"

        if country not in countries:
            continue
        td_info = anchor.find_parent("th")
        column_number = get_col_number(column)
        while column_number > 0:
            td_info = td_info.find_next_sibling("td")
            column_number -= 1
        if not td_info:
            print ("No info for {}, on column {}".format(country, column))
        try:
            countries[country] = int(td_info.text.replace(",", ""))
        except Exception as e:
            print(e)
            print ("No info for {}, on column {}".format(country, column))
    return countries

def get_multiple_info(url, countries,column):
    code = requests.get(url)
    plain = code.text
    soup = BeautifulSoup(plain, "html5lib")
    countries = dict((country, None) for country in countries)
    for tr in soup.find_all("tr"):
        tds = tr.find_all("td")
        if len(tds) < 2:
            continue
        if column == "Neigbouring countries": country_td = tds[1]
        else: country_td = tds[0]
        anchors = country_td.select("a[href]")
        if not anchors:
            continue
        anchor = anchors[0]
        if not anchor:
            continue
        if not anchor.get("title"):
            continue
        if anchor.get("title") in countries:
            country = anchor.get("title")
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
                    countries[country] = [anchor.get("title") for anchor in anchors if anchor.get("title") and anchor.get("title") in countries]
                elif column == "Time zones":
                    countries[country] = [anchor.get("title") for anchor in anchors if anchor.get("title") and anchor.get("title").startswith("UTC")]
            except Exception as e:
                print(e)
                print("No multiple info for {} with {}".format(country,column))
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
    

if __name__ == "__main__":
    countries = init_countries("https://en.wikipedia.org/wiki/List_of_sovereign_states")
    capitals = get_capitals("https://en.wikipedia.org/wiki/List_of_national_capitals", countries)
    population = get_single_info("Population", countries)
    area = get_single_info("Area", countries)
    density = get_single_info("Density", countries)
    neigbouring_countries = get_multiple_info("https://en.wikipedia.org/wiki/List_of_countries_and_territories_by_land_borders", countries, "Neigbouring countries")
    time_zones = get_multiple_info("https://en.wikipedia.org/wiki/List_of_time_zones_by_country", countries, "Time zones")
  