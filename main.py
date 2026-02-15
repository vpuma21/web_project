import requests

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search" # this will be step 1
FORECAST_URL = "https://api.open-meteo.com/v1/forecast" # ill work on step 2 monnday and tuesday

params = { # These are parameters for the request of GEOCODE
    "name": "Chicago",
    "country": "US",
    "count": 1
} 

response = requests.get(GEOCODE_URL, params=params) #
data = response.json()

latitude = data["results"][0]["latitude"]
longitude = data["results"][0]["longitude"]

print("latitude", latitude)
print("longitude", longitude)      







