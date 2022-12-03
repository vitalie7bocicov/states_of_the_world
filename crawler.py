import requests, re
from bs4 import BeautifulSoup

def get_country_data(url):
    base_url = "https://en.wikipedia.org"
    url = base_url + url
    code = requests.get(url)
    plain = code.text
    soup = BeautifulSoup(plain, "html5lib")

    country_name = soup.find("h1",id="firstHeading").text

def crawl(url):
    code = requests.get(url)
    plain = code.text
    soup = BeautifulSoup(plain, "html5lib")
    anchors = soup.select("td > b > a[href]")
    for anchor in anchors:
        get_country_data(anchor.get("href"))
crawl("https://en.wikipedia.org/wiki/List_of_sovereign_states")

