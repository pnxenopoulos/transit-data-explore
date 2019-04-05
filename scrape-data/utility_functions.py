import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

def readHTMLPage(url):
	''' This is a function to read an HTML page and output a string of its text
	@param url String: A string of a url to read
	'''
	page = urlopen(url)
	parsed_page = BeautifulSoup(page, 'html.parser')
	page_html = str(parsed_page)
	return page_html

def concatDF(files):
	''' This is a function to read in a list of filepaths/urls and concatenate all of the dataframes into one
	@param files List: A list of filepaths/urls to read
	'''
	data = pd.DataFrame()
	for file in files:
		print('Reading in ', file)
		temp = pd.read_csv(file)
		temp.columns = [x.lower() for x in temp.columns]
		data = pd.concat([data, temp])
	return data