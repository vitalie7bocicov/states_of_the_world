import requests

def printer(text):
    """
    Prints the given text in a formatted way.

    The text is split into a header and rows of data. The header is
    surrounded by a row of dashes, and each row of data is preceded by
    its index in the list.

    :param text: the text to be printed
    :return: None
    """
    text = text.replace("\"", "") 
    header = text.split("\\n")[0]
    data = text.split("\\n")[1:]
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    index = 1
    for row in data:
        row = row.strip()
        if row:
            print(f"{index}. {row}")
            index += 1
    

if __name__ == "__main__":
    api_url = "http://127.0.0.1:8000"
    # response = requests.get(api_url + "/top_10_countries_by_population")
    # printer(response.text)

    # response = requests.get(api_url + "/top_10_countries_by_area")
    # printer(response.text)

    # response = requests.get(api_url + "/top_10_countries_by_density")
    # printer(response.text)
    
    # response = requests.get(api_url + "/countries")
    # printer(response.text)

    # response = requests.get(api_url + "/countries/capitals")
    # printer(response.text)

    # response = requests.get(api_url + "/countries/population")
    # printer(response.text)

    # response = requests.get(api_url + "/countries/population?order=asc")
    # printer(response.text)

    # response = requests.get(api_url + "/countries/population?order=desc")
    # printer(response.text)

    # response = requests.get(api_url + "/countries/area?order=asc")
    # printer(response.text)

    # response = requests.get(api_url + "/countries/density?order=desc")
    # printer(response.text)

    # response = requests.get(api_url + "/countries/constitutional_form")
    # printer(response.text)

    # response = requests.get(api_url + "/countries/neighbouring_countries")
    # printer(response.text)

    # response = requests.get(api_url + "/countries/languages/official")
    # printer(response.text)

    # response = requests.get(api_url + "/countries/languages/national")
    # printer(response.text)

    # response = requests.get(api_url + "/countries/languages/regional")
    # printer(response.text)

    # response = requests.get(api_url + "/countries/languages/widely_spoken")
    # printer(response.text)

    # response = requests.get(api_url + "/countries/languages/minority")
    # printer(response.text)

    # response = requests.get(api_url + "/countries/time_zones")
    # printer(response.text)

    # response = requests.get(api_url + "/countries/Cyprus")
    # printer(response.text)

    # response = requests.get(api_url + "/countries/Romania")
    # printer(response.text)

    # response = requests.get(api_url + "/countries/Vatican City")
    # printer(response.text)

    # response = requests.get(api_url + "/countries/time_zone/UTC+03:00")
    # printer(response.text)

    # response = requests.get(api_url + "/countries/language/official_languages/English")
    # printer(response.text)

    # response = requests.get(api_url + "/countries/language/official_languages/Romanian")
    # printer(response.text)

    # response = requests.get(api_url + "/countries/language/national_languages/English")
    # printer(response.text)

    # response = requests.get(api_url + "/countries/language/regional_languages/Romanian")
    # printer(response.text)

    # response = requests.get(api_url + "/countries/language/widely_spoken_languages/Russian")
    # printer(response.text)

    # response = requests.get(api_url + "/countries/language/minority_languages/Romanian")
    # printer(response.text)

    # respone = requests.get(api_url + "/countries/constitutional_form/Provisional")
    # printer(respone.text)
    
    # respone = requests.get(api_url + "/countries/constitutional_form/Constitutional monarchy")
    # printer(respone.text)

    # respone = requests.get(api_url + "/countries/constitutional_form/Republic")
    # printer(respone.text)

    # # more than 1 capital
    # respone = requests.get(api_url + "/countries/capitals/more_than_1")
    # printer(respone.text)