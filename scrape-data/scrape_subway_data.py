import re
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

from utility_functions import readHTMLPage, concatDF

# Call in the HTML page data
url = 'http://web.mta.info/developers/turnstile.html'
page_html = readHTMLPage(url)

# Find all links to CSVs and remove last one, which isn't data we need
all_links = re.findall('data/nyct/turnstile/turnstile_\d{6}\.txt', page_html)
url_start = 'http://web.mta.info/developers/'
data_links = [url_start + s for s in all_links]

mta_turnstile_data = pd.DataFrame()
mta_turnstile_data.columns = ['ca', ]
# Separate and concatenate the data
for link in data_links:
	mta_turnstile_data = concatDF(mta_turnstile_data, link)

mta_turnstile_data.columns = ['ca', 'unit', 'scp', 'station', 'linename', 'division', 'date', 'time', 'desc', 'entries', 'exists']
# Write to data folder
mta_turnstile_data.to_csv('data/mta_turnstile.csv', index = False)
