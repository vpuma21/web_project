import requests

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search" # this will be step 1
FORECAST_URL = "https://api.open-meteo.com/v1/forecast" # this is for step 2

# May be late but working on creating a class and instantiate it with the variables obtained from the api call.

class WeatherObservation:
    def __init__(self, city, country, latitude, longitude, temperature_c, windspeed_kmh, observation_time):
         self.city = city
         self.country = country
         self.latitude = latitude
         self.longitude = longitude
         self.temperature_c = temperature_c
         self.windspeed_kmh = windspeed_kmh
         self.observation_time = observation_time

    def __repr__(self):
         return(
            "WeatherObservation("
            f"city={self.city!r}, country={self.country!r}, "
            f"latitude={self.latitude}, longitude={self.longitude}, "
            f"temperature_c={self.temperature_c}, windspeed_kmh={self.windspeed_kmh}, "
            f"observation_time={self.observation_time!r})"
        )

# STEP 1: GEOCODE SECTION

params = { # These are parameters for the request for the GEOCODE site
    "name": "chicago",
    "country": "US",
    "count": 1
} 

response = requests.get(GEOCODE_URL, params=params) # this will send the request from geocode

data = response.json() # this converts it to JSON
location = data["results"][0] # data

name = location["name"]
country = location["country"]
latitude = location["latitude"] 
longitude = location["longitude"]

# print("city", name)
# print("country", country)
# print("latitide", latitude) # we need to extract this
# print("longitude", longitude)# and extract this

# STEP 2: FORECAST SECTION 

forecast_param = { # retriving the latitude and longitude from previous step
    "latitude": latitude,
    "longitude": longitude,
    "current_weather": True
}

response2 = requests.get(FORECAST_URL, params=forecast_param) # this will send second request from forecast

weather_data = response2.json() # convert to JSON again for forecast

temperature = weather_data["current_weather"]["temperature"] # these are supposed to be added 
windspeed = weather_data["current_weather"]["windspeed"]
time = weather_data["current_weather"]["time"]

# print("Temperature:", temperature)
# print("Windspeed:", windspeed)
# print("Observation time:", time)

# STEP 3: JSON -> Python

result = { # the formatting on how it should be + python object
    "city": name,
    "country": country,
    "latitude": latitude,
    "longitude": longitude,
    "temperature_c": temperature,
    "windspeed_kmh": windspeed,
    "observation_time": time
}

# supposed to create class

print("Status", response.status_code) # this is the status code (an extra filler I wanted to add c:) should print that status is 200
print(result) # the other print out were commented out bc those were just tests to see if it works.