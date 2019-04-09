import re
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

from utility_functions import readHTMLPage, concatDF

# Call in the HTML page data
url = 'https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page'
page_html = readHTMLPage(url)

# Find all links to CSVs and remove last one, which isn't data we need
all_links = re.findall('\".*\.csv\"', page_html)
data_links = all_links[:-1]

# add links to yellow cab, green cab and fhv lists
yellow, green, fhv = [], [], []
for link in data_links:
	link = link.replace('\"', '')
	if bool(re.search('yellow', link)):
		yellow.append(link)
	elif bool(re.search('green', link)):
		green.append(link)
	else:
		fhv.append(link)

yellow_cab_data = pd.DataFrame()
for i, link in enumerate(yellow):
	yellow_cab_data = concatDF(yellow_cab_data, link)
	if (i % 5 == 0) and (i != 0):
		filename = 'data/yellow_cab_' + str(int(i/5)) + '.csv'
		mta_turnstile_data.to_csv(filename, index = False)
		mta_turnstile_data = pd.DataFrame(columns = ['ca', 'unit', 'scp', 'station', 'linename', 'division', 'date', 'time', 'desc', 'entries', 'exists'])
		print('Wrote ' + str(int(i/10)))

green_cab_data = pd.DataFrame(columns = ['VendorID', 'lpep_pickup_datetime', 'lpep_dropoff_datetime', 'store_and_fwd_flag', 'RatecodeID', 'PULocationID', 'DOLocationID', 'passenger_count', 'trip_distance', 'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount', 'ehail_fee', 'improvement_surcharge', 'total_amount', 'payment_type', 'trip_type'])
for i, link in enumerate(yellow):
	green_cab_data = concatDF(green_cab_data, link)

# Separate and concatenate the data
yellow_cab_data = concatDF(yellow)
green_cab_data = concatDF(green)
fhv_data = concatDF(fhv)

# Write to data folder
yellow_cab_data.to_csv('data/yellow_cab_data.csv', index = False)
green_cab_data.to_csv('data/green_cab_data.csv', index = False)
fhv_data.to_csv('data/fhv_data.csv', index = False)