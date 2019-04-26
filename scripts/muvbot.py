import requests
import json
import pandas as pd
import datetime as dt
import os
import time


while True:
    try:
        url = 'https://XXXXXXXXXXXXXXXX/XXX/XX/X/in_rectangle?lat1=41.49913121537122&lon1=2.286477237939835&lat2=41.325331221845914&lon2=2.0427180826663975'
        data = json.loads(requests.get(url).text)
        print ('Muving data loaded successfully.')

        temps = dt.datetime.now().strftime('%Y%m%d %H:%M')
        testdf = pd.DataFrame(data['object'])
        testdf['date'] = pd.Series([pd.Timestamp(temps)] * len(testdf))
        #testdf.assign(Date=testdf.Date.dt.round('H'))
        coorddf = testdf[['date','vehicleRegistration','lat', 'lon', 'charge', 'estimatedRange']]
        coorddf = coorddf.rename(columns={'vehicleRegistration': 'plate', 'estimatedRange': 'range'})


        # if file does not exist write header
        if not os.path.isfile('../ebikes/data/muving_data.csv'):
            coorddf.to_csv('../ebikes/data/muving_data.csv', header='column_names', index=False)
            print( 'File has been written successfully at'+ str(temps) )

            # else it exists so append without writing the header
        else:
            coorddf.to_csv('../ebikes/data/muving_data.csv', mode='a', header=False ,index=False)
            print( 'Muving data has been appended successfully at '+ str(temps) )

        time.sleep(5*60)
    except:
        print('Some error was encountered, probably bikes are sleeping now. Trying again in 10 minutes.')
        time.sleep(10*60)
