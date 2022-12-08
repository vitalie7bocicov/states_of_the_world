import requests
from bs4 import BeautifulSoup

def add_capitals(url, countries):
    code = requests.get(url)
    plain = code.text
    soup = BeautifulSoup(plain, "html5lib")

    for tr in soup.find_all("tr"):
        tds = tr.find_all("td")
        if len(tds) >= 2:
            country_td = tds[1]
            anchors = country_td.select("a[href]")
            for anchor in anchors:
                if anchor.get("title") in countries:
                    country = anchor.get("title")
                    td_capital = anchor.find_parent("td").find_previous_sibling("td")
                    if td_capital:
                        countries[country] = td_capital.select("a[href]")[0].text
                    else:
                        print("No capital for {}".format(country))
        elif len(tds) == 1:
            # Palestine is a special case
            country_td = tds[0]
            anchor = country_td.a
            if anchor:
                if anchor.get("title") in countries:
                    country = anchor.get("title")
                    td_capital = anchor.find_parent("tr").find_previous_sibling("tr").find_all("td")[0]
                    countries[country] = td_capital.select("a[href]")[0].text
            
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
    countries = dict()
    for anchor in anchors:
        country = clean_country_name(anchor.get("title"))
        countries[country] = None
    return countries
    

if __name__ == "__main__":
    countries = init_countries("https://en.wikipedia.org/wiki/List_of_sovereign_states")
    add_capitals("https://en.wikipedia.org/wiki/List_of_national_capitals", countries)

    for country, capital in countries.items():
        if capital is None:
            print("No capital for {}".format(country))
        else:
            print("{}: {}".format(country, capital))