import re
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

from utility_functions import readHTMLPage

# Call in the HTML page data
url = 'http://web.mta.info/developers/turnstile.html'
page_html = readHTMLPage(url)

# Find all links to CSVs and remove last one, which isn't data we need
all_links = re.findall('data/nyct/turnstile/turnstile_\d{6}\.txt', page_html)
url_start = 'http://web.mta.info/developers/'
data_links = [url_start + s for s in all_links]

split = data_links.index('http://web.mta.info/developers/data/nyct/turnstile/turnstile_141018.txt')
mta_new_cols = ['ca', 'unit', 'scp', 'station', 'linename', 'division', 'date', 'time', 'desc', 'entries', 'exists']
mta_old_cols = ['ca', 'unit', 'scp', 'date', 'time', 'desc', 'entries', 'exists']

for i, link in enumerate(data_links):
	if i <= split:
		if link == 'http://web.mta.info/developers/data/nyct/turnstile/turnstile_120714.txt':
			mta_turnstile_data = pd.read_csv(link, skiprows = 10, header = None)
			mta_turnstile_data.columns = mta_new_cols
			yearmonthweek = re.findall('\d{6}', link)[0]
			mta_turnstile_data.to_csv('data/subway/new/' + yearmonthweek + '.csv', index = False)
			print('Wrote ' + yearmonthweek)
		else:
			mta_turnstile_data = pd.read_csv(link, header = None)
			mta_turnstile_data.columns = mta_new_cols
			yearmonthweek = re.findall('\d{6}', link)[0]
			mta_turnstile_data.to_csv('data/subway/new/' + yearmonthweek + '.csv', index = False)
			print('Wrote ' + yearmonthweek)
	else:
		mta_turnstile_data = pd.read_csv(link, header = None)
		yearmonthweek = re.findall('\d{6}', link)[0]
		mta_turnstile_data.to_csv('data/subway/old/' + yearmonthweek + '.csv', index = False)
		print('Wrote ' + yearmonthweek)