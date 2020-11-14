import pandas as pd
from datetime import datetime

if __name__ == "__main__":
    dates = pd.date_range(start="2011-11-01", end="2014-02-27")
    dff = pd.DataFrame(data=None, index=dates)
    for i in range(0,112):
        df = pd.read_csv("inputs/tabular/daily_dataset/block_"+str(i)+".csv")
        df = df[['day', 'LCLid','energy_sum']]
        lclid_u = df['LCLid'].unique()
        for ul in lclid_u:
            df_ = df[df['LCLid'] == ul]
            df_.index = [datetime.strptime(x, "%Y-%m-%d") for x in df_['day']]
            dff[ul] = df_['energy_sum']
    
    dff.dropna(axis=0, how="all", inplace=True)
    dff["count"] = dff.count(axis=1)
    dff["average"] = dff.mean(axis=1, skipna=True)

    energy = dff[["count", "average"]]
    energy.index.name = "time"

    weather = pd.read_csv("inputs/tabular/weather_daily_darksky.csv")
    
    weather['time'] =  [x.date() for x in pd.to_datetime(weather['time'])]
    weather.index = weather['time']

    features = ['pressure', 'humidity',  'temperatureMin', 'temperatureMax']

    weather = weather[features]

    #energy = energy.merge(weather)
    weather.to_csv("inputs/tabular/weather.csv")
    energy.to_csv("inputs/tabular/energy.csv")
