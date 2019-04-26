import requests
import json
import pandas as pd
import datetime as dt
import os
import time


while True:
    try:
        url = 'https://XXXXXXXX.XXXXX.json?'
        data = json.loads(requests.get(url).text)
        print ('Scoot data loaded successfully.')

        temps = dt.datetime.now().strftime('%Y%m%d %H:%M')
        testdf = pd.DataFrame(columns=['date','id', 'lat', 'lon', 'charge', 'type'])
        i = 0
        for item in data['scooters']:
            _addon = pd.Series({'id': item['physical_scoot_id'],'lat': item['latitude'], 'lon': item['longitude'], 'charge': item['batt_pct_smoothed'], 'type': item['vehicle_type']['vehicle_class'] })
            testdf.loc[i] = _addon
            i+=1
        testdf['date'] = pd.Series([pd.Timestamp(temps)] * len(testdf))

        # if file does not exist write header
        if not os.path.isfile('../ebikes/data/scoot_data.csv'):
            testdf.to_csv('../ebikes/data/scoot_data.csv', header='column_names', index=False)
            print( 'File has been written successfully at'+ str(temps) )

            # else it exists so append without writing the header
        else:
            testdf.to_csv('../ebikes/data/scoot_data.csv', mode='a', header=False ,index=False)
            print( 'Scoot data has been appended successfully at '+ str(temps) )

        time.sleep(5*60)
    except:
        print('Some error was encountered, probably bikes are sleeping now. Trying again in 10 minutes.')
        time.sleep(10*60)
