import time
import datetime
import pandas as pd
import csv

## FUNCTION FOR DOWNLOADING SHARE INFORMATION ##
def shareDATA():
    period1 = int(time.mktime(datetime.datetime.strptime(fromDATE, "%Y,%m,%d").timetuple()))  # conversion of date to seconds; year, month, day
    period2 = int(time.mktime(datetime.datetime.strptime(toDATE, "%Y,%m,%d").timetuple())) # conversion of date to seconds; year, month, day
    interval = '1d'

    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

    df = pd.read_csv(query_string)
    df.to_csv(f'{ticker}historicalshareprice.csv', index=False)

## DETAILS OF DESIRED SHARES ARE STORED IN CSV FORM INDICATING TICKER, FROM DATE and TO DATE
with open(f'tickerdetails.csv', 'r') as csv_file: # batch form's name is static
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        ticker = line[0]
        fromYEAR = line[1]
        fromMONTH = line[2]
        fromDAY = line[3]
        toYEAR = line[4]
        toMONTH = line[5]
        toDAY = line[6]
        fromDATE = f'{fromYEAR},{fromMONTH},{fromDAY}'
        toDATE = f'{toYEAR},{toMONTH},{toDAY}'
        print(f'Downloading {ticker} data')
        shareDATA()

print("SHARE DATA DOWNLOAD COMPLETE")

