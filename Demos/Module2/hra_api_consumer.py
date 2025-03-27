import requests
from pprint import pprint

from hra_api_client import SpatialSearch, MinMax

url = "https://apps.humanatlas.io/hra-api/v1/cell-type-term-occurences"

params = {
    "age": MinMax(min=45.0, max=60.0),
    "bmi": MinMax(min=65.0, max=83.0),
    "sex": "Female",
    "technologies": [],
    "providers": [],
    "ontology_terms": ["http://purl.obolibrary.org/obo/UBERON_0000955"],
    "cell_type_terms": ["http://purl.obolibrary.org/obo/CL_0000000"],
    "spatial": [
        SpatialSearch(
            x=84.0,
            y=146.0,
            z=53.0,
            radius=12.0,
            target="https://purl.org/ccf/latest/ccf.owl#VHFAllenBrain"
        )
    ]
}


def handle_api(url):
    try:
        response = requests.get(url, params = params)
        if response.status_code == 200:
            print("the GET request worked :)")
            pprint(response.text)
        else: #ie if the response isnt a success
            print(f"GET request failed :( {response.status_code}")
    except requests.exceptions.RequestException as exc:
        print(f"the error that occurred: {exc}")

def display_cellcount(result):
    age = result['main']['age']
    bmi = result['main']['bmi']
    print(f"age: {age}")
    print(f"bmi: {bmi}")


result = handle_api(url)
if result is not None:
    pprint(result)
    #display_cellcount(result)




