import pandas as pd
import requests as rq
import plotly.graph_objects as mapper
from dotenv import load_dotenv #used for loading API from .env file
import os 
from datetime import datetime



load_dotenv() ##pulls API from .env file

apiKey = os.getenv("apiKey")

#city region assignment, used in dashboard
Northeast = ["ME", "NH", "VT", "MA", "CT", "RI", "NJ", "NY", "PA"]
South = ["WV", "MD", "DE", "DC", "VA", "WV", "KY", "TN", "NC", "SC", "GA", "FL", "MS", "AL", "AR", "OK", "LA", "TX"]
Midwest = ["ND", "MN", "WI", "MI", "SD", "IA", "IL", "IN", "OH", "NE", "MO", "KS"]
West = ["WA", "ID", "MT", "OR", "WY", "CA", "NV", "UT", "CO", "AZ", "NM"]

#pull in from wikipedia
tablePop = pd.read_html('https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population')

#store city table
populationTable = tablePop[2]
for i in range(50): ##for the top 50 rows, pulls coordinates. Coordinates then used to pull current weather information. 
    coordinate = populationTable.iloc[i]["Location"].item() ##reads coordinates from table for top 50 cities. 
    cleanedCoordinate = coordinate.replace("\ufeff", "").strip() ##strips extra characters from inital read
    coordinateDecimal = cleanedCoordinate.split("/")[1] ##saves only decimal 
    splitCords = coordinateDecimal.split(" ") ##splits coordinate pair into latitude / longitude
    Lat = float(splitCords[1][:-2]) ##latitude stored as decimal, to be used in API call
    Lon = -1*float(splitCords[2][:-2]) ##longitude stored as decimal. All values negative due western hemesphere location, used in API call
    populationTable.loc[i, 'Latitude Decimal'] = Lat ##stores lat and longitude into dataframe along with corresponding city
    populationTable.loc[i, 'Longitude Decimal'] = Lon
    cityString = populationTable.iloc[i]["City"].item() #clears special marks from city names.
    cityStringCleaned = cityString.split("[")[0] 
    populationTable.loc[i, "City Plain Text"] = cityStringCleaned #stores cleaned names
    if populationTable.iloc[i]["ST"].item() in Northeast: #region storage 
        populationTable.loc[i, "Region"] = "Northeast"
    elif populationTable.iloc[i]["ST"].item() in South:
        populationTable.loc[i, "Region"] = "South"
    elif populationTable.iloc[i]["ST"].item() in Midwest:
        populationTable.loc[i, "Region"] = "Midwest"
    elif populationTable.iloc[i]["ST"].item() in West:
        populationTable.loc[i, "Region"] = "West"
    
    
    response = rq.get(f"http://api.openweathermap.org/data/2.5/weather?lat={Lat}&lon={Lon}&appid={apiKey}&units=imperial") ##call openweather API, get current weather.
    data = response.json()

    if response.status_code == 200: ##store current weather attributes if call successful 
        temperature = data["main"]["temp"] 
        feelsLike = data["main"]["feels_like"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        ## Append weather info to dataframe. To be used by dashboard.
        populationTable.loc[i, 'Temperature'] = temperature
        populationTable.loc[i, 'Feels Like Temp'] = feelsLike
        populationTable.loc[i, 'Description'] = description
        populationTable.loc[i, 'Humidity'] = humidity
        populationTable.loc[i, 'Wind Speed'] = wind_speed
    else: ##errors added if issue calling API.
        populationTable.loc[i, 'Temperature'] = 'error'

    ##pull in weather alerts, if present
    response = rq.get(f"https://api.weather.gov/points/{Lat},{Lon}") ##convert to NWS zone for current city
    data = response.json()
   
    if response.status_code==200: #if zone received, ask for alerts from NWS
        forecastZoneURL = data["properties"]["forecastZone"]
        forecastZone = forecastZoneURL.split("/")[-1] 
        response = rq.get(f"https://api.weather.gov/alerts/active?zone={forecastZone}") ##convert to NWS zone for current city
        data = response.json()
        if response.status_code==200 and data['features']: #verify that alerts are active, and response received
            event = data["features"][0]["properties"]["event"]
            severity = data["features"][0]["properties"]["severity"]
            populationTable.loc[i, 'Weather Event'] = event #store data for Tableau
            populationTable.loc[i, 'Event Severity'] = severity
        else:
            populationTable.loc[i, 'Weather Event'] = "No Ongoing Events"
            populationTable.loc[i, 'Event Severity'] = "N/A"
    else:
        populationTable.loc[i, 'Alerts'] = "None"
        populationTable.loc[i, 'Event Severity'] = "N/A"
    populationTable.loc[i, 'Refresh Time'] = datetime.now() #add refresh time for latest pull
    print (f"API Calls {i*2}% complete.", end = '\r', flush=True) ##display ongoing API progress

errorPresent = False #validate pull successful. If not, error will be displayed. 

for i in range(50): #check to verify that all items have populated as expected
    if populationTable.loc[i, 'Temperature'].item() == 'error':
        errorPresent = True #sets error check to true, stopping file from creation and map from creation

if errorPresent == False:
    populationTable[:50].to_excel('citiesWithWeather.xlsx') ##output file to be used by Tableau Dashboard. Minor cleanup needed after.
    ##begin display of data on map
    latitudes = []
    longitudes =[]
    temperatures = []
    cities = []
    labels = []

    for i in range(50): #populate lists, used for map
        latitudes.append(populationTable.iloc[i]["Latitude Decimal"].item())
        longitudes.append(populationTable.iloc[i]["Longitude Decimal"].item())
        temperatures.append(populationTable.iloc[i]["Temperature"].item())
        cities.append(populationTable.iloc[i]["City Plain Text"].item())

    labels = [f"{city}<br>Temperature: {temp:,}" for city, temp in zip(cities, temperatures)]

    mapDisplay = mapper.Figure(mapper.Scattergeo( #data appended to map
        locationmode='USA-states',
        lat=latitudes,
        lon=longitudes,
        text=cities,
        hovertext = labels,
        hoverinfo = 'text',
        mode='markers',
        marker=dict(
            size=8, 
            color=temperatures,
            colorscale=[[0, 'blue'], [1, 'red']],
            colorbar=dict(title='Temperature')),
    ))

    mapDisplay.update_layout( #display updated
        geo=dict(
            scope='usa',
            projection_type='albers usa',
            showland=True,
        ),
        title="Current Temperatures - Top 50 Most Populated Cities in the US",
    )
    mapDisplay.show()
else:
    print("Error with API read. Please try again later.")