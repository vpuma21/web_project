# MILESTONE 1: HTTP Request and Server Response

### Project Description:
This project is supposed to make HTTP requests to the Open-Meteo API to retrieve weather data for a specific city.
it should be able to show how to send requests, receive server responses, and convert extracted data into the Python language.

### Step 1: The GeoCoding Request

The program will send a request to the Open-Meteo Geocoding API using a city name and a country code. 
The response should contain location data, from which the program should extract parameters, which are:
 - City 
 - Country
 - Latitude
 - Longtitude

### Step 2: The Forecast Request

In this section, It needs to retrieve the latitude and longitude from step 1. Using the retrieved latitude and longitude, the program will send a second request to Open-Meteo Forecast API. This will then return the current weather information, in which includes:

- Temperature
- Windspeed
- Elevation
- Observation Time 

### Step 3: Data Conversion (JSON to Python)

In this section, It needs to take the JSON responses from the API of the previous steps in order to convert it into Python dictionary. The program will print out the data in order to show the successed with the retrives and processing the data.

### THIS IS HOW IT"S SUPPOSED TO LOOK LIKE (sample of how final result/look of project should look like):

- {
   - "id": 1,
   - "city" : "Chicago",
   - "country": "US",
   - "latitude": 41.88,
   - "longitude" : -81.63,
   - "temperature_c" : 18.5
   - "windspeed_kmh" : 12.3
   - "observation_time": "2025-09-04T12:00:00Z",
   - "notes": null
- }

I added the status 200 as an extra since I wanted to know if the status code will be 200 was it will demonstrate it was a success in a way c:
