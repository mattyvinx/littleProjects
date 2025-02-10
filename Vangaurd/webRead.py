import pandas as pd
import requests as rq
import plotly.graph_objects as mapper
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

apiKey = os.getenv("apiKey")


tablePop = pd.read_html('https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population')
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

    response = rq.get(f"http://api.openweathermap.org/data/2.5/weather?lat={Lat}&lon={Lon}&appid={apiKey}&units=imperial") ##call openweather API, get current weather.
    data = response.json()

    if response.status_code == 200: ##store current weather attributes
        temperature = data["main"]["temp"] 
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        ## Append weather info to dataframe. To be used by dashboard.
        populationTable.loc[i, 'Temperature'] = temperature
        populationTable.loc[i, 'Description'] = description
        populationTable.loc[i, 'Humidity'] = humidity
        populationTable.loc[i, 'Wind Speed'] = wind_speed
        populationTable.loc[i, 'Refresh Time'] = datetime.now()
    else: ##errors added if issue calling API.
        print("Error:", data.get("message", "Failed to retrieve data"))
        populationTable.loc[i, 'Temperature'] = 'error'
        populationTable.loc[i, 'Demperature'] = 'error'
        populationTable.loc[i, 'Humidity'] = 'error'
        populationTable.loc[i, 'Wind Speed'] = 'error'
    
    ##Daily historical average, used for dashboard.
    presentDateO = datetime.now()
    presentDayU = presentDateO.strftime("%Y-%m-%d")
    response = rq.get(f"https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={Lat}&lon={Lon}&dt={presentDayU}&appid={apiKey}")
    data = response.json()


    if response.status_code == 200:
        avgLowK = data["result"]["temp"]["average_min"] ##currently in K
        avgHighK = data["result"]["temp"]["average_max"]  ##currently in K
        avgTempK = ((avgLowK+avgHighK) / 2) ##calculate current daily average
        avgTempF = ((avgTempK - 273.15)*9/5+32) ##convert to F
        print(avgTempF)
        populationTable.loc[i, 'Daily Avereage Temp'] = avgTempF
    else:
        print(response)

        ##Append values to dataframe. To be used by dashboard as well.




errorPresent = False #validate pull successful. If not, error will be displayed. 

for i in range(50):
    if populationTable.loc[i, 'Temperature'].item() == 'error':
        errorPresent = True

if errorPresent == False:
    populationTable.to_excel('citiesWithWeather.xlsx') ##output file to be used by Tableau
    ##begin display of data
    latitudes = []
    longitudes =[]
    temperatures = []
    cities = []
    labels = []

    for i in range(50):
        latitudes.append(populationTable.iloc[i]["Latitude Decimal"].item())
        longitudes.append(populationTable.iloc[i]["Longitude Decimal"].item())
        temperatures.append(populationTable.iloc[i]["Temperature"].item())
        cities.append(populationTable.iloc[i]["City Plain Text"].item())

    labels = [f"{city}<br>Temperature: {pop:,}" for city, pop in zip(cities, temperatures)]

    mapDisplay = mapper.Figure(mapper.Scattergeo(
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

    mapDisplay.update_layout(
        geo=dict(
            scope='usa',
            projection_type='albers usa',
            showland=True,
        ),
        title="Current Temperatures in the top 50 Most Populated Cities",
    )
    mapDisplay.show()
else:
    print("Error with API read. Please try again later.")