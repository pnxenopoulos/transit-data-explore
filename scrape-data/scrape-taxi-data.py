import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page'
page = urlopen(url)
parsed_page = BeautifulSoup(page, 'html.parser')
page_html = str(parsed_page)

all_links = re.findall('\".*\.csv\"', page_html)
data_links = all_links[:-1]

yellow, green, fhv = []
for link in data_links:
	if yellow_exists:
		#do this
	elif green_exists:
		#do this
	else:
		#do this (fhv)