import re
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

from utility_functions import readHTMLPage

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

#yellow_cab_cols = ['vendor_id', 'tpep_pickup_datetime', 'tpep_dropoff_datetime','passenger_count', 'trip_distance', 'ratecodeid', 'store_and_fwd_flag', 'pulocationid', 'dolocationid', 'payment_type', 'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount', 'improvement_surcharge', 'total_amount']

#green_cab_cols = ['vendor_id', 'lpep_pickup_datetime', 'lpep_dropoff_datetime', 'store_and_fwd_flag', 'ratecode_id', 'pu_location_id', 'do_location_id', 'passenger_count', 'trip_distance', 'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount', 'ehail_fee', 'improvement_surcharge', 'total_amount', 'payment_type', 'trip_type']

# dont forget to add skiprows = 1, header = None in real downloads
for link in yellow:
	yearmonth = re.findall('\d{4}-\d{2}', link)[0]
	filename = 'data/vehicle/yellow/yellow_' + yearmonth + '.csv'
	yellow_cab_data = pd.read_csv(link)
	#yellow_cab_data.columns = yellow_cab_cols
	yellow_cab_data.to_csv(filename, index = False)

for link in green:
	yearmonth = re.findall('\d{4}-\d{2}', link)[0]
	filename = 'data/vehicle/green/green_' + yearmonth + '.csv'
	green_cab_data = pd.read_csv(link)
	#green_cab_data.columns = green_cab_cols
	green_cab_data.to_csv(filename, index = False)

for link in fhv:
	yearmonth = re.findall('\d{4}-\d{2}', link)[0]
	filename = 'data/vehicle/fhv/fhv_' + yearmonth + '.csv'
	green_cab_data = pd.read_csv(link)
	#green_cab_data.columns = green_cab_cols
	green_cab_data.to_csv(filename, index = False)