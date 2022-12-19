import requests

def printer(text):
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
