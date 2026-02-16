# MILESTONE 1: HTTP Request and Server Response

### Project Description:
This project is supposed to make HTTP requests to the Open-Meteo API to retrieve weather data for a specific city.
it demonstrates how to send requests, receive server responses, and convert extracted data into a Python object.

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

### Step 3: 


