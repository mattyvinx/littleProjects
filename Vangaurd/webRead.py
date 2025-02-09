import pandas as pd
import requests as rq
import plotly.graph_objects as mapper

apiKey = '85c373ea9c4190ca9ff97faeec5684b4'

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

    response = rq.get(f"http://api.openweathermap.org/data/2.5/weather?lat={Lat}&lon={Lon}&appid={apiKey}&units=imperial")
    data = response.json()

    if response.status_code == 200:
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Print the weather details
        populationTable.loc[i, 'Temperature'] = temperature
        populationTable.loc[i, 'Description'] = description
        populationTable.loc[i, 'Humidity'] = humidity
        populationTable.loc[i, 'Wind Speed'] = wind_speed
    else:
        print("Error:", data.get("message", "Failed to retrieve data"))
        populationTable.loc[i, 'Temperature'] = 'error'
        populationTable.loc[i, 'Demperature'] = 'error'
        populationTable.loc[i, 'Humidity'] = 'error'
        populationTable.loc[i, 'Wind Speed'] = 'error'


latitudes = []
longitudes =[]
temperatures = []

for i in range(50):
    latitudes.append(populationTable.iloc[i]["Latitude Decimal"].item())
    longitudes.append(populationTable.iloc[i]["Longitude Decimal"].item())
    temperatures.append(populationTable.iloc[i]["Temperature"].item())


fig = mapper.Figure(mapper.Scattergeo(
    locationmode='USA-states',
    lat=latitudes,
    lon=longitudes,
    mode='markers+text',  # You can also use 'markers' for just the points
    marker=dict(
        size=8, 
        color=temperatures,
        colorscale=[[0, 'blue'], [1, 'red']],
        colorbar=dict(title='Temperature')),
))

fig.update_layout(
    geo=dict(
        scope='usa',
        projection_type='albers usa',
        showland=True,
    )
)
fig.show()








##access coordinates: populationTable.iloc[i]["Location"].item()