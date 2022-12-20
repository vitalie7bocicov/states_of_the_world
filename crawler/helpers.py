
def anchors_are_valid(anchors):
    """
    Check if the given anchors are valid.

    This function checks if the given anchors are not empty and contain a title. It returns a boolean indicating whether
    the anchors are valid or not.

    :param anchors: The anchors to be checked.
    :type anchors: list of dict
    :returns: A boolean indicating whether the anchors are valid or not.
    :rtype: bool
    """
    if not anchors: 
        return False
    anchor = anchors[0]
    if not anchor: 
        return False
    if not anchor.get("title"):
        return False
    return True

def clean_title(title):
    """
    Clean the given title by removing unnecessary prefixes.

    This function removes unnecessary prefixes from the given title, such as "Demographics of the" or "Population of",
    in order to obtain the name of the country.

    :param title: The title to be cleaned.
    :type title: str
    :returns: The cleaned version of the title.
    :rtype: str
    """
    if title.startswith("Demographics of the") or title.startswith("Demography of the"):
        return title[title.find("the ")+4:]
    if title.startswith("Demograph"):
        return title[title.find("of ")+3:]
    if title.startswith("Population of"):
        return title[title.find("of ")+3:]
    return title

def get_column_number(column):
    """
    Get the number of the column corresponding to the given property.

    This function maps the given property to a specific column number in a table. The column number is used to retrieve
    the data for the given property.

    :param column: The property for which the column number is to be retrieved.
    :type column: str
    :returns: The column number for the given property.
    :rtype: int
    """
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

def normalize_country_name(country):
    """
    Normalize the given country name.

    Some country names may be ambiguous or not match the official name of the country. This function returns the
    official name of the country for the given input.

    :param country: The name of the country to be normalized.
    :type country: str
    :returns: The normalized country name.
    :rtype: str
    """
    if country == "Bahamas": return "The Bahamas"
    if country == "Bahamas": return "The Bahamas"
    if country == "Gambia": return "The Gambia"
    if country == "Georgia": return "Georgia (country)"
    if country == "Ireland": return "Republic of Ireland"
    if country == "Artsakh": return "Republic of Artsakh"
    return country

def clean_language(language):
    """
    Clean the given language string by removing unnecessary characters and words.

    :param language: The language string to be cleaned.
    :type language: str
    :returns: The cleaned language string.
    :rtype: str
    """
    language = language.strip()
    if language.find("[")!= -1:
        language = language[:language.find("[")]
    if language.find("(") != -1:
        language = language[:language.find("(")]
    if language.find("language") != -1:
        language = language.replace(" language","")
    if language.find(" and ") != -1:
        language = language.replace(" and ","")
    if (language.find("dialects") != -1
        or language.find("see ") != -1 
        or language.find("Languages of") != -1):
        return ""
    if language.find("in ") != -1:
        language = language.replace("in ","")
    if language.find(" people") != -1:
        language = language.replace(" people","")
    language = language.strip()
    if language.find("\n") != -1:
        language = language.replace("\n"," ")
    return language

def format_languages(languages):
    """
    Format the given list of languages by cleaning and normalizing them.

    This function removes unnecessary prefixes and suffixes from the languages in the list, and splits multiple languages
    that are separated by commas. It also removes empty or invalid languages.

    :param languages: The list of languages to be formatted.
    :type languages: list of str
    :returns: The formatted list of languages.
    :rtype: list of str
    """
    if not languages:
        return []
    if (languages[0].startswith("None") 
        or languages[0].strip()==''):
        return []
    if languages[0].find("languages - ") != -1:
            multiple_languages = languages[0][languages[0].find("languages - ")+12:]
            languages = multiple_languages.split(", ")
    for i in range(len(languages)):
        languages[i] = clean_language(languages[i])
    if not languages:
        return []
    if languages[0].strip()=='':
        return []
    if languages[0].find("Regional/State")!= -1:
        return []
    return languages

def get_languages_from_td(td, country, countries):
    """
    Get the languages from the given td element.

    This function retrieves the languages from the given td element and adds them to the list of languages for the given
    country.

    :param td: The td element from which the languages are to be retrieved.
    :type td: bs4.element.Tag
    :param country: The name of the country for which the languages are to be retrieved.
    :type country: str
    :param countries: The dictionary of countries and their languages.
    :type countries: dict of str to list of str
    :returns: The list of languages for the given country.
    :rtype: list of str
    """
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
