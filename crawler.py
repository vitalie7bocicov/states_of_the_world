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


def clean_title_population(title):
    if title.startswith("Demographics of the") or title.startswith("Demography of the"):
        return title[title.find("the ")+4:]

    if title.startswith("Demograph"):
        return title[title.find("of ")+3:]
    if title.startswith("Population of"):
        return title[title.find("of ")+3:]
    return title


def get_population(url, countries):
    code = requests.get(url)
    plain = code.text
    soup = BeautifulSoup(plain, "html5lib")

    countries = dict((country, None) for country in countries)

    for tr in soup.find_all("tr"):
        tds = tr.find_all("td")

        if len(tds) < 2:
            continue

        country_td = tds[0]
        anchor = country_td.a

        if not anchor:
            continue

        if not anchor.get("title"):
            continue
        
        title = anchor.get("title")
        
        country = clean_title_population(title)
        if country in countries:
            td_population = anchor.find_parent("td").find_next_sibling("td")
            if td_population:
                try:
                    countries[country] = td_population.text
                except Exception as e:
                    print(e)
                    print("No population for {}".format(country))
            else:
                print("No population for {}".format(country))
    return countries

def clean_country_name(country):
    if country == "Kingdom of the Netherlands":
        return "Netherlands"
    return country

def init_countries(url):
    code = requests.get(url)
    plain = code.text
    soup = BeautifulSoup(plain, "html5lib")
    anchors = soup.select("td > b > a[href]")
    countries = []
    for anchor in anchors:
        country = clean_country_name(anchor.get("title"))
        countries.append(country)
    return countries
    

if __name__ == "__main__":
    countries = init_countries("https://en.wikipedia.org/wiki/List_of_sovereign_states")
    capitals = get_capitals("https://en.wikipedia.org/wiki/List_of_national_capitals", countries)
    population = get_population("https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population", countries)
    for country in countries:
        if population[country]==None:
            print("No population for {}".format(country))