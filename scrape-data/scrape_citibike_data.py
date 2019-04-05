import datetime
import pandas as pd

from io import BytesIO
from requests import get
from zipfile import ZipFile
from utility_functions import concatDF

# Get the date
now = datetime.datetime.now()
current_year = now.year
current_month = now.month
data_links = []

for year in range(2014, current_year):
    for month in range(1,13):
        if month < 10:
            month = '0' + str(month)
        if year > 2016:
        	data_links.append("https://s3.amazonaws.com/tripdata/" + str(year) + str(month) + "-citibike-tripdata.csv.zip")
        else:
        	data_links.append("https://s3.amazonaws.com/tripdata/" + str(year) + str(month) + "-citibike-tripdata.zip")
        

if current_month > 2:
    for month in range(1, current_month - 1):
        if month < 10:
            month = '0' + str(month)
        data_links.append('https://s3.amazonaws.com/tripdata/' + str(current_year) + str(month) + '-citibike-tripdata.csv.zip')

citibike_data = pd.DataFrame()
for link in data_links:
	if '201902' in link:
		url = 'https://s3.amazonaws.com/tripdata/201902-citibike-tripdata.csv.zip'
		remotezip = get(url)
		zip_file = ZipFile(BytesIO(remotezip.content))
		temp = pd.read_csv(zip_file.open('201902-citibike-tripdata.csv'))
		temp.columns = [x.lower() for x in temp.columns]
		citibike_data = pd.concat([data, temp])
	else:
		citibike_data = concatDF(citibike_data, link)

# Write to data folder
citibike_data.to_csv('data/citibike.csv', index = False)
