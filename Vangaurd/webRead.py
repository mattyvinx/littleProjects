import pandas as pd
import requests as rq

apiKey = '85c373ea9c4190ca9ff97faeec5684b4'

tablePop = pd.read_html('https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population')
populationTable = tablePop[2]

for i in range(50): ##for the top 50 rows, parses coordinates
    coordinate = populationTable.iloc[i]["Location"].item() ##reads coordinates from table for top 50 cities. 
    cleanedCoordinate = coordinate.replace("\ufeff", "").strip() ##strips extra characters from inital read
    coordinateDecimal = cleanedCoordinate.split("/")[1] ##saves only decimal 
    splitCords = coordinateDecimal.split(" ") ##splits coordinate pair into latitude / longitude
    Lat = float(splitCords[1][:-2]) ##latitude stored as decimal
    Lon = -1*float(splitCords[2][:-2]) ##longitude stored as decimal. All values negative due western hemesphere location
    populationTable.loc[i, 'Latitude Decimal'] = Lat ##stores lat and longitude into dataframe
    populationTable.loc[i, 'Longitude Decimal'] = Lon

    url = f"http://api.openweathermap.org/data/2.5/weather?lat={Lat}&lon={Lon}&appid={apiKey}&units=imperial"
    response = rq.get(url)
    data = response.json()

    # Check if the request was successful
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

    
print (populationTable.head(50))
    
    


'''for i in range(0,50):
    print(populationTable.iloc[i]["Location"])
    '''









##access coordinates: populationTable.iloc[i]["Location"].item()