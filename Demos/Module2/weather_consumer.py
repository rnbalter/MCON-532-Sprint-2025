"""
This is an exercise to learn how to interact with publicly available API directories to extract specific info
"""

import requests
from pprint import pprint

url = "http://api.weatherapi.com/v1/current.json"
headers = {"key": "915f3e2a470f467abb5210346252603"}



def handle_api(url, headers, params):
    """
   Creates a request to WeatherAPI from the given prompt and prints output in terminal

   Args:
       url (string): given above
       headers (string): information needed to make request ie access key
       parameters (string): determines which area will have its weather reported

   Returns:
       response.json (string) if the request status code is 200 ie successful
       boolean False if API request is unsuccessful
   """
    try:
        response = requests.get(url, headers = headers, params = params)
        if response.status_code == 200:
            print("the GET request worked :)")
            #pprint(response.json())
            return response.json()
        else: #ie if the response isnt a success
            print(f"GET request failed :( {response.status_code}")
            return False
    except requests.exceptions.RequestException as exc:
        print(f"the error that occurred: {exc}")

def display_info(result):
    """
    Prints temperature, humidity, and weather condition information neatly

    Args:
       result (string): this is the response.json requested from hande_api()

"""
    temp_f = result["current"]["temp_f"]
    humidity = result["current"]["humidity"]
    print(f"Temperature: {temp_f}°F")
    print(f"Humidity: {humidity}")
    print(f"Condition: {condition}")

def main():
    city = input("enter the name of city ")
    if city:
        params = {"q": city,
              "aqi": "no"}
        result = handle_api(url, headers, params)
        if result != False: #ie if it holds the response data bc city was accepted
            display_info(result)
    else:
        print("enter a valid city name")

if __name__ == '__main__':
    main()






