''' ##pulling historical averages, currently inactive
    presentTime = datetime.now()
    presentMonth, presentDay, presentHour = presentTime.month, presentTime.day, presentTime.hour

    years = [presentTime.year - i for i in range(1, 6)]
    timeStampsUNIX = [int(time.mktime(datetime(year, presentMonth, presentDay, presentHour, 0).timetuple())) for year in years]

    for tsu in timeStampsUNIX:
        response = rq.get(f"https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={Lat}&lon={Lon}&dt={tsu}&appid={apiKey}")
        data = response.json()
        avgTempL = []
        if response.status_code == 200:
            if "data" in data and len(data["data"]) > 0:
                tempK = data['data'][0]['temp']
                tempF = (tempK - 273.15) * 9/5 + 32
                avgTempL.append(tempF)
                avgTemp = 0
                tempSum = 0
                for temp in avgTempL:
                    tempSum+=temp
                avgTemp = tempSum/5
                populationTable.loc[i, 'Average Temp Last 5'] = avgTemp
            else:
                print("Data not available for given time")
                populationTable.loc[i, 'Average Temp Last 5'] = 'N/A'
        else:
            print("Response Error")
            populationTable.loc[i, 'Average Temp Last 5'] = 'N/A'
'''