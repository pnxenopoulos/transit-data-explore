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
mta_cols = ['ca', 'unit', 'scp', 'station', 'linename', 'division', 'date', 'time', 'desc', 'entries', 'exists']

hit_old_data = False
i = 0

while(hit_old_data == False):
	link = data_links[i]
	mta_turnstile_data = pd.read_csv(link, skiprows = 10, header = None)
	mta_turnstile_data.columns = mta_cols
	yearmonthweek = re.findall('\d{6}', link)[0]
	mta_turnstile_data.to_csv('data/subway/' + yearmonthweek + '.csv', index = False)
	print('Wrote ' + yearmonthweek + ' subway data')
	i = i + 1
	if i == split:
		hit_old_data == True
		print('End of subway data scraping')
