import re
import datetime
import pandas as pd

from io import BytesIO
from requests import get
from zipfile import ZipFile

# Get the date
now = datetime.datetime.now()
current_year = now.year
current_month = now.month
data_links = []

# Create list of links to loop through
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

citibike_cols = ['trip_duration', 'start_time', 'stop_time', 'start_station_id', 'start_station_name', 'start_station_lat', 'start_station_lon', 'end_station_id', 'end_station_name', 'end_station_lat', 'end_station_lon', 'bike_id', 'user_type', 'birth_year', 'gender']

for link in data_links:
	if '201902' in link:
		# 201902 has more than one file in the zip, this is to fix that
		url = 'https://s3.amazonaws.com/tripdata/201902-citibike-tripdata.csv.zip'
		remotezip = get(url)
		zip_file = ZipFile(BytesIO(remotezip.content))
		citibike_data = pd.read_csv(zip_file.open('201902-citibike-tripdata.csv'), header = None, skiprows = 1)
		citibike_data.columns = citibike_cols
		citibike_data.to_csv('data/citibike/201902-citibike.csv', index = False)
	else:
		citibike_data = pd.read_csv(link, header = None, skiprows = 1)
		citibike_data.columns = citibike_cols
		yearmonth = re.findall('\d{6}', link)[0]
		citibike_data.to_csv('data/citibike/' + yearmonth + '-citibike.csv', index = False)
		print('Wrote ' + yearmonth)