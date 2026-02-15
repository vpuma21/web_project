import requests

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search" # this will be step 1
FORECAST_URL = "https://api.open-meteo.com/v1/forecast" # ill work on step 2 monnday and tuesday

# STEP 1: GEOCODE SECTION

params = { # These are parameters for the request for the GEOCODE site
    "name": "chicago",
    "country": "US",
    "count": 1
} 

response = requests.get(GEOCODE_URL, params=params) # this will send the request

data = response.json() # this converts it to JSON

latitude = data["results"][0]["latitude"] # extracting latitude
longitude = data["results"][0]["longitude"]# extracting longitude

print(data)

# STEP 2 FORECAST SECTION 










