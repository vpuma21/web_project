# MILESTONE 1: HTTP Request and Server Response

### Milestone Description:
This Milestone is supposed to make HTTP requests to the Open-Meteo API to retrieve weather data for a specific city.
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

In this section, It needs to take the JSON responses from the API of the previous steps in order to convert it into Python dictionary. The program will print out the data in order to show the successed with the retrives and processing the data. This also means that I need to work on creating a class and instantiate it with the variables obtained from the api call.

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

# MILESTONE 2: Flask Server and CRUD ROUTES

### Milestone Description:

In this Milestone, Previous Milestone will be expanding it's API code by implementing a Flask Server and have routes for CRUD operations. The Flash server will be like the backend of the website, allowing the user to interact with the weather data system through the said routes. These routes will be handling create,read,update,and delete records. For now it should return strings/HTML responses.

### Step 1: 
In this step, a Flask application is created to serve as the backend server. The server will act as the entry point of the application and handle incoming requests from the user. The Flask server will initialize the application and run it locally so routes can be accessed through the browser.

### Step 2:
A new file called routes.py is created to define the application's routes. These routes represent the CRUD operations:
   - Create
   - Read
   - Update
   - Delete

Each route currently returns a simple string or HTML response since database functionality has not yet been implemented. These routes will later be expanded to interact with the database.


### Step 3:
The requirements.txt is updated in order to see all necessary dependencies needed for this project to run. Which includes:
   - Flask
   - Requests
This will allow the environment to install all required packages.
