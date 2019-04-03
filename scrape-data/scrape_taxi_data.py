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

# Separate and concatenate the data
yellow_cab_data = concatDF(yellow)
green_cab_data = concatDF(green)
fhv_data = concatDF(fhv)