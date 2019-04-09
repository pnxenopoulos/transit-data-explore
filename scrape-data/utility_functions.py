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
