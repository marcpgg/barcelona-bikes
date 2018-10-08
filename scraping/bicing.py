import requests
import json
import pandas as pd
import datetime as dt
import os
import time


while True:
    try:
        url = 'https://www.bicing.cat/current-bikes-in-use.json'
        data = json.loads(requests.get(url).text)
        print ('Bicing data loaded successfully.')

        testdf = pd.DataFrame(data)
        testdf
        #testdf.assign(Date=testdf.Date.dt.round('H'))
        coorddf = testdf[['dateTime','bikesInUsage','electricalBikesInUsage', 'mechanicalBikesInUsage']]
        coorddf = coorddf.rename(columns={'bikesInUsage': 'total_bikes', 'electricalBikesInUsage': 'ebikes', 'mechanicalBikesInUsage': 'rbikes', 'dateTime': 'date'})


        # if file does not exist write header
        if not os.path.isfile('../ebikes/data/bicing_data.csv'):
            coorddf.to_csv('../ebikes/data/bicing_data.csv', header='column_names', index=False)
            print( 'File has been written successfully at'+ str(dt.Now.ToString("yyyy-MM-ddTHH:mm:sszzz")) )

            # else it exists so append without writing the header
        else:
            coorddf.to_csv('../ebikes/data/bicing_data.csv', mode='a', header=False ,index=False)
            print( 'Bicing data has been appended successfully at '+ str(dt.Now.ToString("yyyy-MM-ddTHH:mm:sszzz")) )

        time.sleep(5*60)
    except:
        print('Some error was encountered, probably bikes are sleeping now. Trying again in 10 minutes.')
        time.sleep(10*60)
