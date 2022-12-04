import requests, re
from bs4 import BeautifulSoup

def get_capitals(soup):
    capitals=[]
    for tr in soup.select('table > tbody > tr'):
        th = tr.find("th",class_="infobox-label", scope="row")
        if(re.match(r".*>Capital<.*",str(th))):
            is_found = False
            for anchor in tr.td.select("td > a[href]"):
                capitals.append(anchor.get("title"))
                is_found = True
            if not is_found:
                for anchor in tr.td.select("td > span > a[href]"):
                    capitals.append(anchor.get("title"))
                    is_found = True
            if not is_found:
                for anchor in tr.td.select("td div ul li > a[href]"):
                    capitals.append(anchor.get("title"))
                    is_found = True
    return capitals

def get_population(soup):
    anchors = soup.select(f"tr[class=\"mergedtoprow\"] > th[class=\"infobox-header\"] > a[title]")
    population = 0
    for anchor in anchors:
        if str(anchor.next_element).strip() == "Population":
            element = anchor.find_parent("tr").next_sibling.td.next_element
            if(str(element).find("div") != -1):
                element=element.ul.li.next_element
            if(str(element).find("img") != -1 or str(element).find("span") != -1):
                element = element.next_element
            population = str(element).strip().split(" ")[0]
            population = int(population.replace("(","").replace(",",""))
        elif str(anchor.next_element).strip() == "Area":
             ok=1
    # missing a[title] on tr > th
    if population == 0:
        ths = soup.select(f"tr[class=\"mergedtoprow\"] > th[class=\"infobox-header\"]")
        for th in ths:
            if str(th.next_element) == 'Population':
                element = th.find_parent("tr").next_sibling.td.next_element
                if(str(element).find("div") != -1):
                    element=element.ul.li.next_element
                if(str(element).find("img") != -1 or str(element).find("span") != -1):
                    element = element.next_element
                population = str(element).strip().split(" ")[0]
                population = int(population.replace("(","").replace(",",""))
    return population

def convert_sq_mi_to_sq_km(sq_mi):
    return float(sq_mi) / 2.589988

def get_density(soup):
    anchors = soup.select(f"tr[class=\"mergedtoprow\"] > th[class=\"infobox-header\"] > a[title]")
    density = 0
    for anchor in anchors:
        if str(anchor.next_element).strip() == "Population":
            element = anchor.find_parent("tr")
            while "mergedbottomrow" not in element.get("class"):
                element = element.next_sibling
            if str(element.th.div.next_element).find("Density")!=-1:
                density = element.td.next_element
    # missing a[title] on tr > th
    if density == 0:
        ths = soup.select(f"tr[class=\"mergedtoprow\"] > th[class=\"infobox-header\"]")
        for th in ths:
            if str(th.next_element) == 'Population':
                element = th.find_parent("tr")
                while "mergedbottomrow" not in element.get("class"):
                    element = element.next_sibling
                if str(element.th.div.next_element).find("Density")!=-1:
                    density = element.td.next_element
    if density!=0 : 
        density = density.split(" ")[0]
        density = density.replace(",","")
        if density.find("sq")!=-1:
            density = density.split("/")[0]
            density = convert_sq_mi_to_sq_km(density)
        if str(density).find("km")!=-1:
            density = float(density.split("/")[0])
    return density

def get_area(soup):
    anchors = soup.select(f"tr[class=\"mergedtoprow\"] > th[class=\"infobox-header\"] > a[href]")
    area = 0
    for anchor in anchors:
        if str(anchor.next_element).strip() == "Area":
            area = anchor.find_parent("tr").next_sibling.td.next_element
    # missing a[title] on tr > th
    if area == 0:
        ths = soup.select(f"tr[class=\"mergedtoprow\"] > th[class=\"infobox-header\"]")
        for th in ths:
            if str(th.next_element) == 'Area':
                area = th.find_parent("tr").next_sibling.td.next_element
 
    if area!=0:
        area = area.replace(u'\xa0', u' ')
        area = area.replace(",","")
        if area.find("sq")!=-1:
            area = area.split(" ")[0]
            area = convert_sq_mi_to_sq_km(area)
        elif area.find("km")!=-1:
           area = area.split(" ")[0]
           if area.find("–")!=-1:
                area = area.split("–")[0]
           area = float(area)
    return area


def get_country_data(url):
    base_url = "https://en.wikipedia.org"
    url = base_url + url
    code = requests.get(url)
    plain = code.text
    soup = BeautifulSoup(plain, "html5lib")
    country_name = soup.find("h1",id="firstHeading").text
    capitals = get_capitals(soup)
    population = get_population(soup)
    density = get_density(soup)
    area = get_area(soup)
    print(f"{country_name}   -  Capital/s: {capitals}  -  Population: {population}    -   Density: {density}    -  Area: {area}")

def crawl(url):
    code = requests.get(url)
    plain = code.text
    soup = BeautifulSoup(plain, "html5lib")
    anchors = soup.select("td > b > a[href]")
    for anchor in anchors:
        get_country_data(anchor.get("href"))
crawl("https://en.wikipedia.org/wiki/List_of_sovereign_states")

