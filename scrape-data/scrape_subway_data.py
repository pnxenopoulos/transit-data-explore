import re
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

from utility_functions import readHTMLPage, concatDF

# Call in the HTML page data
url = 'http://web.mta.info/developers/turnstile.html'
page_html = readHTMLPage(url)

# Find all links to CSVs and remove last one, which isn't data we need
all_links = re.findall('\".*\.txt\"', page_html)
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

# Separate and concatenate the data
yellow_cab_data = concatDF(yellow)
green_cab_data = concatDF(green)
fhv_data = concatDF(fhv)

# Write to data folder
yellow_cab_data.to_csv('data/yellow_cab_data.csv', index = False)
green_cab_data.to_csv('data/green_cab_data.csv', index = False)
fhv_data.to_csv('data/fhv_data.csv', index = False)