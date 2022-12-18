import requests


def printer(text):
    text = text.replace("\"", "") 
    header = text.split("\\n")[0]
    data = text.split("\\n")[1:]
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    for index,row in enumerate(data):
        if row.strip():
            print(f"{index+1}. {row}")
    

if __name__ == "__main__":
    api_url = "http://127.0.0.1:8000"
    response = requests.get(api_url + "/top_10_countries_by_population")
    printer(response.text)

    response = requests.get(api_url + "/top_10_countries_by_area")
    printer(response.text)

    response = requests.get(api_url + "/top_10_countries_by_density")
    printer(response.text)

    

