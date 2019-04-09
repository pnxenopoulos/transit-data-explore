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

mta_turnstile_data = pd.DataFrame(columns = ['ca', 'unit', 'scp', 'station', 'linename', 'division', 'date', 'time', 'desc', 'entries', 'exists'])

# Separate and concatenate the data
for i, link in enumerate(data_links):
	mta_turnstile_data = concatDF(mta_turnstile_data, link)
	if (i % 10 == 0) and (i != 0):
		filename = 'data/mta_turnstile_' + str(int(i/10)) + '.csv'
		mta_turnstile_data.to_csv(filename, index = False)
		mta_turnstile_data = pd.DataFrame(columns = ['ca', 'unit', 'scp', 'station', 'linename', 'division', 'date', 'time', 'desc', 'entries', 'exists'])
		print('Wrote ' + str(int(i/10)))
	if i == len(data_links)-1:
		filename = 'data/mta_turnstile_last.csv'
		mta_turnstile_data.to_csv(filename, index = False)
		mta_turnstile_data = pd.DataFrame(columns = ['ca', 'unit', 'scp', 'station', 'linename', 'division', 'date', 'time', 'desc', 'entries', 'exists'])
		print('Wrote ' + str(int(i/10) + 1))
