import datetime
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

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
        data_links.append("https://s3.amazonaws.com/tripdata/" + str(year) + month + "-citibike-tripdata.zip")

if current_month > 2:
    for month in range(1, current_month - 1):
        if month < 10:
            month = '0' + str(month)
        data_links.append("https://s3.amazonaws.com/tripdata/" + str(current_year) + month + "-citibike-tripdata.zip")

# Separate and concatenate the data
citibike_data = concatDF(data_links)

# Write to data folder
citibike_data.to_csv('data/citibike.csv', index = False)
